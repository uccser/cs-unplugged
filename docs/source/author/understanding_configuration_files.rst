Understanding configuration files
##############################################################################

There is a lot of content within the CS Unplugged project.
We split this content across many files and configuration files are the things
that bring everything together.
Understanding how to read and write these configuration files is important
for working on this project, because these files are used for configuring the
content data when stored in the system database.

This page aims to give a brief tutorial on YAML files, so you can modify
configuration files within this project.

Here is an example YAML file:

.. code-block:: yaml

  learning-outcomes: learning-outcomes.yaml
  programming-exercises-structure: programming-exercises-structure.yaml

  topic-structure-files:
    - binary-numbers/structure.yaml
    - error-detection-and-correction/structure.yaml

YAML files are mostly made up of key/value pairs, often called a dictionary
within programming languages.
This configuration file contains the follow three key/value pairs:

- The key ``learning-outcomes`` points to the file
  ``learning-outcomes.yaml``
- The key ``programming-exercises-structure`` points to the file
  ``programming-exercises-structure.yaml``
- The key ``topic-structure-files`` points to the ordered list of files
  ``binary-numbers/structure.yaml`` and
  ``error-detection-and-correction/structure.yaml``

The majority of configuration files within this project only use dictionaries
and lists to store their data.
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

We try to avoid deep nesting (indentation) within configuration files as it's
hard to read nested data.
We have split configuration data across multiple configuration files to avoid
this issue.

If you want to learn more about YAML, there are plenty of great tutorials
available on the internet.
