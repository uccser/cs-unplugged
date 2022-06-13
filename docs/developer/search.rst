Search Feature
##############################################################################

The search feature uses `Django Haystack <http://haystacksearch.org/>`_ to search indexed models.
Two filters are available:

1.  Filter by model.
2.  Filter by related curriculum areas.
    The two models that have related curriculum areas:

    -   Curriculum integrations.
    -   Lessons (through learning outcomes with curriculum areas).

The search index indexes text using character fields, which requires exact word matches to find objects, however the character field gives fast performance.

The search page form uses `multiple-select <http://wenzhixin.net.cn/p/multiple-select/>`_ widgets to allow the user to easily select items to filter by.

Indexing of general and Classic CS Unplugged pages
==============================================================================

Allowing the user to search for general pages (for example, the webpage on computational thinking) and Classic CS Unplugged page (for example, the graph colouring activity) was an important feature to implement.
There were three main strategies to accomplish this task:

1. **Modify Django Haystack to handle non-model data** - This would have been a very hard approach to take (Django Haystack authors do not recommend it) as the package is built around models to its core.
2. **After Django Haystack performs search, using Python to search pages** - This would be very easy to implement however would lower search performance as it would occur for each request.
3. **Create models for Django Haystack to index** - This would involve adding models to the ``general`` and ``classic`` applications for content to be indexed.

The best strategy of these was number 3, as it didn't require extensive rewriting of the Django Haystack package and complex searching on every request.
Therefore models were added to both applications for the two types of content.
Initially we converted all data into configuration files for model creation (for example, instead of manually listing all Classic CS Unplugged URLs for redirection in the url routing file, store the redirect data within the model).
However Django is not setup to handle multiple URL routes all based off the pattern.
For example, Django would not check a URL matches a unit plan slug after failing to find a topic:

- ``r"^/topics/(?P<topic_slug>[-\w]+)/$"``
- ``r"^/topics/(?P<lesson_slug>[-\w]+)/$"``

Therefore the current setup of URLs and views for the ``general`` and ``classic`` applications is left untouched, and new configuration files are added for data to be added as models.
The configuration files do duplicate some data, but only for pages that are searchable.

More information on the decisions to implement this feature is `available on GitHub <https://github.com/uccser/cs-unplugged/pull/886>`_.
