from selene.support.shared import browser
from appium.webdriver.common.appiumby import AppiumBy


def article(article_number: int):
    return browser.all((AppiumBy.ID, 'org.wikipedia.alpha:id/page_list_item_title'))[article_number]
