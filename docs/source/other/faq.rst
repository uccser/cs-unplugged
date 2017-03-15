Frequently asked questions
##############################################################################

The topics application is the main focus of the CS Unplugged website, as it
contains the majority of educational material for the project.

.. contents:: Contents
  :local:

.. _what-is-a-slug:

What is a URL slug?
==============================================================================

A URL slug is a short label for something, containing only letters, numbers,
or hyphens.
They’re generally used in URLs.
In our system, a slug must be no longer than 50 characters, and use hyphens
instead of underscores.

These are *valid* example slugs:

- ``algorithms``
- ``binary-numbers``
- ``exercise-2``

These are *invalid* example slugs:

- ``Algorithms``
- ``Binary Numbers``
- ``Binary_Numbers``
- ``binary_numbers``
- ``exercise 2``

See also:

- `Definition of URL slug on Wikipedia`_

.. _what-is-an-application:

What is an application?
==============================================================================

Django contains 'applications' which are Python packages that provide
some set of features.
Each large part/chunk of the CS Unplugged is a separate application.
Read :ref:`this section in our project structure guide <django-applications>`
for details of the applications used in the CS Unplugged system.

.. _Definition of URL slug on Wikipedia: https://en.wikipedia.org/wiki/Semantic_URL#Slug
