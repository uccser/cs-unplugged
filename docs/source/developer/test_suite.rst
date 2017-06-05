Test Suite
##############################################################################

.. contents:: Contents
  :local:

Structure
==============================================================================

.. code-block:: none
      
  └── tests/
      ├── general/
      │   ├── management/
      │   ├── templatetags/
      │   ├── urls/
      │   └── views/
      ├── resources/
      │   ├── loaders/
      │   ├── models/
      │   ├── resource/
      │   ├── urls/
      │   ├── views/
      │   └── ResourcesTestDataGenerator.py
      ├── topics/
      │   ├── loaders/
      │   │   └── assets/
      │   ├── models/
      │   ├── urls/
      │   ├── views/
      │   └── TopicsTestDataGenerator.py
      ├── utils
      │   └── errors/
      ├── BaseTest.py
      └── BaseTestWithDB.py
