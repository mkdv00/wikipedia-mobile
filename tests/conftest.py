import os
import pytest
from appium import webdriver
from dotenv import load_dotenv
from selene.support.shared import browser
from appium.options.android import UiAutomator2Options
from wikipedia_app.utils.attachment import screenshot, screen_xml_dump, video_from_browserstack


load_dotenv()


@pytest.fixture(scope='function', autouse=True)
def app_config():
    options = UiAutomator2Options().load_capabilities({
        "platformName": "android",
        "platformVersion": "9.0",
        "deviceName": "Google Pixel 3",
        "app": os.getenv('APP'),
        'bstack:options': {
            "projectName": "Wikipedia mobile project",
            "buildName": "browserstack-build-DEMO",
            "sessionName": "BStack first_test",
            "userName": os.getenv('USER_NAME'),
            "accessKey": os.getenv('KEY')
        }
    })
    browser.config.driver = webdriver.Remote(os.getenv('BROWSERSTACK_HUB'), options=options)

    yield

    screenshot()
    screen_xml_dump()
    session_id = browser.driver.session_id
    browser.quit()
    browser.config.timeout = 10

    video_from_browserstack(session_id)
