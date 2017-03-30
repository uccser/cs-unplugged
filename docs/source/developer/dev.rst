Dev Application
##############################################################################

This application:

1. Provides a quick reference for seeing what content has been added to the databse.
2. Allows authors to check markdown content has rendered as expected.
3. Is to be used in a development environment.

This application is available only when ``DEBUG`` mode is enabled (and therefore is not
visible in production).

This application does not necessarily show the same connection/layout of content as in
the actual site itself. This is because some of the links in this app link to the actual
site, but many link to a copy of the template from the topics app (and are therefore are
likely to be out of date at any given point in time).


What does this app contain?
==============================================================================

- Topics - a list of available topics, with their child unit plans and lessons.
  All of these link to the corresponding page in the Topics application. The purpose of 
  this list is to give an overview of which lessons have been added to each unit plan,
  and which unit plans have been added to each topic.
  It is possible for someone to have created a markdown file for a lesson (or unit plan,
  or topic) but it now be shown in this list, this is because only markdown files listed
  in configuration (``yaml``) files are loaded into the database.

- Curriculum areas - a list of curriculum areas and their subdomains.

- Curriculum integrations - a list of curriculum integration activities. This **does
  not** link to the template from the topic application. This is because it is possible
  for a curriculum integration to be loaded into the database without it being assigned
  to a topic