# Custom reveal.js speaker notes plugin

A modified version of the reveal.js speaker notes plugin.

- https://github.com/hakimel/reveal.js
- https://github.com/hakimel/reveal.js/tree/master/plugin/notes

The source repository is licensed under the MIT license.

The original license is available within this directory, and also in `third-party-licences/revealjs.txt`.

A big thank you to Hakim El Hattab for making such a great framework.

## Changes from original

- HTML for speaker view is served at a specific URL by Django.
  This allows us to easier edit and link files to the HTML.
- JavaScript for the speaker view has been moved to its own file for easier editing.
- CSS for the speaker view has been moved to its own file for easier editing and been converted to SCSS.

## Files related to plugin

```
csunplugged/
    static/
        js/
            reveal-speaker-notes-plugin/
                LICENSE
                README.md
                reveal-plugin.js
                speaker-notes-window.js
        scss/
            reveal-speaker-notes-plugin/
                speaker-notes-window.scss
    templates/
        at_a_distance/
            reveal-speaker-notes-plugin/
                speaker-notes-window.html
third-party-licences/
    revealjs.txt
```

Logic for serving speaker notes view is found within the `at_a_distance` application (in particular the `views.py` and `urls.py` files.
Some SCSS partials are imported for consistency with the custom theme used.
