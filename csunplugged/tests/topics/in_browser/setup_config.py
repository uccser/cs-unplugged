"""Performs the collection of the BrowserStack access key, testing capabilities, and URL config."""

import os

# ---------- DISABLE FOR DEV TESTING ON LOCALLY ACTIVE SITE --------- #
TEST_ON_LIVE_SITE = True
# ---------- DISABLE FOR DEV TESTING ON LOCALLY ACTIVE SITE --------- #

LOCAL_URL = "http://localhost/en/"   # Used for travis build and local dev servers.
LIVE_URL = "https://www.csunplugged.org/en/"

BASE_URL = None
TRAVIS_LAUNCH = False

# Gathers the BrowserStack access key from env variables or local file.
# Testing URLs are then allocated accordingly.
try:
    ACCESS_KEY = os.environ['KEY']
    BASE_URL = LOCAL_URL
    TRAVIS_LAUNCH = True
except KeyError:
    # Handle whether tests run from in class or by run_browser_tests file.
    internal_test_launch = os.getenv('JSONFILE', None) is None
    if internal_test_launch:
        BS_access_file = 'in_browser/local_browser_testing.txt'
    else:
        BS_access_file = 'local_browser_testing.txt'
    with open(BS_access_file, "r") as f:
        ACCESS_KEY = f.readline()
    if TEST_ON_LIVE_SITE:
        BASE_URL = LIVE_URL
    else:
        BASE_URL = LOCAL_URL
    pass

COMMAND_EXECUTOR = 'http://cseducationresea1:' + ACCESS_KEY + '@hub.browserstack.com:80/wd/hub'
