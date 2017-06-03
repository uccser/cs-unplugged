Content Style Guide
##############################################################################

.. note::

  This page is currently intended for internal staff only.


.. contents:: Contents
  :local:

 
Writing style
==============================================================================

When using pronouns in reference to a hypothetical person, gender neutral pronouns (they/their/them) should be used. 
 
All documents (other than those for internal use only) must be written clearly and simply so that a non-expert is able to understand them. Preferably documents should be readable for students. 
 
Any jargon used needs to be clearly explained. 


Capitalisation rules
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
 

Including images
==============================================================================

All images included in a document have a comment which links to the original image file in a specified Google Drive Folder. See section on Images Folder.

Completed files
==============================================================================

When files are ready for github they are given the prefix “COMPLETE - “, e.g. “Unit plan” will become “COMPLETE - Unit plan”. Once a file has been marked as complete and ready for github it must not be edited, any edits or suggestions made to the Google doc are ignored.
 
Until a completed document has been entered into github any proposed edits are instead noted in the diff file. Once a document has been fully added to github then the notes for it in the diff file are moved to github, removed from the diff file, and all future edits for the document are entered as issues on github.
 
When adding a suggested edit to the diff file it is placed under the heading which names the document it refers to. All typo and grammar fixes include both the incorrect and corrected version in quotation marks. Any links that need to be added are included with the text for the link, and links that need to be changed include the current and new links, including links for image files.

Topic folder
==============================================================================

Each topic has its own folder in the “Draft units and lessons” folder, which contains all content relevant to that topic. Topic names and the units underneath each topic folder are as they are in the scorecard. This applies to all topics even if they only contain one unit. 
The structure of the topic folder, and folder and document names (in bold), are as they are below:
 
- Folder: <Topic name>
  - Folder: Programming challenges
  - Folder: Resources
  - Doc: Glossary
  - Doc: Topic description
  - Doc: Curriculum integration
  - Doc: Diff file - if any files are complete
  - Folder: <Unit name> Unit
    
    - Doc: Unit plan
    - Folder: Lessons - if lessons do not cover all age groups then the relevant folder(s) should be omitted
    
      - Folder: 5-7
      - Folder: 8-10
      - Folder: 11-14
    
    - Doc: Ideas

Topic Description
------------------------------------------------------------------------------
As you might guess, contains the description of the topic!
This description applies to all the units within the topic. It is one introductory paragraph, less than 150 words, which gives a big picture overview of why this topic is being taught/is relevant, and what it will cover.
 
Glossary
------------------------------------------------------------------------------
The following are added to the glossary and linked to where the words are used:

- All Computer Science, programming, and Computational thinking jargon
- All Education jargon
- All curriculum language that is not broadly used internationally
 
Unit folder
==============================================================================

Ideas
------------------------------------------------------------------------------

Dumping ground document for ideas for future lessons, units, curriculum integrations etc. This doc won't be moved to github so is always open for edits.
 
Unit plan
------------------------------------------------------------------------------

Template here.
Sections in italics are descriptions of sections, sections/words that are not are to appear in the final unit plan

Curriculum integration
------------------------------------------------------------------------------

Contains idea and instruction cards for incorporating the unit content into lessons with other subjects, such as writing and art. Cards are short and preferably half a page - two pages in length (including any pictures).
 
Lessons
------------------------------------------------------------------------------

Template here. - complete
Sections in italics are descriptions of sections, sections/words that are not are to appear in the final unit plan
 
Separate folders are used for each age group: 5-7, 8-10, and 11-14. Lessons are numbered. 
 
If the same, identical, lesson is used for multiple age groups the file is copied to each folder and a note is added to the top of the document saying “This is identical to <insert link to lesson>”. The original document that is linked too should be the one in the lowest age group, e.g. if the same lesson occurs for 8-10 and 11-14, then the 11-14 copy should contain the note “This is identical to <insert link to lesson>”, rather than the 8-10 lesson.
 
 
Learning Outcomes
==============================================================================

Each learning outcome has a unique text value, unique key, and belongs to a topic area

Text value
------------------------------------------------------------------------------

The text value is the text that will be displayed in the learning outcomes sections on the website. These are written using language familiar to teachers and simple enough that it is understandable for students. Learning outcomes always begin with a verb.

Key
------------------------------------------------------------------------------

Learning outcome keys need to follow these rules:
- Words in keys are written in lowercase and are separated with a - e.g. explain-different-states.

- The order of words in the key are:
  1. The topic area of the outcome
  2. If the topic area is cross-curricula, the curriculum area of the outcome
  3. The verb used at the beginning of the text value
  4. Keywords describing the content of the outcome
 
There is no limit on the length of keys as it is important they are descriptive enough.
 
 
Resources
==============================================================================
 
Programming Challenges
==============================================================================

Currently this is the rules that Hayley and Jack use to create the suggested blocks for the programming languages. 
 
There needs to be enough scaffolding to support students to be able to achieve a result, independently. 
 
Separate out all the blocks that “click” together, leaving all the information inside where the parameter is written. All duplicates of a block should be displayed. See examples below: 
 
1. The order of the blocks should always be randomised.
If there are more than six blocks: the blocks should be split into groups by colour, and then randomise the order of the blocks in these groups.
This is the order the colour groups should be displayed in:

 
2. Where a variable is inserted into another block, those blocks stay together ie
 

 
3. All join blocks are displayed as one and all the variables/text are included ie 
 

 
 
4. For blocks containing join blocks - keep the join block within the parent block.

 
5. Loops should keep the condition blocks, but the blocks within the loop should be extracted.

 
