"""Helper functions and variables for the running of the in-browser tests."""

import os

TITLE_ERROR_TEXT = "Failed to load page\nExpected title = {}, got {}"
URL_ERROR_TEXT = "Failed to load page\nExpected url = {}, not {}"
LANG_SELECTOR_ERROR_TEXT = "Language selector failed.\nExpected {}, got {}"

LOCAL_URL = "http://localhost/en/"
LIVE_URL = "https://csunplugged.org/en/"

BASE_URL = None
CAPABILITIES = None

CAP_LIST = [
    {
        "os": "Windows",
        "os_version": "10",
        "browser": "Chrome",
        "browser_version": "61.0",
        "resolution": "1920x1080"
    },
    {
        "os": "Windows",
        "os_version": "10",
        "browser": "Chrome",
        "browser_version": "62.0",
        "resolution": "1920x1080"
    },
    {
        "os": "Windows",
        "os_version": "10",
        "browser": "Chrome",
        "browser_version": "63.0",
        "resolution": "1920x1080"
    }
]

DEV_TESTING_ON_LIVE_SERVER_CAPABILITIES = {
    'os': 'Windows',
    'os_version': '10',
    'browser': 'Chrome',
    'browser_version': '63.0',
    'resolution': '1920x1080'
}

DEV_TESTING_PARAMETERIZATION_TEST_CAPABILITIES = {
    'os': 'Windows',
    'os_version': '10',
    'browser': 'Chrome',
    'browser_version': '62.0',
    'resolution': '1920x1080'
}

TRAVIS_BUILD_CAPABILITIES = {
    'os': 'Windows',
    'os_version': '10',
    'browser': 'Chrome',
    'browser_version': '63.0',
    'resolution': '1920x1080',
    'browserstack.local': 'true'
}

try:
    ACCESS_KEY = os.environ['KEY']
    BASE_URL = LOCAL_URL
    CAPABILITIES = TRAVIS_BUILD_CAPABILITIES
except KeyError:
    with open('local_browser_testing.txt', "r") as f:
        ACCESS_KEY = f.readline()
    BASE_URL = LIVE_URL

    CAPABILITIES = DEV_TESTING_ON_LIVE_SERVER_CAPABILITIES
    pass

COMMAND_EXECUTOR = 'http://cseducationresea1:' + ACCESS_KEY + '@hub.browserstack.com:80/wd/hub'

language_dict = {
    'en': 'English',
    'de': 'Deutsch',
    'es': 'Español',
    'mi': 'Te Reo Māori',
    'zh-hans': '简体中文'
}


def check_title_and_url(driver, expected_title, expected_url):
    """Check that the title and url are correct."""
    if driver.title != expected_title:
        raise Exception(TITLE_ERROR_TEXT.format(expected_title, driver.title))
    if driver.current_url != expected_url:
        raise Exception(URL_ERROR_TEXT.format(expected_url, driver.current_url))


def load_home_page(driver):
    """Load the base url and checks the title is correct."""
    driver.get(BASE_URL)
    if driver.title != "CS Unplugged":
        raise Exception(TITLE_ERROR_TEXT.format(driver.title, "CS Unplugged"))
    hide_dev_toolbar(driver)


def load_page(driver, path):
    """Load the desired url excluding the base url."""
    driver.get(BASE_URL + path)
    hide_dev_toolbar(driver)


def hide_dev_toolbar(driver):
    """Hide the tool bar if the test has been run in developer mode, ie it has been run locally."""
    if BASE_URL == LOCAL_URL:
        driver.find_element_by_id("djHideToolBarButton").click()


def change_language(driver, lang_code):
    """Change the language to the language code given."""
    driver.find_element_by_id("navbarLanguageSelector").click()
    driver.find_element_by_link_text(language_dict[lang_code]).click()
    lang_value = driver.find_element_by_tag_name("html").get_attribute("lang")
    if lang_value != lang_code:
        raise Exception(LANG_SELECTOR_ERROR_TEXT.format(lang_code, lang_value))