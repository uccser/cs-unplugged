import os

TITLE_ERROR_TEXT = "Failed to load page\nExpected title = {}, got {}"
URL_ERROR_TEXT = "Failed to load page\nExpected url = {}, not {}"

ACCESS_KEY = os.environ['KEY']
COMMAND_EXECUTOR = 'http://cseducationresea1:' + ACCESS_KEY + '@hub.browserstack.com:80/wd/hub'

local_server = {
    'os': 'Windows',
    'os_version': '10',
    'browser': 'Chrome',
    'browser_version': '63.0',
    'resolution': '1920x1080',
    'browserstack.local': 'true'
}


def check_title_and_url(driver, expected_title, expected_url):
    if driver.title != expected_title:
        raise Exception(TITLE_ERROR_TEXT.format(expected_title, driver.title))
    if driver.current_url != expected_url:
        raise Exception(URL_ERROR_TEXT.format(expected_url, driver.current_url))


def load_home_page(driver):
    driver.get("http://localhost/en")
    if driver.title != "CS Unplugged":
        raise Exception(TITLE_ERROR_TEXT.format(driver.title, "CS Unplugged"))
