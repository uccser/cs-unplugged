from selenium import webdriver
import time

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


def test_trial():
    driver = webdriver.Remote(
        command_executor='http://cseducationresea1:y1shw2Ck8GyVc53Y4LrT@hub.browserstack.com:80/wd/hub',
        desired_capabilities=v1)

    driver.get("https://csunplugged.org/en/")
    if "CS Unplugged" not in driver.title:
        raise Exception("Unable to load Cs unplugged page!")
    # assert(driver.title.contains("CS Unplugged"))
    driver.quit()


def test_trial_15():
    driver = webdriver.Remote(
        command_executor='http://cseducationresea1:y1shw2Ck8GyVc53Y4LrT@hub.browserstack.com:80/wd/hub',
        desired_capabilities=v2)

    driver.get("https://csunplugged.org/en/")
    if "CS Unplugged" not in driver.title:
        raise Exception("Unable to load Cs unplugged page!")
    print(driver.title)
    driver.quit()


def test_trial2():
    driver = webdriver.Remote(
        command_executor='http://cseducationresea1:y1shw2Ck8GyVc53Y4LrT@hub.browserstack.com:80/wd/hub',
        desired_capabilities=v3)

    driver.get("https://csunplugged.org/en/")
    driver.find_element_by_xpath(
        "(.//*[normalize-space(text()) and normalize-space(.)='Topics'])").click()
    time.sleep(3)
    if "Topics" not in driver.title:
        raise Exception("Unable to load CS unplugged page!")
    print(driver.title)
    driver.quit()


def test_local():
    driver = webdriver.Remote(
        command_executor='http://cseducationresea1:y1shw2Ck8GyVc53Y4LrT@hub.browserstack.com:80/wd/hub',
        desired_capabilities=local_server)

    driver.get("http://127.0.0.1:8000/polls/")
    element = driver.find_element_by_tag_name("a")
    if "what's up?" not in element.text:
        raise Exception("Unable to load local page!")
    print(element.text)
    driver.quit()


def test_browser_first():
    driver = webdriver.Remote(
        command_executor='http://cseducationresea1:y1shw2Ck8GyVc53Y4LrT@hub.browserstack.com:80/wd/hub',
        desired_capabilities=local_server)

    driver.get("localhost/en/search/?q=")
    driver.find_element_by_xpath(
        "(.//*[normalize-space(text()) and normalize-space(.)='Show all curriculum areas'])[1]/following::div[1]").click()
    driver.find_element_by_xpath(
        "(.//*[normalize-space(text()) and normalize-space(.)='Logic'])[2]/following::input[1]").click()
    element = driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Filter by curriculum areas'])[1]/following::span[1]")
    print(element.text)
    # if "what's up?" not in element.text:
    #     raise Exception("Unable to load local page!")

    driver.quit()
