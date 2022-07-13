/**
 * Modified version of the reveal.js speaker notes plugin.
 *
 * Changes from original are listed in the README file.
 */

(function () {

    var notes,
        notesValue,
        currentState,
        currentSlide,
        upcomingSlide,
        layoutLabel,
        layoutDropdown,
        pendingCalls = {},
        lastRevealApiCallId = 0,
        connected = false

    var connectionStatus = document.querySelector('#connection-status');

    var SPEAKER_LAYOUTS = {
        'default': 'Default',
        'notes-only': 'Notes only'
    };

    setupLayout();

    let openerOrigin;


    try {
        openerOrigin = window.opener.location.origin;
    }
    catch (error) { console.warn(error) }

    // In order to prevent XSS, the speaker view will only run if its
    // opener has the same origin as itself
    if (window.location.origin !== openerOrigin) {
        connectionStatus.innerHTML = 'Error: The speaker notes window can only be opened from the same origin and by a slide deck.';
        return;
    }

    var connectionTimeout = setTimeout(function () {
        connectionStatus.innerHTML = 'Error connecting to main window.<br>Please try closing and reopening the speaker view.';
    }, 5000);

    window.addEventListener('message', function (event) {

        clearTimeout(connectionTimeout);
        connectionStatus.style.display = 'none';

        var data = JSON.parse(event.data);

        // The overview mode is only useful to the reveal.js instance
        // where navigation occurs so we don't sync it
        if (data.state) delete data.state.overview;

        // Messages sent by the notes plugin inside of the main window
        if (data && data.namespace === 'reveal-notes') {
            if (data.type === 'connect') {
                handleConnectMessage(data);
            }
            else if (data.type === 'state') {
                handleStateMessage(data);
            }
            else if (data.type === 'return') {
                pendingCalls[data.callId](data.result);
                delete pendingCalls[data.callId];
            }
        }
        // Messages sent by the reveal.js inside of the current slide preview
        else if (data && data.namespace === 'reveal') {
            if (/ready/.test(data.eventName)) {
                // Send a message back to notify that the handshake is complete
                window.opener.postMessage(JSON.stringify({ namespace: 'reveal-notes', type: 'connected' }), '*');
            }
            else if (/slidechanged|fragmentshown|fragmenthidden|paused|resumed/.test(data.eventName) && currentState !== JSON.stringify(data.state)) {

                dispatchStateToMainWindow(data.state);

            }
        }

    });

    /**
     * Updates the presentation in the main window to match the state
     * of the presentation in the notes window.
     */
    const dispatchStateToMainWindow = debounce((state) => {
        window.opener.postMessage(JSON.stringify({ method: 'setState', args: [state] }), '*');
    }, 500);

    /**
     * Asynchronously calls the Reveal.js API of the main frame.
     */
    function callRevealApi(methodName, methodArguments, callback) {

        var callId = ++lastRevealApiCallId;
        pendingCalls[callId] = callback;
        window.opener.postMessage(JSON.stringify({
            namespace: 'reveal-notes',
            type: 'call',
            callId: callId,
            methodName: methodName,
            arguments: methodArguments
        }), '*');

    }

    /**
     * Called when the main window is trying to establish a
     * connection.
     */
    function handleConnectMessage(data) {

        if (connected === false) {
            connected = true;

            setupIframes(data);
            setupKeyboard();
            setupNotes();
            setupTimer();
            setupHeartbeat();
        }

    }

    /**
     * Called when the main window sends an updated state.
     */
    function handleStateMessage(data) {

        // Store the most recently set state to avoid circular loops
        // applying the same state
        currentState = JSON.stringify(data.state);

        // No need for updating the notes in case of fragment changes
        if (data.notes) {
            notes.classList.remove('hidden');
            notesValue.style.whiteSpace = data.whitespace;
            notesValue.innerHTML = data.notes;
            setupNoteCopyEvents();
        }
        else {
            notes.classList.add('hidden');
        }

        // Update the note slides
        currentSlide.contentWindow.postMessage(JSON.stringify({ method: 'setState', args: [data.state] }), '*');
        upcomingSlide.contentWindow.postMessage(JSON.stringify({ method: 'setState', args: [data.state] }), '*');
        upcomingSlide.contentWindow.postMessage(JSON.stringify({ method: 'next' }), '*');

    }

    // Limit to max one state update per X ms
    handleStateMessage = debounce(handleStateMessage, 200);

    /**
     * Forward keyboard events to the current slide window.
     * This enables keyboard events to work even if focus
     * isn't set on the current slide iframe.
     *
     * Block F5 default handling, it reloads and disconnects
     * the speaker notes window.
     */
    function setupKeyboard() {

        document.addEventListener('keydown', function (event) {
            if (event.keyCode === 116 || (event.metaKey && event.keyCode === 82)) {
                event.preventDefault();
                return false;
            }
            currentSlide.contentWindow.postMessage(JSON.stringify({ method: 'triggerKey', args: [event.keyCode] }), '*');
        });

    }

    /**
     * Creates the preview iframes.
     */
    function setupIframes(data) {

        var params = [
            'receiver',
            'progress=false',
            'history=false',
            'transition=none',
            'autoSlide=0',
            'backgroundTransition=none',
            'hide-controls-modal',
        ].join('&');

        var urlSeparator = /\?/.test(data.url) ? '&' : '?';
        var hash = '#/' + data.state.indexh + '/' + data.state.indexv;
        var currentURL = data.url + urlSeparator + params + '&postMessageEvents=true' + hash;
        var upcomingURL = data.url + urlSeparator + params + '&controls=false&keyboard=false' + hash;

        currentSlide = document.createElement('iframe');
        currentSlide.setAttribute('width', 1280);
        currentSlide.setAttribute('height', 1024);
        currentSlide.setAttribute('src', currentURL);
        document.querySelector('#current-slide').appendChild(currentSlide);

        upcomingSlide = document.createElement('iframe');
        upcomingSlide.setAttribute('width', 640);
        upcomingSlide.setAttribute('height', 512);
        upcomingSlide.setAttribute('src', upcomingURL);
        document.querySelector('#upcoming-slide').appendChild(upcomingSlide);

    }

    /**
     * Setup the notes UI.
     */
    function setupNotes() {

        notes = document.querySelector('.speaker-controls-notes');
        notesValue = document.querySelector('.speaker-controls-notes .value');
    }

    /**
     * We send out a heartbeat at all times to ensure we can
     * reconnect with the main presentation window after reloads.
     */
    function setupHeartbeat() {

        setInterval(() => {
            window.opener.postMessage(JSON.stringify({ namespace: 'reveal-notes', type: 'heartbeat' }), '*');
        }, 1000);

    }

    function getTimings(callback) {

        callRevealApi('getSlidesAttributes', [], function (slideAttributes) {
            callRevealApi('getConfig', [], function (config) {
                var totalTime = config.totalTime;
                var minTimePerSlide = config.minimumTimePerSlide || 0;
                var defaultTiming = config.defaultTiming;
                if ((defaultTiming == null) && (totalTime == null)) {
                    callback(null);
                    return;
                }
                // Setting totalTime overrides defaultTiming
                if (totalTime) {
                    defaultTiming = 0;
                }
                var timings = [];
                for (var i in slideAttributes) {
                    var slide = slideAttributes[i];
                    var timing = defaultTiming;
                    if (slide.hasOwnProperty('data-timing')) {
                        var t = slide['data-timing'];
                        timing = parseInt(t);
                        if (isNaN(timing)) {
                            console.warn("Could not parse timing '" + t + "' of slide " + i + "; using default of " + defaultTiming);
                            timing = defaultTiming;
                        }
                    }
                    timings.push(timing);
                }
                if (totalTime) {
                    // After we've allocated time to individual slides, we summarize it and
                    // subtract it from the total time
                    var remainingTime = totalTime - timings.reduce(function (a, b) { return a + b; }, 0);
                    // The remaining time is divided by the number of slides that have 0 seconds
                    // allocated at the moment, giving the average time-per-slide on the remaining slides
                    var remainingSlides = (timings.filter(function (x) { return x == 0 })).length
                    var timePerSlide = Math.round(remainingTime / remainingSlides, 0)
                    // And now we replace every zero-value timing with that average
                    timings = timings.map(function (x) { return (x == 0 ? timePerSlide : x) });
                }
                var slidesUnderMinimum = timings.filter(function (x) { return (x < minTimePerSlide) }).length
                if (slidesUnderMinimum) {
                    message = "The pacing time for " + slidesUnderMinimum + " slide(s) is under the configured minimum of " + minTimePerSlide + " seconds. Check the data-timing attribute on individual slides, or consider increasing the totalTime or minimumTimePerSlide configuration options (or removing some slides).";
                    alert(message);
                }
                callback(timings);
            });
        });

    }

    /**
     * Return the number of seconds allocated for presenting
     * all slides up to and including this one.
     */
    function getTimeAllocated(timings, callback) {

        callRevealApi('getSlidePastCount', [], function (currentSlide) {
            var allocated = 0;
            for (var i in timings.slice(0, currentSlide + 1)) {
                allocated += timings[i];
            }
            callback(allocated);
        });

    }

    /**
     * Create the timer and clock and start updating them
     * at an interval.
     */
    function setupTimer() {

        var start = new Date(),
            timeEl = document.querySelector('.speaker-controls-time'),
            clockEl = timeEl.querySelector('.clock-value'),
            hoursEl = timeEl.querySelector('.hours-value'),
            minutesEl = timeEl.querySelector('.minutes-value'),
            secondsEl = timeEl.querySelector('.seconds-value'),
            pacingTitleEl = timeEl.querySelector('.pacing-title'),
            pacingEl = timeEl.querySelector('.pacing'),
            pacingHoursEl = pacingEl.querySelector('.hours-value'),
            pacingMinutesEl = pacingEl.querySelector('.minutes-value'),
            pacingSecondsEl = pacingEl.querySelector('.seconds-value');

        var timings = null;
        getTimings(function (_timings) {

            timings = _timings;
            if (_timings !== null) {
                pacingTitleEl.style.removeProperty('display');
                pacingEl.style.removeProperty('display');
            }

            // Update once directly
            _updateTimer();

            // Then update every second
            setInterval(_updateTimer, 1000);

        });


        function _resetTimer() {

            if (timings == null) {
                start = new Date();
                _updateTimer();
            }
            else {
                // Reset timer to beginning of current slide
                getTimeAllocated(timings, function (slideEndTimingSeconds) {
                    var slideEndTiming = slideEndTimingSeconds * 1000;
                    callRevealApi('getSlidePastCount', [], function (currentSlide) {
                        var currentSlideTiming = timings[currentSlide] * 1000;
                        var previousSlidesTiming = slideEndTiming - currentSlideTiming;
                        var now = new Date();
                        start = new Date(now.getTime() - previousSlidesTiming);
                        _updateTimer();
                    });
                });
            }

        }

        timeEl.addEventListener('click', function () {
            _resetTimer();
            return false;
        });

        function _displayTime(hrEl, minEl, secEl, time) {

            var sign = Math.sign(time) == -1 ? "-" : "";
            time = Math.abs(Math.round(time / 1000));
            var seconds = time % 60;
            var minutes = Math.floor(time / 60) % 60;
            var hours = Math.floor(time / (60 * 60));
            hrEl.innerHTML = sign + zeroPadInteger(hours);
            if (hours == 0) {
                hrEl.classList.add('mute');
            }
            else {
                hrEl.classList.remove('mute');
            }
            minEl.innerHTML = ':' + zeroPadInteger(minutes);
            if (hours == 0 && minutes == 0) {
                minEl.classList.add('mute');
            }
            else {
                minEl.classList.remove('mute');
            }
            secEl.innerHTML = ':' + zeroPadInteger(seconds);
        }

        function _updateTimer() {

            var diff, hours, minutes, seconds,
                now = new Date();

            diff = now.getTime() - start.getTime();

            clockEl.innerHTML = now.toLocaleTimeString('en-US', { hour12: true, hour: '2-digit', minute: '2-digit' });
            _displayTime(hoursEl, minutesEl, secondsEl, diff);
            if (timings !== null) {
                _updatePacing(diff);
            }

        }

        function _updatePacing(diff) {

            getTimeAllocated(timings, function (slideEndTimingSeconds) {
                var slideEndTiming = slideEndTimingSeconds * 1000;

                callRevealApi('getSlidePastCount', [], function (currentSlide) {
                    var currentSlideTiming = timings[currentSlide] * 1000;
                    var timeLeftCurrentSlide = slideEndTiming - diff;
                    if (timeLeftCurrentSlide < 0) {
                        pacingEl.className = 'pacing behind';
                    }
                    else if (timeLeftCurrentSlide < currentSlideTiming) {
                        pacingEl.className = 'pacing on-track';
                    }
                    else {
                        pacingEl.className = 'pacing ahead';
                    }
                    _displayTime(pacingHoursEl, pacingMinutesEl, pacingSecondsEl, timeLeftCurrentSlide);
                });
            });
        }

    }

    /**
     * Sets up the speaker view layout and layout selector.
     */
    function setupLayout() {

        layoutDropdown = document.querySelector('.speaker-layout-dropdown');
        layoutLabel = document.querySelector('.speaker-layout-label');

        // Render the list of available layouts
        for (var id in SPEAKER_LAYOUTS) {
            var option = document.createElement('option');
            option.setAttribute('value', id);
            option.textContent = SPEAKER_LAYOUTS[id];
            layoutDropdown.appendChild(option);
        }

        // Monitor the dropdown for changes
        layoutDropdown.addEventListener('change', function (event) {

            setLayout(layoutDropdown.value);

        }, false);

        // Restore any currently persisted layout
        setLayout(getLayout());

    }

    /**
     * Sets a new speaker view layout. The layout is persisted
     * in local storage.
     */
    function setLayout(value) {

        var title = SPEAKER_LAYOUTS[value];

        layoutLabel.innerHTML = 'Layout' + (title ? (': ' + title) : '');
        layoutDropdown.value = value;

        document.body.setAttribute('data-speaker-layout', value);

        // Persist locally
        if (supportsLocalStorage()) {
            window.localStorage.setItem('reveal-speaker-layout', value);
        }

    }

    /**
     * Returns the ID of the most recently set speaker layout
     * or our default layout if none has been set.
     */
    function getLayout() {

        if (supportsLocalStorage()) {
            var layout = window.localStorage.getItem('reveal-speaker-layout');
            if (layout) {
                return layout;
            }
        }

        // Default to the first record in the layouts hash
        for (var id in SPEAKER_LAYOUTS) {
            return id;
        }

    }

    function supportsLocalStorage() {

        try {
            localStorage.setItem('test', 'test');
            localStorage.removeItem('test');
            return true;
        }
        catch (e) {
            return false;
        }

    }

    function zeroPadInteger(num) {

        var str = '00' + parseInt(num);
        return str.substring(str.length - 2);

    }

    /**
     * Limits the frequency at which a function can be called.
     */
    function debounce(fn, ms) {

        var lastTime = 0,
            timeout;

        return function () {

            var args = arguments;
            var context = this;

            clearTimeout(timeout);

            var timeSinceLastCall = Date.now() - lastTime;
            if (timeSinceLastCall > ms) {
                fn.apply(context, args);
                lastTime = Date.now();
            }
            else {
                timeout = setTimeout(function () {
                    fn.apply(context, args);
                    lastTime = Date.now();
                }, ms - timeSinceLastCall);
            }

        }

    }

    /*
     * Sets up <pre> tags in speaker notes for copying.
     */
    function setupNoteCopyEvents() {
        var pre_elems = notesValue.querySelectorAll("pre");
        pre_elems.forEach(
            function (pre) {
                pre.addEventListener("click", copyToClipboard, true)

                let tooltip_instruction = document.createElement("div");
                tooltip_instruction.classList.add("tooltip");
                tooltip_instruction.innerText = "📋 Click text box above to copy to clipboard";

                let tooltip_success = document.createElement("div");
                tooltip_success.classList.add("tooltip");
                tooltip_success.innerText = "✅ Copied!";

                pre.after(tooltip_instruction, tooltip_success);
            }
        );
    }

    /*
     * Copies elements text to the system clipboard.
     * New function added by UCCSER
     */
    function copyToClipboard(event) {
        let pre = event.target;
        // Copy text
        var text = pre.innerText;
        navigator.clipboard.writeText(text);
        // Remove highlight
        document.getSelection().removeAllRanges();
        // Update tooltips
        var hidden_tooltips = notesValue.querySelectorAll(".tooltip-hide");
        hidden_tooltips.forEach( function(tooltip) {
            tooltip.classList.remove("tooltip-hide");
        });
        pre.nextSibling.classList.add("tooltip-hide");
    }
})();
