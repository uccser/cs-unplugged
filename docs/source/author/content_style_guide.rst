Content Style Guide
##############################################################################

.. note::

  This page is currently intended for internal staff only.


.. contents:: Contents
  :local:

 
Writing Style
==============================================================================

When using pronouns in reference to a hypothetical person, gender neutral pronouns (they/their/them) should be used. 
 
All documents (other than those for internal use only) must be written clearly and simply so that a non-expert is able to understand them.
Preferably documents should be readable for students. 
 
Any jargon used needs to be clearly explained. 


Capitalisation Rules
------------------------------------------------------------------------------

In the majority of cases capitalisation should not be used for keywords and titles, with the following exceptions, where the phrase refers to a commonly used term that is often capitilised in the literature:

- Computer Science
- Computational Thinking
- Digital Technologies (note that this is the correct form to refer to the subject area in NZ, with caps and plural; if it's referring to something other than the subject then use lower case e.g. "smartphones and other digital technologies", or even better, avoid the phrase e.g. "smartphones and other digital devices")
- Sorting Network
- Numeracy
- Literacy
 
The following wouldn't be capitalised:
binary number(s), digits, binary digits
 


Google Drive Folder Structure
==============================================================================

Including Images
------------------------------------------------------------------------------

All images included in a document have a comment which links to the original image file in a specified Google Drive Folder.


Completed Documents
------------------------------------------------------------------------------

Once a document is completed:

1. Prefix the document name with ``COMPLETE -``, e.g. ``Unit plan`` will become ``COMPLETE - Unit plan``.

2. Put a note in the document header:

    *A later version is under development, and will be released later in 2017.
    No further updates will be made to this document.*

3. Mark the document as ``Finished in Google Docs/Ready for GitHub`` on the Scorecard.

3. Do not edit the document any further!


Topic Folder
------------------------------------------------------------------------------

Each topic has its own folder in the ``Draft units and lessons`` folder, which contains all content relevant to that topic.
A topic folder contains unit plan folders as they are in the scorecard.
This applies to all topics even if they only contain one unit. 
The structure of the topic folder, and folder and document names, are as they are below:
 
.. code-block:: none

  └── topic-name/
      ├── Programming challenges/
      ├── Resources/
      ├── unit-name Unit/
      │   ├── Lessons/
      │   │   ├── 5-7/
      │   │   ├── 8-10/
      │   │   └── 11-14/
      │   ├── Ideas
      │   └── Unit plan
      ├── Glossary
      ├── Topic description
      ├── Curriculum integration
      └── Diff file

Note:

- If lessons do not cover all age groups then the relevant folder(s) should be omitted.

- The ``Diff file`` is only required if the folder contains documents that are complete.


Glossary
------------------------------------------------------------------------------
The following are added to the glossary and linked to where the words are used:

- All Computer Science, programming, and Computational thinking jargon
- All Education jargon
- All curriculum language that is not broadly used internationally


Topic description
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Contains the description of the topic!
This description applies to all the units within the topic.
It is one introductory paragraph, less than 150 words, which gives a big picture overview of why this topic is being taught/is relevant, and what it will cover.


Curriculum integration
------------------------------------------------------------------------------

Contains idea and instruction cards for incorporating the unit content into lessons with other subjects (e.g. writing, art, mathematics, etc).
Cards are short and preferably half a page - two pages in length (including any pictures).


Diff file
------------------------------------------------------------------------------

Until a completed document has been entered into GitHub any proposed edits are
noted in the diff file.
Once a document has been fully added to GitHub then the notes are moved from the Diff file to GitHub, and all future edits for the document are entered as issues on GitHub.

When adding a suggested edit to the diff file:

- It is listed under the heading corresponding to the name of the document.

- All typo and grammar fixes include both the incorrect and corrected version in quotation marks.

- Any links that need to be added are included with the text for the link, and links that need to be changed include the current and new links, including links for image files.


Unit Folder
------------------------------------------------------------------------------

Ideas
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Dumping ground document for ideas for future lessons, units, curriculum integrations etc. This doc won't be moved to GitHub so is always open for edits.


Unit plan
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The `Unit Plan Template is here`_.
Sections in italics are descriptions of sections/words that are not are to appear in the final unit plan.

Lessons
------------------------------------------------------------------------------

The `Lesson Template is here`_.
Sections in italics are descriptions of sections/words that are not are to appear in the final lesson.
 
Separate folders are used for each age group: 5-7, 8-10, and 11-14.
Lessons are numbered. 
 
If the same, identical, lesson is used for multiple age groups the file is copied to each folder and a note is added to the top of the document saying “This is identical to <insert link to lesson>”. The original document that is linked to should be the one in the lowest age group, e.g. if the same lesson occurs for 8-10 and 11-14, then the 11-14 copy should contain the note “This is identical to <insert link to lesson>”, rather than the 8-10 lesson.
 
 
Learning Outcomes
------------------------------------------------------------------------------

Each learning outcome has a unique text value, unique key, and belongs to a topic area.
The list of learning outcomes can be found in the Scorecard and are named according to the rules described in the sections below.


Text value
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The text value is the text that will be displayed in the learning outcomes sections on the website.
These are written using language familiar to teachers and simple enough that it is understandable for students.
Learning outcomes always begin with a verb.


Key
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Learning outcome keys need to follow these rules:

- Words in keys are written in lowercase and are separated with a hyphen e.g. ``explain-different-states``.

- The order of words in the key are:
  
  1. The topic area of the outcome
  2. If the topic area is cross-curricula, the curriculum area of the outcome
  3. The verb used at the beginning of the text value
  4. Keywords describing the content of the outcome
 
There is no limit on the length of keys as it is important they are as descriptive as possible.


Programming Challenges
==============================================================================

There needs to be enough scaffolding to support students to be able to achieve a result, independently. 

When transferrring a programming challenge from Google Docs to GitHub, these are the rules to follow:

 
1. Separate out all the blocks that “click” together, leaving all the information inside where the parameter is written. All duplicates of a block should be displayed.
 
2. The order of the blocks should always be randomised. If there are more than six blocks the blocks should be split into groups by colour, and then randomise the order of the blocks in these groups. This is the order the colour groups should be displayed in:

.. image:: ../_static/img/scratch_example_1.png
  :alt: A image showing the order to display colour groups in.
 
2. Where a variable is inserted into another block, those blocks stay together, example below:
 
.. image:: ../_static/img/scratch_example_2.png
  :alt: A screenshot of a say block containing a variable.
 
3. All join blocks are displayed as one and all the variables/text are included, example below:
  
.. image:: ../_static/img/scratch_example_3.png
  :alt: A screenshot of several join blocks together.
 
4. For blocks containing join blocks keep the join block within the parent block, example below.

.. image:: ../_static/img/scratch_example_4.png
  :alt: A screenshot of a set block containing a join block.

5. Loops should keep the condition blocks, but the blocks within the loop should be extracted.
 
.. _Unit Plan Template is here: https://docs.google.com/document/d/1DBwrpKy9sulDq_O1vKQoLapTuhzIIq3iHIcwKKvCKK8/
.. _Lesson Template is here: https://docs.google.com/document/d/1uUN7kPsTlyIGEnmAxTDNat7S4yKM5VNzrnmtTnegSaQ/edit