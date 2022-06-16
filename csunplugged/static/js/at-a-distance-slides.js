const Reveal = require('reveal.js');
// import Markdown from 'reveal.js/plugin/markdown/markdown.esm.js';

let deck = new Reveal({
    // The "normal" size of the presentation, aspect ratio will
    // be preserved when the presentation is scaled to fit different
    // resolutions. Can be specified using percentage units.
    width: 1920,
    height: 1080,

    // Factor of the display size that should remain empty around
    // the content
    margin: 0.04,

    // Bounds for smallest/largest possible scale to apply to content
    minScale: 0.1,
    maxScale: 2.0,

    embedded: true,
    transition: 'slide',
})
deck.initialize();
