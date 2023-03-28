from selene import be, have
from selene.support.shared import browser
from appium.webdriver.common.appiumby import AppiumBy
from wikipedia_app.models.controls.article import article


def given_opened():
    skip_button_id = 'org.wikipedia.alpha:id/fragment_onboarding_skip_button'
    wikipedia_title_id = 'org.wikipedia.alpha:id/main_toolbar_wordmark'

    if browser.element((AppiumBy.ID, skip_button_id)).matching(be.visible):
        browser.element((AppiumBy.ID, skip_button_id)).click()
        # Check wikipedia title
        browser.element((AppiumBy.ID, wikipedia_title_id)).should(be.visible)


def open_search_page():
    search_page_xpath = '//android.widget.FrameLayout[@content-desc="Search"]/android.widget.FrameLayout'
    browser.element((AppiumBy.XPATH, search_page_xpath)).click()


def wikipedia_search(text: str):
    search_wikipedia_id = 'org.wikipedia.alpha:id/search_src_text'
    browser.element((AppiumBy.ACCESSIBILITY_ID, 'Search Wikipedia')).click()
    browser.element((AppiumBy.ID, search_wikipedia_id)).type(text)


def check_wikipedia_search(text: str):
    article(article_number=0).should(have.text(text))


def article_open(article_number: int):
    article(article_number=article_number).click()
    web_view_popup_id = 'org.wikipedia.alpha:id/page_web_view'
    browser.element((AppiumBy.ID, web_view_popup_id)).click()


def check_article_open(text: str):
    article_desc_xpath = '//android.webkit.WebView/android.view.View/android.view.View[1]/android.view.View[2]'
    browser.element((AppiumBy.XPATH, article_desc_xpath)).should(have.text(text))


def open_saved_page():
    saved_page_xpath = '//android.widget.FrameLayout[@content-desc="Saved"]/android.widget.FrameLayout'
    browser.element((AppiumBy.XPATH, saved_page_xpath)).click()


def check_page_title(text: str):
    title_xpath = '//*[@resource-id="org.wikipedia.alpha:id/main_toolbar"]/android.widget.TextView'
    browser.element((AppiumBy.XPATH, title_xpath)).should(have.text(text))


def open_login_form():
    join_wikipedia_button_id = 'org.wikipedia.alpha:id/positiveButton'
    browser.element((AppiumBy.ID, join_wikipedia_button_id)).click()

    create_account_login_button_id = 'org.wikipedia.alpha:id/create_account_login_button'
    browser.element((AppiumBy.ID, create_account_login_button_id)).click()


def fill_login_form(username: str, password: str):
    username_input_xpath = '//*[@resource-id="org.wikipedia.alpha:id/login_username_text"]//android.widget.EditText'
    browser.element((AppiumBy.XPATH, username_input_xpath)).type(username)

    password_input_xpath = '//*[@resource-id="org.wikipedia.alpha:id/login_password_input"]//android.widget.EditText'
    browser.element((AppiumBy.XPATH, password_input_xpath)).type(password)


def submit_form():
    login_button_id = 'org.wikipedia.alpha:id/login_button'
    browser.element((AppiumBy.ID, login_button_id)).click()


def check_snack_bar_text(text: str):
    snack_bar_id = 'org.wikipedia.alpha:id/snackbar_text'
    browser.element((AppiumBy.ID, snack_bar_id)).should(have.text(text))


def check_login_with_incorrect_data():
    login_form_xpath = '//*[@resource-id="org.wikipedia.alpha:id/action_bar"]/android.widget.TextView'
    browser.element((AppiumBy.XPATH, login_form_xpath)).should(have.text('Log in'))


def check_saved_articles_after_login():
    saved_description_id = 'org.wikipedia.alpha:id/item_description'
    browser.element((AppiumBy.ID, saved_description_id)).should(have.text('Default list for your saved articles'))


def open_article_categories():
    more_options_button_xpath = '//android.widget.ImageView[@content-desc="More options"]'
    browser.element((AppiumBy.XPATH, more_options_button_xpath)).click()

    categories_button_id = 'org.wikipedia.alpha:id/page_categories'
    browser.element((AppiumBy.ID, categories_button_id)).click()


def check_categories_title():
    categories_title_id = 'org.wikipedia.alpha:id/categories_dialog_title'
    browser.element((AppiumBy.ID, categories_title_id)).should(have.text('Categories'))
