Troubleshooting
##############################################################################

Viewing website
==============================================================================

Images are not displayed when I view the website
******************************************************************************

Firstly check the image is located in the ``build`` folder.
If the image isn't located within the folder, check the Gulp script is
running and hasn't reported any errors.

**Normal Images (not Scratch block images)**

If the image is located within the ``build`` folder, check the complete
filepath is correct.

**Scratch block images**

Check the ``.txt`` files located within the ``temp`` folder for a file
containing the Scratch block syntax for the image missing (project wide
find & replace is your friend here).

If you can find the file with the same block syntax and there isn't a image
in the ``build`` folder with the same filename (``.svg`` instead of ``.txt``),
try stopping and restarting the Gulp script.
If this doesn't fix the problem, the problem is in our Gulp script so log a
bug on our `issue tracker`_.

If you can't find a file within the ``temp`` folder, check the syntax used in
the text is valid.
If the syntax is valid, the problem is in our Markdown to HTML converter to
log a bug on our `issue tracker`_.

Changed CSS/SCSS styles are not updated when I view the website
******************************************************************************

Firstly check the compiled CSS is located in the ``build`` folder, and that
the changes have appeared in the compiled CSS file.
If the CSS file does not include the changes made, check the Gulp script is
running.
If you are editing SCSS files, check the Gulp script isn't reporting SCSS
compilation errors.

The website isn't displaying when I open ``localhost:8000`` or ``127.0.0.1:8000``
*********************************************************************************

Check you have a terminal running the ``python manage.py runserver`` command,
and that it hasn't reported any errors.

The website isn't displaying when I open ``localhost:3000`` or ``127.0.0.1:3000``
*********************************************************************************

Firsty check you have a terminal running the ``gulp`` command, and that it
hasn't reported any errors.

Then check you have a terminal running the ``python manage.py runserver``
command, and that it hasn't reported any errors.

.. _issue tracker: https://github.com/uccser/cs-unplugged/issues
