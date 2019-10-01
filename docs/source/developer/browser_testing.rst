Browser testing
##############################################################################

.. contents:: Contents
  :local:


Setup
==============================================================================

Before the test suite will function it is necessary to complete some imports into the ``in_browser/`` directory.

Enter the following into the terminal:

``pip install selenium``

``pip install django.test``

For testing outside the Travis build it is also necessary to create a file named ``local_browser_testing.txt`` inside the ``in_browser/`` directory.
This file provides the BrowserStack Access Key read during runtime. If you don't have the access key handy, visit `BrowserStack <https://automate.browserstack.com>`_,
login, and click "show +" at the top left of the window.

Save this key in plain text on the first line and save.
MAKE SURE TO ADD THIS FILE TO GITIGNORE. This can be done by right clicking the file in the project window. The file's text should turn a mossy colour if completed correctly. This will prevent the key being visible to everyone on Git.

.. note::

    If you do expose the Access Key then it can be reset using the BrowserStack API.
    You can find info on this `here`_.


.. _here: https://www.browserstack.com/automate/reset-access-key

Structure
==============================================================================

All related browser testing files are in the ``tests/topics/in_browser/`` directory, which in the ``csfieldguide/`` directory (at the same level as the apps).
It is structured as follows:

.. code-block:: none

  └── in_browser/
      ├── BaseBrowserTest.py
      ├── browserstack_local_commands.txt
      ├── capabilities.json
      ├── local_browser_testing.txt (Untracked)
      ├── run_browser_test.py
      ├── setup_config.py
      └── test_*.py

Items of interest from this diagram:

- ``BaseBrowserTest.py`` - this class inherits the ``unittest.TestCase`` class, and performs the setup and teardown operations required for the Selenium web driver and the capabilities used for testing.
  This is the base test class that all other browser tests should inherit from.
  It also contains a method named "load_page" which should be called at the beginning of most tests.

- ``browserstack_local_commands.txt`` - contains the commands necessary for running the BrowserStack local binary.
  This file allows for BrowserStack to access servers running on localhost.


- ``capabilities.json`` - contains the BrowserStack capabilities for the browser versions, os, local testing, and other settings.
  Information on the capabilities available can be found on their `web page <https://www.browserstack.com/automate/capabilities>`_.

- ``local_browser_testing.txt`` - contains the BrowserStack Access key required for the selenium tests to be completed on the remote device.
  This should not be pushed to the repository.

- ``run_browser_test.py`` - contains the code to perform the multi-threading required to run an instance of a test for each set of capabilities.
  Bear in mind these threads may be limited by the amount provided by the BrowserStack plan.

- ``setup_config.py`` - acts as the entrance point for the environment variables required by the suite.
  The variables provided determine which state the tests will run in. See the section on `Running tests`_ for more info.


Adding tests
==============================================================================

Examine the existing tests to gain an understanding of how to extend the base test class.
Most of the hard work is completed under the hood already but there are some important points to note:

- Make use of the load_page method provide by the base class at the beginning of each test unless specifically not required.
  This method closes the developer window that is loaded with the web page due to it's local launch.
  It can also be used to pass extra parameters. Be sure to set the URL variable in the child class if you wish to use this method.

- Each selenium operation such as finding single elements takes around 0.3 seconds so be conservative! This time will add up!
  Make use of the in-built selenium driver methods like "find_elements_by_class_name" to select multiple elements in the same time.

- The ActionChains module provided within the selenium.webdriver package can be used for complex operations like drag-and-drops.
  This is particularly useful for testing interactive elements.


Running tests
==============================================================================

The suite has many features that allow you to run the tests in different ways.
This allows for only the desired tests to be run to save time.
It takes around 8 minutes to just launch the website locally within the travis build so these other options can be very useful when used correctly.

Firstly, the tests can be run on a server you have started locally or on the currently live server.
This provides the following advantages:

- Live server: Quick and easy as you don't have to launch the website and BrowserStack binary locally. This is only useful when you are adding new tests to existing live features.

- Local server: Local changes on your current branch will be testable.

This option can be manipulated by changing the TEST_ON_LIVE_SERVER variable in the ``setup_config.py`` file.
Setting this value to True (to enable live testing) will have no effect on the Travis build.
However it is important to remember this variable will enable/disable local changes and may be the reason your tests are suddenly failing.

There are also two ways tests can be launched manually:

- Method/Class/File: Just like a regular unit test the tests can be launched from any of these places.
  This will only run the test using the first capability dictionary in the ``capabilities.json`` file.

- Command line (All capabilities in parallel): This will simulate how Travis will run the tests and print the results to the command line.
  This can be done using the command from inside the ``in_browser/`` directory:

  ``python3 run_browser_tests.py capabilities.json``

  Unlike the Travis build this WILL be affected by the TEST_ON_LIVE_SERVER variable.

The tests will be run through Travis when the code is pushed to Git.

Understanding the results
==============================================================================

Any failing tests will be displayed in the terminal or within Travis depending on where they were launched.
Any Selenium errors can be tracked back to the source using the debug information provided. This will contain the capabilities that the test were run on.
By matching these capabilities and the name of the test you will be able to locate the test on BrowserStack where the error resulted.

.. note::
  BrowserStack provides a recording of the test being carried out which is extremely useful for understanding the test result.
  You should check this recording and the listed web interactions it records beneath to confirm the test was completed as expected.


Selenium
==============================================================================

Provides the browser testing framework used for the web page interactions.
Check out their extensive `documentation <https://seleniumhq.github.io/selenium/docs/api/py/api.html>`_ for more information.


BrowserStack
==============================================================================

Provides the devices to remotely test the given capabilities.
Check out their extensive `docs <https://www.browserstack.com/docs>`_ for more information.






















sdfdsf
