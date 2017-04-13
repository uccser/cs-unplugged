Topic Content
##############################################################################

The topics application (see :ref:`what-is-an-application`) is the main focus of
the CS Unplugged website, as it contains the majority of educational material
for the project.

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

When developing locally, once you have a server and ``gulp`` running (see
:doc:`../getting_started/basic_usage`) you can go to the url below to get a
quick overview of what content is loaded:

.. code-block:: none

  localhost:3000/__dev__/

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

The diagram below shows an overview of what is in each config file:

.. image:: ../_static/img/topics_config_file_overview.png


.. _application-structure-file:

Application Structure File
------------------------------------------------------------------------------

- **File Name:** ``structure.yaml``

- **Location:** ``topics/content/<language>/``

- **Purpose:** Defines the top level configuration files to process for defining
  the content of the topics application.

- **Required Fields:**

  - ``topics``: A list of topic names.

- **Optional Fields:**

  - ``misc-structure-files``: A list of configuration files to include in the
    topics application. The files that can be included are listed below (each
    file has its own description in this page). Each of these are optional.

    - ``learning-outcomes``
    - ``curriculum-areas``
    - ``programming-exercises-structure``


A complete application structure file may look like the following:

.. code-block:: yaml

  topics:
    - binary-numbers
    - error-detection-correction

  misc-structure-files:
    - learning-outcomes
    - curriculum-areas
    - programming-exercises-structure

.. _topic-file:

Topic File
------------------------------------------------------------------------------

- **File Name:** ``<topic-name>.yaml``

- **Location:** ``topic/content/<language>/<topic-name>/``

- **Referenced In:** ``topic/content/<launguage>/structure.yaml``

- **Purpose:** This file defines the attributes of a specific topic, including
  connected unit plan, programming exercise, and curriculum integration
  configuration files.

- **Required Fields:**

  - ``unit-plans``: A list of unit plans for this topic.

- **Optional Fields:**

  - ``icon``: An icon for the topic (to be used on a page showing all available
    topics)

  - ``other-resources``: The name of a Markdown file containing information
    about other related (external) resources.

  - ``misc-structure-files``: A list of configuration files to include for this
    particular topic. The files that can be included are listed below (each
    file has its own description in this page). Each of these are optional.

      - ``programming-exercises``
  
      - ``curriculum-integrations``


A complete topic structure file may look like the following:

.. code-block:: yaml

  unit-plans:
    - unit-plan
    - unit-plan-2

  icon: img/binary-numbers-0-1.png

  other-resources: other-resources.md

  misc-structure-files:
    - programming-exercises
    - curriculum-integrations


.. _unit-plan-file:

Unit Plan File
------------------------------------------------------------------------------

- **File Name:** ``<unit-plan-name>.yaml``

- **Location:** ``topic/content/<language>/<topic-name>/<unit-plan-name>``

- **Referenced In:** ``topic/content/<language>/<topic-name>/<topic-name>.yaml``

- **Purpose:** This file defines all the lessons (and their respective)
  attributes for the unit plan.

- **Required Fields:**

  - ``lessons``: This contains a list of lessons their attributes. A lesson
    has its own list of required and optional fields:

      - **Required Fields:**

        - ``<lesson-name>``

        - ``minimum-age``: The suggested minimum age group to teach this lesson
          to.

        - ``maximum-age``: The suggested maximum age group to teach this lesson
          to.

        - ``number``: The number order for this lesson.
          Lessons are sorted by minimum age, maximum age, then number so
          lessons in different age ranges can use the same number without
          conflict.

      - **Optional Fields:**

        - ``programming-exercises``: A list of programming execises that are
          relevant to this lesson.

        - ``learning-outcomes``: A list of learning outcomes relevant to this
          lessons.

        - ``curriculum-areas``: The other areas of a school curriculum that
          this lesson could be taught in.

        - ``resources-classroom``:

        - ``resources-generated``:


A complete unit plan structure file with multiple lessons may look like the
following:

.. code-block:: yaml
  
  lessons:
    
    introduction-to-bits:
      minimum-age: 7
      maximum-age: 11
      number: 1
      programming-exercises:
        - count-to-16
        - count-to-1-million
      learning-outcomes:
        - binary-data-representation
      curriculum-areas*:
        - maths

    how-binary-digits-work:
      minimum-age: 7
      maximum-age: 11
      number: 2
      learning-outcomes:
        - binary-data-representation
        - binary-justify-representation


.. _curriculum-integrations-file:

Curriculum Integrations File
------------------------------------------------------------------------------

- **File Name:** ``curriculum-intergrations.yaml``

- **Location:** ``topics/content/<language>/<topic-name>/``

- **Referenced In:** ``topics/content/<language>/<topic-name>.yaml``

- **Purpose:** Contains a list of activities that can be used to integrate the
  topic with another area in the curriculum.

- **Required Fields:**

  - ``<activity-name>``:This is the name of the integration. Each integration
    has its own list of required and optional fields:

    - **Required Fields:**

      - ``number``:

    - **Optional Fields:**

      - ``curriculum-areas``:

      - ``prerequisite-lessons``:



A complete curriculum integration structure file with multiple activities may
look like the following:

.. code-block:: yaml

  binary-number-bracelets:
    number: 1
    curriculum-areas:
      - math
      - art
    prerequisite-lessons:
      - introduction-to-binary-digits
      - counting-in-binary

  binary-leap-frog:
    number: 2
    curriculum-areas:
      - math
      - pe
    prerequisite-lessons:
      - counting-in-binary

.. _programming-exercises-structure-file:

Programming Exercises Structure File
------------------------------------------------------------------------------

- **File Name:** ``programming-exercises-structure``

- **Location:** ``topics/content/<language>/``

- **Referenced In:** ``topics/content/<language>/structure.yaml``

- **Purpose:** This file defines the structure of programming exercises for all
  topics.

- **Required Fields:**

  - ``language``:

    - **Required Fields:**

      - ``<language-name>``:

        - **Required Fields:**

          - ``name``:

        - **Optional Fields:**

          - ``icon``:


  - ``difficulties``:

    - **Required Fields**:

      - ``level``:

      - ``name``:


A complete programming exercise structure file may look like the following:

.. code-block:: yaml

  language:
    scratch:
      name: Scratch
      icon: img/scratch-cat.png
    ruby:
      name: Ruby

  difficulties:
    - level: 1
      name: Beginner
    - level: 2
      name: Intermediate
    - level: 3
      name: Advanced


.. _programming-exercises-file:

Programming Exercises File
------------------------------------------------------------------------------

- **File Name:** ``programming-exercises.yaml``

- **Location:** ``topics/content/<language>/<topic-name>/programming-exercises``

- **Referenced In:** ``topics/content/<language>/<topic-name>/<topic-name>.yaml``

- **Purpose:** This file defines the programming exercises for a particular
  topic, including their respective attributes.

- **Required Fields:**

  - ``<programming-exercise-name>``

    - **Required Fields:**

      - ``exercise-set-number``:

      - ``exercise-number``: The number order for this programming exercise.
        Exercises are sorted this number.


      - ``difficulty-level``:

      - ``programming-exercises``:

    - **Optional Fields:**

      - ``learning-outcomes``: 


A complete programming exercises structure file may look like the following:

.. code-block:: yaml

  count-to-16:
    exercise-set-number: 1
    exercise-number: 1
    difficulty-level: 1
    programming-languages:
      - ruby
      - python
    learning-outcomes:
      - programming-sequence

  count-to-a-million:
    exercise-set-number: 1
    exercise-number: 2
    difficulty-level: 3
    programming-languages:
      - python
    learning-outcomes:
      - programming-basic-logic
    

.. _learning-outcomes-file:

Learning Outcomes File
------------------------------------------------------------------------------

- **File Name:** ``learning-outcomes.yaml``

- **Location:** ``topics/content/en/``

- **Referenced In:** ``topics/content/en/structure.yaml``

- **Purpose:** Defines the learning outcomes avilable for all topics.

- **Required Fields:**

  - ``<key>``:


A complete learning outcome structure file may look like the following:

.. code-block:: yaml

  binary-data-representation: Explain how a binary digit is represented using two contrasting values.
  binary-count: Demonstrate how to represent any number between 0 and 31 using binary.
  binary-convert-decimal: Perform a demonstration of how the binary number system works by converting any decimal number into a binary number.
  binary-justify-representation: Argue that 0’s and 1’s are still a correct way to represent what is stored in the computer.


.. _curriculum-areas-file:

Curriculum Areas File
------------------------------------------------------------------------------

- **File Name:** ``curriculum-areas.yaml``

- **Location:** ``topics/content/en/``

- **Referenced In:** ``topics/content/en/structure.yaml``

- **Purpose:** Defines the curriculum areas available for all topics.

- **Required Fields:**

  - ``<curriculum area name>``

    - **Required Fields:**

      - ``name``:

  - **Optional Fields:**

    - ``children``:


An example curriculum areas file with multiple curriculums may look like
the following:

.. code-block:: yaml

  maths:
    name: Maths
    children:
      geometry:
        name: Geometry
      algebra:
        name: Algebra

  science:
    name: Science

  art:
    name: Art

.. note::

  The maximum depth for children is one, that is, children curriculum areas
  cannot have children.

.. note::

  When including a curriculum area in another configuration file, adding a child curriculum area will automatically add the parent curriculum area, you do not need to specify this manually. For example, adding "maths-geometry" means that "maths" is automatically included.
