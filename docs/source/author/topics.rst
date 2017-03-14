Topics application
##############################################################################

The topics application is the main focus of the CS Unplugged website, as it
contains the majority of educational material for the project.

.. contents:: Contents
  :local:

Topics overview
==============================================================================

A general overview of the topics application can be described in the following
diagram.

.. The following image can copied for be edits here: https://goo.gl/ZkQsLW
.. image:: ../_static/img/topics_overview_diagram.svg
  :alt: A diagram providing an overview of topics application content

- The application is made up of **topics** (for example: binary numbers)

  - This can contain a **unit plan** with **lessons**.
    A topic can actually contain several **unit plans** if required, each with
    their own lessons.

    - Each lesson can have connected **learning outcomes**,
      **curriculum links**, and **generated resources**.

  - Topics can also contain **follow up activities**, which can also contain
    **curriculum links**.

  - Topics can also contain **programming exercises**.

    - A programming exercise can have **language implementations**, which contain
      language specific expected values, hints, and possible solutions.
      For example: an exercise may have implementations available in Scratch and
      Python.

- **Learning outcomes** and **curriculum links** are defined at a language
  level, so can be used by all topic content.

- Also defined at the language level is **languages** and **difficulties** for
  programming exercises.

This is just a broad overview of the topics application.

.. _topics-directory-structure:

Topics content directory
==============================================================================

The diagram below is an example of the ``content/en/`` language directory for
the project's topic application, where:

- Blue is directories.
- Red is YAML configuration files (see :doc:`understanding_configuration_files`).
- Green is Markdown text files.

.. include:: ../_static/html_snippets/topics_content_directory_tree.rst

.. _adding-topics-content:

Adding content
==============================================================================

The following flow charts will take you step by step through the process of
adding new content to the topics application.

.. _adding-topics-content-topic:

Adding a topic
------------------------------------------------------------------------------

You can add a new topic by following this flowchart.

.. The following image can copied for be edits here: https://goo.gl/Vjv6XV
.. The image is included as raw HTML because it has clickable nodes.
.. raw:: html

  <map name="topics-map">
    <area shape="rect" coords="215,90,317,127" href="#topics-content-directory">
    <area shape="rect" coords="215,200,317,234" href="#topic-file">
    <area shape="rect" coords="215,307,317,343" href="#application-structure-file">
    <area shape="rect" coords="215,425,317,460" href="../getting_started/basic_usage.html#command-manage-loaddata">
    <area shape="rect" coords="215,541,317,576" href="../getting_started/basic_usage.html#command-manage-runserver">
    <area shape="rect" coords="215,658,317,694" href="../getting_started/basic_usage.html#command-gulp">
  </map>
  <img src="../_static/img/topics_adding_topic_flowchart.png" usemap="#topics-map">

After you have added a topic, you can then add unit plans, lessons, follow
up activities, and programming exercises using the flow charts below.

.. _adding-topics-content-unit-plan:

Adding a unit plan and/or lesson
------------------------------------------------------------------------------

You can add a new unit plan and/or lesson by following this flowchart.
If a lesson requires new learning outcomes or curriculum links, see
:ref:`adding-topics-content-learning-outcomes-curriculum-links`.

.. The following image can copied for be edits here: https://goo.gl/Vjv6XV
.. The image is included as raw HTML because it has clickable nodes.
.. raw:: html

  <map name="unit-plan-map">
    <area shape="rect" coords="215,90,317,127" href="#topics-content-directory">
    <area shape="rect" coords="284,330,387,364" href="#topics-content-directory">
    <area shape="rect" coords="284,570,387,605" href="#unit-plan-file">
    <area shape="rect" coords="284,684,387,719" href="#topic-file">
    <area shape="rect" coords="284,930,387,965" href="#topics-content-directory">
    <area shape="rect" coords="284,1172,387,1206" href="#unit-plan-file">
    <area shape="rect" coords="284,1294,387,1329" href="#unit-plan-file">
    <area shape="rect" coords="229,1471,333,1504" href="../getting_started/basic_usage.html#command-manage-loaddata">
    <area shape="rect" coords="229,1589,333,1622" href="../getting_started/basic_usage.html#command-manage-runserver">
    <area shape="rect" coords="229,1704,333,1738" href="../getting_started/basic_usage.html#command-gulp">
  </map>
  <img src="../_static/img/topics_adding_unit_plan_flowchart.png" usemap="#unit-plan-map">

.. _adding-topics-content-follow-up-activity:

Adding a follow up activity
------------------------------------------------------------------------------

You can add a new follow up activity by following this flowchart.
If a follow up activity requires new curriculum links, see
:ref:`adding-topics-content-learning-outcomes-curriculum-links`.

.. The following image can copied for be edits here: https://goo.gl/Vjv6XV
.. The image is included as raw HTML because it has clickable nodes.
.. raw:: html

  <map name="follow-up-activities-map">
  <area shape="rect" coords="217,90,319,127" href="#topics-content-directory">
  <area shape="rect" coords="283,459,387,494" href="#topics-content-directory">
  <area shape="rect" coords="283,571,387,607" href="#follow-up-activities-file">
  <area shape="rect" coords="283,688,387,723" href="#topic-file">
  <area shape="rect" coords="283,939,387,973" href="#follow-up-activities-file">
  <area shape="rect" coords="216,1088,319,1124" href="../getting_started/basic_usage.html#command-manage-loaddata">
  <area shape="rect" coords="216,1206,319,1240" href="../getting_started/basic_usage.html#command-manage-runserver">
  <area shape="rect" coords="216,1325,319,1358" href="../getting_started/basic_usage.html#command-gulp">
  </map>
  <img src="../_static/img/topics_adding_follow_up_activities_flowchart.png" usemap="#follow-up-activities-map">

.. _adding-topics-content-programming-exercise:

Adding a programming exercise
------------------------------------------------------------------------------

You can add a new programming exercise by following this flowchart.
If a programming exercise requires new learning outcomes, see
:ref:`adding-topics-content-learning-outcomes-curriculum-links`.

.. The following image can copied for be edits here: https://goo.gl/Vjv6XV
.. The image is included as raw HTML because it has clickable nodes.
.. raw:: html

  <map name="programming-exercise-map">
    <area shape="rect" coords="215,90,320,126" href="#topics-content-directory">
    <area shape="rect" coords="284,460,387,494" href="#topics-content-directory">
    <area shape="rect" coords="284,571,387,607" href="#programming-exercises-file">
    <area shape="rect" coords="284,684,387,719" href="#topic-file">
    <area shape="rect" coords="284,805,387,841" href="#topics-content-directory">
    <area shape="rect" coords="284,1074,387,1110" href="#programming-exercises-file">
    <area shape="rect" coords="349,1542,452,1578" href="#programming-exercises-file">
    <area shape="rect" coords="216,1709,319,1744" href="../getting_started/basic_usage.html#command-manage-loaddata">
    <area shape="rect" coords="216,1826,319,1860" href="../getting_started/basic_usage.html#command-manage-runserver">
    <area shape="rect" coords="216,1943,319,1977" href="../getting_started/basic_usage.html#command-gulp">
  </map>
  <img src="../_static/img/topics_adding_programming_exercises_flowchart.png" usemap="#programming-exercise-map">

.. _adding-topics-content-learning-outcomes-curriculum-links:

Adding learning outcomes and/or curriculum links
------------------------------------------------------------------------------

You can add a new programming exercise by following this flowchart.

.. The following image can copied for be edits here: https://goo.gl/Vjv6XV
.. The image is included as raw HTML because it has clickable nodes.
.. raw:: html

  <map name="learning-outcomes-curriculum-links-map">
    <area shape="rect" coords="215,90,320,126" href="#topics-content-directory">
    <area shape="rect" coords="281,342,387,377" href="#learning-outcomes-file">
    <area shape="rect" coords="281,616,387,652" href="#curriculum-links-file">
  </map>
  <img src="../_static/img/topics_adding_learning_outcomes_curriculum_links_flowchart.png" usemap="#learning-outcomes-curriculum-links-map">

Configuration Files
==============================================================================

This section details configuration files within the ``content`` directory for a
specific language.
These files define the topics content on the website and their respective
attributes (for example: the difficulty of a programming exercise).
If you haven't used the YAML configuration files before, see
:doc:`understanding_configuration_files`.

The diagram below shows an example of YAML file locations for the
``content/en/`` language directory, where:

- Blue is directories.
- Red is YAML configuration files.

.. include:: ../_static/html_snippets/topics_content_directory_tree_only_yaml.rst

.. _application-structure-file:

Application Structure File
------------------------------------------------------------------------------

This file defines the top level configuration files to process for defining
the content of the topics application.

The location of this file is within a language file, and it must be named:
``structure.yaml``

This file must contain the following key/value pairs:

.. code-block:: yaml

  # Learning outcomes for all topics
  learning-outcomes: learning-outcomes.yaml

  # Curriculum links for all topics
  curriculum-links: curriculum-links.yaml

  # Defines languages and difficulty levels for all programming exercises
  programming-exercises-structure: programming-exercises-structure.yaml

  # Lists all topics to include in CS Unplugged project
  # The order of topics here defines their order on the website
  topic-structure-files:
    - binary-numbers/binary-numbers.yaml
    - error-detection-correction/error-detection-correction.yaml

.. _topic-file:

Topic File
------------------------------------------------------------------------------

This file defines the attributes of a specific topic, including connected
unit plan, programming exercise, and follow up activity configuration files.

The location of this file is within a topic directory.
This file is listed in the :ref:`application-structure-file`.

This file must contain the following key/value pairs:

.. code-block:: yaml

  # The URL slug for the topic
  slug: binary-numbers

  # The Markdown file containing the description of the topic
  # This is essentially the text for the webpage for the topic
  # The file path is relative to this YAML file
  md-file: index.md

  # An image icon used for the topic within the static directory
  # The path is from the top of the static directory
  icon: img/binary-numbers-0-1.png

.. note::

  The name of the topic is retrieved from the first header in the
  ``md-file``.

The file may also contain any of the following optional key/value pairs:

.. code-block:: yaml

  # A list of unit plan configuaration files for this topic
  # The order here defines their order on the website
  # The file paths are relative to this YAML file
  unit-plans:
    - unit-plan/unit-plan.yaml

  # A configuaration file defining programming exercises for the topic
  # The file path is relative to this YAML file
  programming-exercises: programming-exercises/programming-exercises.yaml

  # A configuaration file defining follow up activities for the topic
  # The file path is relative to this YAML file
  follow-up-activities: follow-up-activities/follow-up-activities.yaml

  # A Markdown file describing other resources
  # The file path is relative to this YAML file
  other-resources-md-file: other-resources.md

.. _unit-plan-file:

Unit Plan File
------------------------------------------------------------------------------

This file defines the attributes of a unit plan, including all lessons (and
their respective attributes) for the unit plan.

The location of this file is within a unit plan directory.
These files are listed in a :ref:`topic-file`.

This file must contain the following key/value pairs:

.. code-block:: yaml

  # The URL slug for the unit plan
  # We recommend using 'unit-plan' for the first unit-plan for each topic
  slug: unit-plan

  # The Markdown file containing the description of the unit plan
  # This is essentially the text for the webpage for the unit plan
  # The file path is relative to this YAML file
  md-file: unit-plan.md

  # Key containing all lesson data
  lessons:
    # The URL slug of the lesson
    # We don't recommend using numbered slugs as ordering may change but
    # slug should be consistent.
    lesson-1:
      # The minimum age this lesson is suitable for
      minimum-age: 5
      # The maximum age this lesson is suitable for
      maximum-age: 7
      # The number order for this lesson
      # Lessons are sorted by minimum age, maximum age, then number
      # so lessons in different age ranges can use the same number
      # without conflict.
      number: 1

      # The Markdown file containing the description of the lesson
      # This is essentially the text for the webpage for the lesson
      # The file path is relative to this YAML file
      md-file: lessons/5-7/lesson-1.md

Lessons may also contain any of the following key/value pairs (same
indentation as ``minimum-age``, ``maximum-age``, ``number``, etc):

.. code-block:: yaml

  # The Markdown file containing the content for the handout of the lesson
  # This is essentially the text for the webpage for the handout
  # The file path is relative to this YAML file
  handout: lessons/5-7/lesson-1-handout.md

  # The slugs for the learning outcomes for this lesson
  learning-outcomes:
    - binary-data-representation
    - binary-count
    - binary-convert-decimal
    - binary-justify-representation

  # The slugs for the curriculum links for this lesson
  curriculum-links:
    - maths

  # A list of Markdown text of classroom resources required for this lesson
  resources-classroom:
    - Pens
    - String

  # A list of resources generated by CS Unplugged system
  # Each resource listed requires the following two keys:
  #   slug: The slug of the resource in the resources app
  #   description: Markdown text describing the use of the resource
  resources-generated:
    - slug: sorting-network
      description: One copy per student
    - slug: treasure-hunt
      description: One copy per student

.. note::

  The name of the unit plan is retrieved from the first header in the
  ``md-file``.

  The name of lessons are retrieved from the first header in their
  ``md-file``.

An example unit plan configuaration file with multiple lessons may look like
the following:

.. code-block:: yaml

  slug: unit-plan
  md-file: unit-plan.md
  lessons:
    lesson-1:
      minimum-age: 5
      maximum-age: 7
      number: 1
      md-file: lessons/5-7/lesson-1.md
      handout: lessons/5-7/lesson-1-handout.md
      learning-outcomes:
        - binary-data-representation
        - binary-count
        - binary-convert-decimal
        - binary-justify-representation
      curriculum-links:
        - maths
      resources-classroom:
        - Pens
        - String
      resources-generated:
        - slug: sorting-network
          description: One copy per student
        - slug: sorting-network
          description: One copy per student

    lesson-2:
      minimum-age: 5
      maximum-age: 7
      number: 2
      md-file: lessons/5-7/lesson-2.md
      handout: lessons/5-7/lesson-2-handout.md
      learning-outcomes:
        - binary-data-representation
        - binary-count
      curriculum-links:
        - maths
        - science
      resources-classroom:
        - Pens

    lesson-3:
      minimum-age: 5
      maximum-age: 7
      number: 3
      md-file: lessons/5-7/lesson-3.md
      handout: lessons/5-7/lesson-3-handout.md
      learning-outcomes:
        - binary-convert-decimal
        - binary-justify-representation
      curriculum-links:
        - maths
        - art

.. _follow-up-activities-file:

Follow Up Activities File
------------------------------------------------------------------------------

This file defines the follow up activities for a topic (and their respective
attributes).

The location of this file is within a topic directory.
This configuaration file is listed in a :ref:`topic-file`.
It is also valid to have no configuaration file if there are no follow up
activities for a topic.

This file can contain as many follow up activities as you like, as long as
each activity has a unique slug URL within the topic.

The file should have the following key/value pair structure:

.. code-block:: yaml

  # The URL slug for the follow up activity
  painting-parity:
    # This number is used for ordering follow up activities
    number: 1

    # The Markdown file containing the description of the activity
    # This is essentially the text for the webpage for the activity
    # The file path is relative to this YAML file
    md-file: painting-parity.md

    # The slugs for the curriculum links for this activity
    curriculum-links:
      - arts

An example follow up activities configuaration file with multiple activities
may look like the following:

.. code-block:: yaml

  binary-number-bracelets:
    number: 1
    md-file: bracelets.md
    curriculum-links:
      - arts
      - design

  hidden-binary-signals:
    number: 2
    md-file: hidden-binary-signals.md
    curriculum-links:
      - science

.. note::

  The name of follow up activites are retrieved from the first header in the
  ``md-file`` for each activity.

.. _programming-exercises-structure-file:

Programming Exercises Structure File
------------------------------------------------------------------------------

This file defines the structure of programming exercises for all topics.
The two components it defines is available language for exercise
implementations, and difficulties of exercises.

The location of this file is within the language directory.
This configuaration file is listed in a :ref:`application-structure-file`.
This file can contain as many languages and difficulties as you like.

The file should have the following key/value pair structure:

.. code-block:: yaml

  # Available languages for implementations of programming execises
  languages:
    # The slug of the language implementation
    scratch:
      # The name of the language implementation
      name: Scratch
      # An image icon used for the topic within the static directory
      # The path is from the top of the static directory
      icon: img/scratch-cat.png
    python:
      name: Python
      icon: img/python-logo.png
    cplusplus:
      name: C++
      icon: img/cplusplus-logo.png

  # Available difficulties for programming execises
  # The difficulties are stored in a list for easier reading but will
  # be displayed by sorting the level attribute from smallest to largest.
  difficulties:
      # A difficulty has a level attribute as a number (smaller = easier)
    - level: 1
      # A difficult level has a name for displaying the level
      name: Beginner
    - level: 2
      name: Growing Experience
    - level: 3
      name: Ready to Expand

.. _programming-exercises-file:

Programming Exercises File
------------------------------------------------------------------------------

This file defines the programming exercises for a particular topic, including
their respective attributes.

The location of this file is within a programming exercises directory.
This file is listed in a :ref:`topic-file`.

The file should have the following key/value pair structure:

.. code-block:: yaml

  # The URL slug for the unit plan
  count-to-16:
    # The number of the exercise
    number: 1
    # The number for difficulty level for this exercise
    difficulty-level: 1
    # Activities are usually displayed in difficuly, then number order

    # The Markdown file containing the description of the exercise
    # This is essentially the text for the webpage for the exercise
    # The file path is relative to this YAML file
    md-file: exercise-1.1/index.md

    # The slugs for the learning outcomes for this lesson
    learning-outcomes:
      - programming-sequence
      - programming-one-input-output

    # The programming implementations for this exercise
    programming-languages:
      # The slug for the programming language
      scratch:
        # The Markdown file containing the hints for this programming language
        # implementation of this exercise
        # The file path is relative to this YAML file
        hints: exercise-1.1/scratch-hints.md
        # The Markdown file containing the solution for this programming
        # language implementation of this exercise
        # The file path is relative to this YAML file
        solution: exercise-1.1/scratch-solution.md

.. note::

  The name of programming exercises are retrieved from the first header in the
  ``md-file`` for each exercise.

.. code-block:: yaml

  count-to-16:
    number: 1
    difficulty-level: 1
    md-file: exercise-1.1/index.md
    learning-outcomes:
      - programming-sequence
      - programming-one-input-output
    programming-languages:
      scratch:
        hints: exercise-1.1/scratch-hints.md
        solution: exercise-1.1/scratch-solution.md
      python:
        hints: exercise-1.1/python-hints.md
        solution: exercise-1.1/python-solution.md

  count-to-a-million:
    number: 2
    difficulty-level: 3
    md-file: exercise-2/index.md
    learning-outcomes:
      - programming-basic-logic
    programming-languages:
      scratch:
        hints: exercise-2/scratch-hints.md
        solution: exercise-2/scratch-solution.md
      python:
        hints: exercise-2/python-hints.md
        solution: exercise-2/python-solution.md

.. _learning-outcomes-file:

Learning Outcomes File
------------------------------------------------------------------------------

This file defines the learning outcomes avilable for all topics.

The location of this file is within the language directory.
This file is listed in a :ref:`application-structure-file`.
This file can contain as many learning outcomes as you like.

The file should only contain pairs of outcome slug to outcome text pairs.
For example:

.. code-block:: yaml

  binary-data-representation: Explain how a binary digit is represented using two contrasting values.
  binary-count: Demonstrate how to represent any number between 0 and 31 using binary.
  binary-convert-decimal: Perform a demonstration of how the binary number system works by converting any decimal number into a binary number.
  binary-justify-representation: Argue that 0’s and 1’s are still a correct way to represent what is stored in the computer.

.. note::

  Lessons and programming exercises link to learning outcomes by listing
  their slug.

.. _curriculum-links-file:

Curriculum Links File
------------------------------------------------------------------------------

This file defines the curriculum links avilable for all topics.

The location of this file is within the language directory.
This file is listed in a :ref:`application-structure-file`.
This file can contain as many curriculum links as you like.

The file should have the following key/value pairs:

.. code-block:: yaml

  # The URL slug for the curriculum link
  maths:
    # The display name for the curriculum
    name: maths

.. note::

  Lessons and follow up activities link to curriculums by listing their
  slug.

An example curriculum links file with multiple curriculums may look like
the following:

.. code-block:: yaml

  maths:
    name: Maths

  science:
    name: Science

  art:
    name: Art
