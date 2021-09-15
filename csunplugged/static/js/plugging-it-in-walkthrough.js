const introJS = require('intro.js');

$(document).ready(function () {

    var intro = introJS();

    if (programming_lang === 'python') {
        intro.setOptions({
            showStepNumbers: false,
            steps: [
                {
                    element: ".programming__info-area-content",
                    intro: "These are the requirements for the program you need to create - it describes what your program should do.",
                    step: 1,
                    position: "right"
                },
                {
                    element: ".CodeMirror",
                    intro: "This is where you type your code to solve the challenge.",
                    step: 2
                },
                {
                    element: "#editor_check_button",
                    intro: "Clicking the 'Check' button will run your code to see if it works correctly for our test cases.",
                    step: 3
                },
                {
                    element: "#download_button",
                    intro: "Clicking the 'Download' button will download the program you have written to your computer.",
                    step: 4
                },
                {
                    element: "#test-case-table",
                    intro: "These are the test cases that will be used to see if your program is working correctly.",
                    step: 5
                },
                {
                    element: "#test-case-table tbody tr:nth-child(1)",
                    intro: "Here is the first test case.",
                    step: 6
                },
                {
                    element: "#test-case-table tbody tr:nth-child(1) td:nth-child(1)",
                    intro: "This is the input that will be passed to your program for this particular test. \
                    If this is blank, it means no input will be passed to your program.",
                    step: 7
                },
                {
                    element: "#test-case-table tbody tr:nth-child(1) td:nth-child(2)",
                    intro: "This is the output that the test expects your program to print for the given input.",
                    step: 8
                },
                {
                    element: "#test-case-table tbody tr:nth-child(1) td:nth-child(3)",
                    intro: "This is where your program will print its output. This is compared against the expected output.",
                    step: 9
                },
                {
                    element: "#test-case-table tbody tr:nth-child(1) td:nth-child(4)",
                    intro: "A test case will pass if the received output matches the expected output. If all test cases pass the question has been solved.",
                    step: 10
                },
                {
                    element: "#next_challenge_button button",
                    intro: "Click this button when you are ready to move on to the next challenge.",
                    step: 11,
                    position: "top"
                },
                {
                    element: "#lessons_nav_toggle",
                    intro: "Click here to see the other challenges for this topic.",
                    step: 12
                },
                {
                    element: ".navbar-brand",
                    intro: "Click here to see the other topics available.",
                    step: 13
                },
            ].filter(function (obj) {
                style = $(obj.element).attr('style');
                return style == undefined || !style.includes('display: none')
            })
        });
    } else {
        intro.setOptions({
            showStepNumbers: false,
            steps: [
                {
                    element: ".programming__info-area-content",
                    intro: "These are the requirements for the program you need to create - it describes what your program should do.",
                    step: 1,
                    position: "right"
                },
                {
                    element: "#blocklyDiv",
                    intro: "This is where you create your program to solve the challenge.",
                    step: 2
                },
                {
                    element: "#blockly_editor_run_program_button",
                    intro: "Clicking the 'Run' button will run the program you have created without submitting it.",
                    step: 3
                },
                {
                    element: "#editor_check_button",
                    intro: "Clicking the 'Submit' button will submit your program to see if it works correctly for our test cases.",
                    step: 4
                },
                {
                    element: "#test-case-table",
                    intro: "These are the test cases that will be used to see if your program is working correctly.",
                    step: 5
                },
                {
                    element: "#test-case-table tbody tr:nth-child(1)",
                    intro: "Here is the first test case.",
                    step: 6
                },
                {
                    element: "#test-case-table tbody tr:nth-child(1) td:nth-child(1)",
                    intro: "This is the input that will be passed to your program for this particular test. \
                    If this is blank, it means no input will be passed to your program.",
                    step: 7
                },
                {
                    element: "#test-case-table tbody tr:nth-child(1) td:nth-child(2)",
                    intro: "This is the output that the test expects your program to print for the given input.",
                    step: 8
                },
                {
                    element: "#test-case-table tbody tr:nth-child(1) td:nth-child(3)",
                    intro: "This is where your program will print its output. This is compared against the expected output.",
                    step: 9
                },
                {
                    element: "#test-case-table tbody tr:nth-child(1) td:nth-child(4)",
                    intro: "A test case will pass if the received output matches the expected output. If all test cases pass the question has been solved.",
                    step: 10
                },
                {
                    element: ".block-based-console",
                    intro: "This is where the output of your program will get displayed when you click the 'Run' button.",
                    step: 11,
                    position: "bottom"
                },
                {
                    element: "#next_challenge_button button",
                    intro: "Click this button when you are ready to move on to the next challenge.",
                    step: 12,
                    position: "top"
                },
                {
                    element: "#lessons_nav_toggle",
                    intro: "Click here to see the other challenges for this topic.",
                    step: 13
                },
                {
                    element: ".navbar-brand",
                    intro: "Click here to see the other topics available.",
                    step: 14
                },
            ].filter(function (obj) {
                style = $(obj.element).attr('style');
                return style == undefined || !style.includes('display: none')
            })
        });
    }

    $("#introjs-walkthrough").click(function() {
        intro.start().onbeforechange(function() {
            currentElement = $(this._introItems[this._currentStep].element);
            node = currentElement.prop('nodeName');
            // When looking at a full row of the table, force it to scroll to the far left
            // so the highlight only overhangs to the right
            if (node == 'TABLE' || node == 'TR') {
                currentElement = currentElement.find('td:first-of-type')
            }
            containerId = 'test-case-table-container';
            scroll_to_element(containerId, currentElement);
        });
    });
});


function scroll_to_element(containerId, element) {
    // For use by the tutorials
    var container = $('#' + containerId);
    var contWidth = container.width();
    var contLeft = container.offset().left;
    var elemLeft = $(element).offset().left - contLeft; // wrt container
    var elemWidth = element.width();
    var isInView = elemLeft >= 0 && (elemLeft + elemWidth) <= contWidth;

    if (!isInView) {
        container.scrollLeft(0);
        var scrollTo = $(element).offset().left - contLeft;
        container.scrollLeft(scrollTo);
    }
}
