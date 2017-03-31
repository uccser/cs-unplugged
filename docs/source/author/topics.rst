Topic Content
##############################################################################

The topics application (see :ref:`what-is-an-application`) is the main focus of the CS Unplugged website, as it
contains the majority of educational material for the project.

.. contents:: Contents
  :local:

Topics Overview
==============================================================================

A general overview of the topics application can be described in the following
diagram.

.. The following image can copied for be edits here: https://goo.gl/Vjv6XV
.. image:: ../_static/img/topics_overview_diagram.png
  :alt: A diagram providing an overview of topics application content

- The application is made up of **topics** (for example: binary numbers)

  - This can contain a **unit plan** with **lessons**.
    A topic can actually contain several **unit plans** if required, each with
    their own lessons.

    - Each lesson can have connected **learning outcomes**,
      **curriculum areas**, and **generated resources**.

  - Topics can also contain **follow up activities**, which can also contain
    **curriculum areas**.

  - Topics can also contain **programming exercises**.

    - A programming exercise can have **language implementations**, which contain
      language specific expected values, hints, and possible solutions.
      For example: an exercise may have implementations available in Scratch and
      Python.

- **Learning outcomes** and **curriculum areas** are defined at a language
  level, so can be used by all topic content.

- Also defined at the language level is **languages** and **difficulties** for
  programming exercises.

This is just a broad overview of the topics application.


.. _viewing-the-current-state:

Viewing the Current State
------------------------------------------------------------------------------

When developing locally, once you have a server and ``gulp`` runing (see
:doc:`../getting_started/basic_usage`) you can go to the url below to get a
quick overview of what content is loaded and how it
connects together:

.. code-block:: none

  localhost:3000/__dev__/

This page gives a high level overview of what is currently loaded into the database.
For more information about what this page displays, see :doc:`../developer/dev`.

.. _topics-directory-structure:

Topics Content Directory
==============================================================================

The diagram below is an example of the ``content/en/`` language directory for
the project's topic application, where:

- Blue is directories.
- Red is YAML configuration files (see :doc:`understanding_configuration_files`).
- Green is Markdown text files.

.. raw:: html
  :file: ../_static/html_snippets/topics_content_directory_tree.html

.. _adding-topics-content:

Adding Content
==============================================================================

The following flow charts will take you step by step through the process of
adding new content to the topics application, and you can click the 'Read more'
items on flowcharts to be taken to the relevant section in the documentation.
Below this section is full details on how to structure and write the
configuration files for the topics application.

.. _adding-topics-content-topic:

Adding a Topic
------------------------------------------------------------------------------

You can add a new topic by following this flowchart.

.. The following image can copied for be edits here: https://goo.gl/Vjv6XV
.. The image is included as raw HTML because it has clickable nodes.
.. raw:: html

  <map name="topics-map">
    <area shape="rect" coords="215,90,317,127" href="#topics-content-directory">
    <area shape="rect" coords="215,200,317,234" href="#topic-file">
    <area shape="rect" coords="215,307,317,343" href="#application-structure-file">
    <area shape="rect" coords="215,425,317,460" href="../getting_started/basic_usage.html#command-manage-updatedata">
    <area shape="rect" coords="215,541,317,576" href="../getting_started/basic_usage.html#command-manage-runserver">
    <area shape="rect" coords="215,658,317,694" href="../getting_started/basic_usage.html#command-gulp">
  </map>
  <img src="../_static/img/topics_adding_topic_flowchart.png" usemap="#topics-map">

After you have added a topic, you can then add unit plans, lessons, follow
up activities, and programming exercises using the flow charts below.

.. _adding-topics-content-unit-plan:

Adding a Unit Plan and/or Lesson
------------------------------------------------------------------------------

You can add a new unit plan and/or lesson by following this flowchart.
If a lesson requires new learning outcomes or curriculum areas, see
:ref:`adding-topics-content-learning-outcomes-curriculum-areas`.

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
    <area shape="rect" coords="229,1471,333,1504" href="../getting_started/basic_usage.html#command-manage-updatedata">
    <area shape="rect" coords="229,1589,333,1622" href="../getting_started/basic_usage.html#command-manage-runserver">
    <area shape="rect" coords="229,1704,333,1738" href="../getting_started/basic_usage.html#command-gulp">
  </map>
  <img src="../_static/img/topics_adding_unit_plan_flowchart.png" usemap="#unit-plan-map">

.. _adding-topics-content-curriculum-integrations:

Adding a Curriculum Integration
------------------------------------------------------------------------------

You can add a new curriculum integration by following this flowchart.
If a curriculum integration requires new curriculum areas, see
:ref:`adding-topics-content-learning-outcomes-curriculum-areas`.

.. The following image can copied for be edits here: https://goo.gl/Vjv6XV
.. The image is included as raw HTML because it has clickable nodes.
.. raw:: html

  <map name="curriculum-integrations-map">
  <area shape="rect" coords="217,90,319,127" href="#topics-content-directory">
  <area shape="rect" coords="283,459,387,494" href="#topics-content-directory">
  <area shape="rect" coords="283,571,387,607" href="#follow-up-activities-file">
  <area shape="rect" coords="283,688,387,723" href="#topic-file">
  <area shape="rect" coords="283,939,387,973" href="#follow-up-activities-file">
  <area shape="rect" coords="216,1088,319,1124" href="../getting_started/basic_usage.html#command-manage-updatedata">
  <area shape="rect" coords="216,1206,319,1240" href="../getting_started/basic_usage.html#command-manage-runserver">
  <area shape="rect" coords="216,1325,319,1358" href="../getting_started/basic_usage.html#command-gulp">
  </map>
  <img src="../_static/img/topics_adding_curriculum_integrations_flowchart.png" usemap="#curriculum-integrations-map">

.. _adding-topics-content-programming-exercise:

Adding a Programming Exercise
------------------------------------------------------------------------------

You can add a new programming exercise by following this flowchart.
If a programming exercise requires new learning outcomes, see
:ref:`adding-topics-content-learning-outcomes-curriculum-areas`.

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
    <area shape="rect" coords="216,1709,319,1744" href="../getting_started/basic_usage.html#command-manage-updatedata">
    <area shape="rect" coords="216,1826,319,1860" href="../getting_started/basic_usage.html#command-manage-runserver">
    <area shape="rect" coords="216,1943,319,1977" href="../getting_started/basic_usage.html#command-gulp">
  </map>
  <img src="../_static/img/topics_adding_programming_exercises_flowchart.png" usemap="#programming-exercise-map">

.. _adding-topics-content-learning-outcomes-curriculum-areas:

Adding Learning Outcomes and/or Curriculum Areas
------------------------------------------------------------------------------

You can add a new programming exercise by following this flowchart.

.. The following image can copied for be edits here: https://goo.gl/Vjv6XV
.. The image is included as raw HTML because it has clickable nodes.
.. raw:: html

  <map name="learning-outcomes-curriculum-areas-map">
    <area shape="rect" coords="215,90,320,126" href="#topics-content-directory">
    <area shape="rect" coords="281,342,387,377" href="#learning-outcomes-file">
    <area shape="rect" coords="281,616,387,652" href="#curriculum-areas-file">
  </map>
  <img src="../_static/img/topics_adding_learning_outcomes_curriculum_areas_flowchart.png" usemap="#learning-outcomes-curriculum-areas-map">

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

.. raw:: html
  :file: ../_static/html_snippets/topics_content_directory_tree_only_yaml.html

.. _application-structure-file:

Application Structure File
------------------------------------------------------------------------------

This file defines the top level configuration files to process for defining
the content of the topics application.

The location of this file is within a language file, and it must be named:
``structure.yaml``

This file must contain the following key/value pairs:

- ``learning-outcomes`` - The path to the configuration file for learning outcomes.
  This file lists learning outcomes for all topics.

  - For example:

    .. code-block:: yaml

      learning-outcomes: learning-outcomes.yaml

- ``curriculum-areas`` - The path to the configuration file for curriculum
  areas.
  This file lists curriculum areas for all topics.

  - For example:

    .. code-block:: yaml

      curriculum-areas: curriculum-areas.yaml

- ``programming-exercises-structure`` - The path to the configuration file for
  programming exercises structure.
  This file defines languages and difficulty levels for all programming
  exercises.

  - For example:

    .. code-block:: yaml

      programming-exercises-structure: programming-exercises-structure.yaml

- ``topic-structure-files`` - A list of paths to the configuration file for
  each topic to be included.
  The order of topics here defines their order on the website.

  - For example:

    .. code-block:: yaml

      topic-structure-files:
        - binary-numbers/binary-numbers.yaml
        - error-detection-correction/error-detection-correction.yaml

A complete application structure file may look like the following:

.. code-block:: yaml

  learning-outcomes: learning-outcomes.yaml
  curriculum-areas: curriculum-areas.yaml
  programming-exercises-structure: programming-exercises-structure.yaml
  topic-structure-files:
    - binary-numbers/binary-numbers.yaml
    - error-detection-correction/error-detection-correction.yaml

.. _topic-file:

Topic File
------------------------------------------------------------------------------

This file defines the attributes of a specific topic, including connected
unit plan, programming exercise, and curriculum integration configuration
files.

The location of this file is within a topic directory.
This file is listed in the :ref:`application-structure-file`.

This file must contain the following key/value pairs:

- ``slug`` - The URL slug for this topic (see :ref:`what-is-a-slug`).

  - For example:

    .. code-block:: yaml

      slug: binary-numbers

  - The following slugs are not allowed for topics:

    - ``curriculum-integrations``

- ``md-file`` - The Markdown file containing the description of the topic.
  This is essentially the text for the webpage for the topic.
  The name of the topic is retrieved from the first header in this file.
  The file path is relative to the YAML file.

  - For example:

    .. code-block:: yaml

      md-file: index.md

- ``icon`` - The image icon used for the topic within the static directory.
  The path is from the top of the static directory.

  - For example:

    .. code-block:: yaml

      icon: img/binary-numbers-0-1.png

The file may also contain any of the following optional key/value pairs:

- ``unit-plans`` - A list of unit plan configuaration files for this topic.
  The order here defines their order on the website.
  The file path is relative to the YAML file.

  - For example:

    .. code-block:: yaml

      unit-plans:
        - unit-plan/unit-plan.yaml

- ``programming-exercises`` - A configuaration file defining programming
  exercises for the topic.
  The file path is relative to the YAML file.

  - For example:

    .. code-block:: yaml

      programming-exercises: programming-exercises/programming-exercises.yaml

- ``follow-up-activities`` - A configuaration file defining follow up
  activities for the topic.
  The file path is relative to the YAML file.

  - For example:

    .. code-block:: yaml

      follow-up-activities: follow-up-activities/follow-up-activities.yaml

- ``other-resources-md-file`` - A Markdown file describing other resources.
  The file path is relative to the YAML file.

  - For example:

    .. code-block:: yaml

      other-resources-md-file: other-resources.md

A complete topic file may look like the following:

.. code-block:: yaml

  slug: binary-numbers
  md-file: index.md
  icon: img/binary-numbers-0-1.png
  unit-plans:
    - unit-plan/unit-plan.yaml
  programming-exercises: programming-exercises/programming-exercises.yaml
  follow-up-activities: follow-up-activities/follow-up-activities.yaml
  other-resources-md-file: other-resources.md

.. _unit-plan-file:

Unit Plan File
------------------------------------------------------------------------------

This file defines the attributes of a unit plan, including all lessons (and
their respective attributes) for the unit plan.

The location of this file is within a unit plan directory.
These files are listed in a :ref:`topic-file`.

This file must contain the following key/value pairs:

- ``slug`` - The URL slug for this unit plan (see :ref:`what-is-a-slug`).
  We recommend using 'unit-plan' for the first unit-plan for each topic

  - For example:

    .. code-block:: yaml

      slug: unit-plan

- ``md-file`` - The Markdown file containing the description of the topic.
  This is essentially the text for the webpage for the topic.
  The name of the unit plan is retrieved from the first header in this file.
  The file path is relative to the YAML file.

  - For example:

    .. code-block:: yaml

      md-file: index.md

- ``lessons`` - A key containing all lesson slugs (see :ref:`what-is-a-slug`),
  and these lesson slugs contain the lesson data.
  We don't recommend using numbered slugs (for example: ``lesson-1``) as
  ordering may change but a slug should never change.

  - For example:

    .. code-block:: yaml

      lessons:
        introduction-to-bits:
          ...lesson data here...
        counting-bits:
          ...lesson data here...

  - Each lesson slug must contain the following values:

    - ``md-file`` - The Markdown file containing the description of the lesson.
      This is essentially the text for the webpage for the lesson.
      The name of the lesson is retrieved from the first header in this file.
      The file path is relative to the YAML file.

      - For example:

        .. code-block:: yaml

          md-file: introduction-to-bits/index.md

    - ``minimum-age`` - The minimum age this lesson is suitable for.

      - For example:

        .. code-block:: yaml

          minimum-age: 5

    - ``maximum-age`` - The maximum age this lesson is suitable for.

      - For example:

        .. code-block:: yaml

          minimum-age: 7

    - ``number`` - The number order for this lesson.
      Lessons are sorted by minimum age, maximum age, then number
      so lessons in different age ranges can use the same number
      without conflict.

      - For example:

        .. code-block:: yaml

          number: 1

  - Each lesson may also contain any of the following key/value pairs
    (same indentation as ``minimum-age``, ``maximum-age``, etc):

    - ``programming-exercises`` - A list of slugs for the programming
      exercises for this lesson.
      The slugs are defined in the :ref:`programming-exercises-file` for
      the same topic as the lessons.
      You can include any number (including zero) of programming exercises,
      and you can list the same programming exercise for different lessons.
      The programming exercises listed should be relevant to the content of
      the lesson, and not the age range of the lesson.
      This is because programming exercises are written for all ages.

      - For example:

        .. code-block:: yaml

          programming-exercises:
            - count-to-16
            - count-to-a-million

    - ``learning-outcomes`` - A list of slugs for the learning outcomes for
      this lesson.
      The slugs are defined in the :ref:`learning-outcomes-file`.

      - For example:

        .. code-block:: yaml

          learning-outcomes:
            - binary-data-representation
            - binary-count
            - binary-convert-decimal
            - binary-justify-representation

    - ``curriculum-areas`` - A list of slugs for the curriculum areas for
      this lesson.
      The slugs are defined in the :ref:`curriculum-areas-file`.

      - For example:

        .. code-block:: yaml

          curriculum-areas:
            - maths

    - ``resources-classroom`` - A list of Markdown text of classroom resources
      required for this lesson resources-classroom.

      - For example:

        .. code-block:: yaml

          resources-classroom:
            - Pens
            - String

    - ``resources-generated`` - A list of handout resources generated by CS
      Unplugged system.

      - Each resource listed requires the following two keys:

        - ``slug`` - The slug of the resource in the resources app
          (see :ref:`what-is-a-slug`).

        - ``description`` - Markdown text describing the use of the resource.

      - For example:

        .. code-block:: yaml

          resources-generated:
            - slug: sorting-network
              description: One copy per student
            - slug: treasure-hunt
              description: One copy per student

An example unit plan configuaration file with multiple lessons may look like
the following:

.. code-block:: yaml

  slug: unit-plan
  md-file: unit-plan.md
  lessons:
    introduction-to-bits:
      minimum-age: 5
      maximum-age: 7
      number: 1
      md-file: introduction-to-bits/index.md
      programming-exercises:
        - count-to-16
      learning-outcomes:
        - binary-data-representation
        - binary-count
        - binary-convert-decimal
        - binary-justify-representation
      curriculum-areas:
        - maths
      resources-classroom:
        - Pens
        - String
      resources-generated:
        - slug: sorting-network
          description: One copy per student

    counting-bits:
      minimum-age: 5
      maximum-age: 7
      number: 2
      md-file: counting-bits/index.md
      programming-exercises:
        - count-to-16
        - count-to-a-million
      learning-outcomes:
        - binary-data-representation
        - binary-count
      curriculum-areas:
        - maths
        - science
      resources-classroom:
        - Pens

    a-byteful-of-data:
      minimum-age: 8
      maximum-age: 10
      number: 1
      md-file: a-byteful-of-data/index.md
      learning-outcomes:
        - binary-convert-decimal
        - binary-justify-representation
      curriculum-areas:
        - maths
        - art

.. _curriculum-integrations-file:

Curriculum Integrations File
------------------------------------------------------------------------------

This file defines the curriculum integrations for a topic (and their respective
attributes).

The location of this file is within a topic directory.
This configuaration file is listed in a :ref:`topic-file`.
It is also valid to have no configuaration file if there are no curriculum
integrations for a topic.

This file can contain as many curriculum integrations as you like, as long as
each curriculum integration has a unique slug URL within the topic.

The file should have the following key/value pair structure:

- **Curriculum integration slugs** - A slug listed for each curriculum
  integration (see :ref:`what-is-a-slug`).
  We don't recommend using numbered slugs (for example: ``integration-1``) as
  ordering may change but a slug should never change.

  - For example:

    .. code-block:: yaml

      binary-number-bracelets:
        ...integration data here...
      hidden-binary-signals:
        ...integration data here...

  - Each curriculum integration slug must contain the following values:

    - ``md-file`` - The Markdown file containing the description of the
      curriculum integration.
      This is essentially the text for the webpage for the integration.
      The name of the curriculum integration is retrieved from the first
      heading in this file.
      The file path is relative to the YAML file.

      - For example:

        .. code-block:: yaml

          md-file: binary-number-bracelets/index.md

    - ``number`` - The number order for this curriculum integration.
      Integrations are sorted this number.

      - For example:

        .. code-block:: yaml

          number: 1

    - ``curriculum-areas`` - A list of slugs for the curriculum areas for
      this curriculum integration.
      The slugs are defined in the :ref:`curriculum-areas-file`.

      - For example:

        .. code-block:: yaml

          curriculum-areas:
            - maths

  - Each curriculum integration slug may also contain the following
    (same indentation as ``md-file``, ``number``, etc):

    - ``prerequisite-lessons`` - A list of lesson slugs for any lessons that
      are expected to be completed before the attempting this curriculum
      integration.
      If any lessons are listed, a warning is provided to the user that they
      must know the content covered in the listed lessons.
      Since curriculum integrations are stored at a topic level, both the unit
      plan slug and lesson slug must be provided.
      The slugs should be separated by the ``/`` character, see example
      below.
      The slugs are defined in the :ref:`unit-plan-file`.

      - For example:

        .. code-block:: yaml

          prerequisite-lessons:
            - unit-plan/introduction-to-bits
            - unit-plan/counting-bits

An example curriculum integrations configuaration file with multiple activities
may look like the following:

.. code-block:: yaml

  binary-number-bracelets:
    number: 1
    md-file: bracelets.md
    curriculum-areas:
      - arts
      - design
    prerequisite-lessons:
      - unit-plan/introduction-to-bits
      - unit-plan/counting-bits

  hidden-binary-signals:
    number: 2
    md-file: hidden-binary-signals.md
    curriculum-areas:
      - science

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

- ``languages`` - A key containing all language slugs
  (see :ref:`what-is-a-slug`) for available languages for implementations of
  programming execises.
  These slugs contain the language data.

  - For example:

    .. code-block:: yaml

      lessons:
        python:
          ...language data here...
        scratch:
          ...language data here...

  - Each language slug must contain the following values:

    - ``name`` - The name of the language implementation.

      - For example:

        .. code-block:: yaml

          name: Scratch

    - ``icon`` - The image icon used for the language within the static
      directory.
      The path is from the top of the static directory.

      - For example:

        .. code-block:: yaml

          icon: img/scratch-cat.png


- ``difficulties`` - A list of available difficulties for programming execises.
  The difficulties are stored in a list for easier reading but will
  be displayed by sorting the level attribute from smallest to largest.

  - Each difficulty list item must contain the following values:

    - ``level`` - A number to represent the difficulty level level attribute
      as a number (smaller = easier).

      - For example:

        .. code-block:: yaml

          level: 1

    - ``name`` - The name for the difficulty level to display to the user.

      - For example:

        .. code-block:: yaml

          name: Beginner

A complete programming exercise structure file may look like the following:

.. code-block:: yaml

  languages:
    scratch:
      name: Scratch
      icon: img/scratch-cat.png
    python:
      name: Python
      icon: img/python-logo.png
    cplusplus:
      name: C++
      icon: img/cplusplus-logo.png

  difficulties:
    - level: 1
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

- **Programming exercise slugs** - A slug listed for each programming exercise
  (see :ref:`what-is-a-slug`).
  We don't recommend using numbered slugs (for example: ``exercise-1``) as
  ordering may change but a slug should never change.

  - For example:

    .. code-block:: yaml

      count-to-16:
        ...exercise data here...
      count-to-a-million:
        ...exercise data here...

  - Each programming exercise slug must contain the following values:

    - ``md-file`` - The Markdown file containing the description of the
      programming exercise.
      This is essentially the text for the webpage for the exercise.
      The name of the programming exercise is retrieved from the first header
      in this file.
      The file path is relative to the YAML file.

      - For example:

        .. code-block:: yaml

          md-file: count-to-16/index.md

    - ``number`` - The number order for this programming exercise.
      Exercises are sorted this number.

      - For example:

        .. code-block:: yaml

          number: 1

    - ``difficulty-level`` - The difficulty level number for this programming
      exercise.
      The difficulty numbers are defined in
      :ref:`programming-exercises-structure-file`.

      - For example:

        .. code-block:: yaml

          difficulty-level: 1

    - ``learning-outcomes`` - A list of slugs for the learning outcomes for
      this lesson.
      The slugs are defined in the :ref:`learning-outcomes-file`.

      - For example:

        .. code-block:: yaml

          learning-outcomes:
            - programming-sequence
            - programming-one-input-output

    - ``programming-languages`` - A key containing all programming language
      slugs (see :ref:`what-is-a-slug`), and these language slugs contain the
      language implementation data.
      The slugs are defined in the :ref:`programming-exercises-structure-file`.

      - For example:

        .. code-block:: yaml

          programming-languages:
            python:
              ...Python data here...
            scratch:
              ...Scratch data here...

      - Each language slug must contain the following values:

        - ``expected-result`` - The Markdown file containing the expected
          result for the language implementation of the exercise.
          This is essentially the text for the expected result section for
          this language on the website for this exercise.
          The file path is relative to the YAML file.

          - For example:

            .. code-block:: yaml

              expected-result: count-to-16/scratch-expected.md

        - ``hints`` - The Markdown file containing the hints for the language
          implementation of the exercise.
          This is essentially the text for the hints section for this language
          on the website for this exercise.
          The file path is relative to the YAML file.

          - For example:

            .. code-block:: yaml

              hints: count-to-16/scratch-hints.md

        - ``solution`` - The Markdown file containing the solution for the
          language implementation of the exercise.
          This is essentially the text for the solution section for this
          language on the website for this exercise.
          The file path is relative to the YAML file.

          - For example:

            .. code-block:: yaml

              solution: count-to-16/scratch-solution.md

A complete programming exercise file may look like the following:

.. code-block:: yaml

  count-to-16:
    number: 1
    difficulty-level: 1
    md-file: count-to-16/index.md
    learning-outcomes:
      - programming-sequence
      - programming-one-input-output
    programming-languages:
      scratch:
        expected-result: count-to-16/scratch-expected.md
        hints: count-to-16/scratch-hints.md
        solution: count-to-16/scratch-solution.md
      python:
        expected-result: count-to-16/python-expected.md
        hints: count-to-16/python-hints.md
        solution: count-to-16/python-solution.md

  count-to-a-million:
    number: 2
    difficulty-level: 3
    md-file: count-to-a-million/index.md
    learning-outcomes:
      - programming-basic-logic
    programming-languages:
      scratch:
        expected-result: count-to-a-million/scratch-expected.md
        hints: count-to-a-million/scratch-hints.md
        solution: count-to-a-million/scratch-solution.md
      python:
        expected-result: count-to-a-million/python-expected.md
        hints: count-to-a-million/python-hints.md
        solution: count-to-a-million/python-solution.md

.. _learning-outcomes-file:

Learning Outcomes File
------------------------------------------------------------------------------

This file defines the learning outcomes avilable for all topics.

The location of this file is within the language directory.
This file is listed in a :ref:`application-structure-file`.
This file can contain as many learning outcomes as you like.

The file should only contain pairs of outcome slug (see :ref:`what-is-a-slug`)
to outcome text pairs.

For example:

.. code-block:: yaml

  binary-data-representation: Explain how a binary digit is represented using two contrasting values.
  binary-count: Demonstrate how to represent any number between 0 and 31 using binary.
  binary-convert-decimal: Perform a demonstration of how the binary number system works by converting any decimal number into a binary number.
  binary-justify-representation: Argue that 0’s and 1’s are still a correct way to represent what is stored in the computer.

.. note::

  Lessons and programming exercises area to learning outcomes by listing
  their slug.

.. _curriculum-areas-file:

Curriculum Areas File
------------------------------------------------------------------------------

This file defines the curriculum areas avilable for all topics.

The location of this file is within the language directory.
This file is listed in a :ref:`application-structure-file`.
This file can contain as many curriculum areas as you like.
Lessons and follow up activities area to curriculums by listing their
slug.

The file should have the following key/value pairs:

- **Curriculum area slugs** - A slug listed for each curriculum area
  (see :ref:`what-is-a-slug`).

  - For example:

    .. code-block:: yaml

      maths:
        ...math data here...
      science:
        ...science data here...

  - Each curriculum area slug must contain the following values:

    - ``name`` - The text for the curriculum area for displaying to the user.

An example curriculum areas file with multiple curriculums may look like
the following:

.. code-block:: yaml

  maths:
    name: Maths

  science:
    name: Science

  art:
    name: Art


Curriculum areas can be broken down into more specific areas (for example, Geometry is a specific area of Maths). This may look like the following:

.. code-block:: yaml

  maths:
    name: Maths
    children:
      maths-geometry:
        name: Maths - Geometry
      maths-algebra:
        name: Maths - Algebra

  science:
    name: Science

  art:
    name: Art

The maximum depth for children is one, that is, children curriculum areas cannot have children.

.. note::

  When including a curriculum area in another configuration file, adding a child curriculum area will automatically add the parent curriculum area, you do not need to specify this manually. For example, adding "maths-geometry" means that "maths" is automatically included.
