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
