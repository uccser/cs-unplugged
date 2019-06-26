from selenium import webdriver
import time
import os

ACCESS_KEY = os.environ['KEY']
COMMAND_EXECUTOR = 'http://cseducationresea1:' + ACCESS_KEY + '@hub.browserstack.com:80/wd/hub'

v1 = {
    'os_version': '10',
    'browser': 'Chrome',
    'browser_version': '60.0',
    'resolution': '1920x1080',
    'browserstack.local': 'true',
    # 'browserstack.selenium_version': '3.5.2',
    # 'browserstack.localIdentifier': os.environ['BROWSERSTACK_LOCAL_IDENTIFIER']
}

v2 = {
    'os_version': '10',
    'browser': 'Chrome',
    'browser_version': '61.0',
    'resolution': '1920x1080',
    'browserstack.local': 'true',
    # 'browserstack.selenium_version': '3.5.2',
    # 'browserstack.localIdentifier': os.environ['BROWSERSTACK_LOCAL_IDENTIFIER']
}

v3 = {
    'os_version': '10',
    'browser': 'Chrome',
    'browser_version': '62.0',
    'resolution': '1920x1080',
    'browserstack.local': 'true',
    # 'browserstack.selenium_version': '3.5.2',
    # 'browserstack.localIdentifier': os.environ['BROWSERSTACK_LOCAL_IDENTIFIER']
}

local_server = {
    'os_version': '10',
    'browser': 'Chrome',
    'browser_version': '63.0',
    'resolution': '1920x1080',
    'browserstack.local': 'true',
    # 'browserstack.selenium_version': '3.5.2',
    # 'browserstack.localIdentifier': os.environ['BROWSERSTACK_LOCAL_IDENTIFIER']
}


# def test_trial():
#     driver = webdriver.Remote(
#         command_executor=COMMAND_EXECUTOR,
#         desired_capabilities=v1)
#
#     driver.get("https://csunplugged.org/en/")
#     if "CS Unplugged" not in driver.title:
#         raise Exception("Unable to load Cs unplugged page!")
#     driver.quit()
#
#
# def test_trial_15():
#     driver = webdriver.Remote(
#         command_executor=COMMAND_EXECUTOR,
#         desired_capabilities=v2)
#
#     driver.get("https://csunplugged.org/en/")
#     if "CS Unplugged" not in driver.title:
#         raise Exception("Unable to load Cs unplugged page!")
#     driver.quit()
#
#
# def test_trial2():
#     driver = webdriver.Remote(
#         command_executor=COMMAND_EXECUTOR,
#         desired_capabilities=v3)
#
#     driver.get("https://csunplugged.org/en/")
#     driver.find_element_by_xpath(
#         "(.//*[normalize-space(text()) and normalize-space(.)='Topics'])").click()
#     time.sleep(3)
#     if "Topics" not in driver.title:
#         raise Exception("Unable to load CS unplugged page!")
#     driver.quit()


def test_local():
    driver = webdriver.Remote(
        command_executor=COMMAND_EXECUTOR,
        desired_capabilities=local_server)

    driver.get("http://localhost/en")
    element = driver.title
    if "CS Unplugged" not in element.text:
        raise Exception("Unable to load local page!")
    driver.quit()


def test_local_2():
    driver = webdriver.Remote(
        command_executor=COMMAND_EXECUTOR,
        desired_capabilities=local_server)

    driver.get("http://localhost/en/topics/searching-algorithms/")
    element = driver.title
    if "Searching Algorithms - CS Unplugged" not in element.text:
        raise Exception("Unable to load local page!")
    driver.quit()
