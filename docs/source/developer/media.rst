Media
##############################################################################

.. warning::

  The documentation for this page is still being written.

  This page will cover:

  - Animations
    - GIF conversion using the SWF > MP4 > GIF conversion pipeline
  - Images
  - Video

Animations
==============================================================================

Animations are located in the ``csunplugged/static/img`` directory.

Animations are currently created by creating the elements using Adobe Illustrator and then animated on Adobe Animate.
The frame rate used is normally 30fps, but this does not need to be strictly followed.
The animations are then exported in a .gif format.

The SWF > MP4 > GIF Pipeline
------------------------------------------------------------------------------
Sometimes, exporting as a .gif file will not work on Adobe Animate (exports with incorrect colours, or incomplete animations).
In this case, the animation must follow the rather convuluted SWF > MP4 > GIF pipeline.

1. The animation is exported in a .swf format in Adobe Animate.
2. The animation is converted to a .mp4 file using a conversion tool, such as `Swivel <https://www.newgrounds.com/wiki/creator-resources/flash-resources/swivel>`_.
3. The animation is converted to a .gif file using a conversion tool, such as `ezgif <https://ezgif.com/video-to-gif>`_.
