Dev Application
##############################################################################

This application:

1. Provides a quick reference for viewing what content has been added to the database.
2. Allows authors to check Markdown content has rendered as expected.
3. Is only to be used in a development environment.

This application is available only when ``DEBUG`` mode is enabled (and therefore is not
visible in production). ``DEBUG`` mode is enabled by default when developing locally.

This application does not necessarily show the same connection/layout of content as in
the actual site itself. This is because some of the links in this app link to the actual
site, but many link to a copy of the template from the topics app (and are therefore are
likely to be out of date at any given point in time).


What does this app contain?
==============================================================================

The dev application currently contains the following:

- Topics - a list of available topics, and links to the corresponding template in the
  topics applications. The children listed under each topic are:

    - Unit Plans and Lessons. - All of these link to the corresponding page in the Topics
      application. The purpose of this list is to give an overview of which lessons have
      been added to each unit plan, and which unit plans have been added to each topic.
      It is possible for someone to have created a markdown file for a lesson (or unit
      plan, or topic) but it not be shown in this list, this is because only Markdown
      files listed in configuration (``yaml``) files are loaded into the database.

    - Curriculum Integrations - a list of curriculum integration activities. This **does
      not** link to the template from the topic application. This is because a curriculum
      integration only has to be linked to a topic (at the very least) in order for it to
      be loaded into the database, i.e. it is possible for a curriculum integration to be
      loaded into the database without it being assigned to a lesson.

    - Programming Challenges - a list of programming challenges. This **does not** link to
      the template from the topic application. This is because a programming challenge
      only has to be linked to a topic (at the very least) in order for it to be loaded
      into the database, i.e. it is possible for a programming challenge to be loaded
      into the database without it being assigned to a lesson.

- Curriculum Areas - a list of curriculum areas and their subdomains.

- Learning Outcomes - a list of learning outcomes.

- Programming Challenge Languages - a list of programming languages that programming
  challenge solutions can be given in.

- Programming Challenge Difficulties - a list of difficulty levels and their corresponding
  title.
