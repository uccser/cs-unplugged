Understanding Configuration Files
##############################################################################

There is a lot of content within the CS Unplugged project.
We split this content across many files and configuration files are the things
that bring everything together.
These files are used for configuring the content data stored in the
system database, so it is important to understand how to read and write these
configuration files if you are working on this project.

Here is an example configuration file used to define follow up activities
in the CS Unplugged project:

.. code-block:: yaml

  binary-number-bracelets:
    number: 1
    md-file: bracelets.md
    curriculum-areas:
      - arts
      - design

  hidden-binary-signals:
    number: 2
    md-file: hidden-binary-signals.md
    curriculum-areas:
      - listening

This page aims to give a brief tutorial on YAML files, so you can modify and write
configuration files within this project.

YAML files are mostly made up of key/value pairs, where each key is matched with
one value.
This is often called a dictionary in programming languages.
This configuration file contains the follow three key/value pairs:

- The key ``learning-outcomes`` points to the file
  ``learning-outcomes.yaml``
- The key ``programming-challenges-structure`` points to the file
  ``programming-challenges-structure.yaml``
- The key ``topic-structure-files`` points to the ordered list of files
  ``binary-numbers/structure.yaml`` and
  ``error-detection-and-correction/structure.yaml``

The majority of configuration files within this project only use dictionaries
(sets of key/value pairs) and lists to store their data.
Here are some other useful tips:

.. code-block:: yaml

  # You can include comments in YAML by starting with a # character

  # This stores the integer 7 in the key 'number'
  number: 7

  # This is an ordered list of dictionaries within the key 'difficulties'
  difficulties:
    - level: 1
      name: Beginner
    - level: 2
      name: Growing Experience
    - level: 3
      name: Ready to Expand

You may find that there is more than one configuration file that you need to
modify/create.
This is because it is difficult to read files using deep nesting
(indentation), so we have split configuration data across multiple files to
avoid this issue.

If you want to learn more about YAML, there are plenty of great tutorials
available online.
