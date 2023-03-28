import allure

from wikipedia_app.data import search_data, user
from wikipedia_app.models import app


@allure.label('owner', 'Kudaev.m')
@allure.title('Test search')
def test_search_successfully():
    app.given_opened()

    with allure.step('Make search request'):
        app.open_search_page()
        app.wikipedia_search(text=search_data.search_text)
        app.check_wikipedia_search(text=search_data.expected_search_text)


@allure.label('owner', 'Kudaev.m')
@allure.title('Test open article')
def test_open_article():
    app.given_opened()

    with allure.step('Search for Python article'):
        app.wikipedia_search(text=search_data.search_text)
        app.check_wikipedia_search(text=search_data.expected_search_text)

    with allure.step('Open first article'):
        app.article_open(article_number=0)
        app.check_article_open(text=search_data.expected_article_description)


@allure.label('owner', 'Kudaev.m')
@allure.title('Test open article categories')
def test_open_article_categories():
    app.given_opened()

    with allure.step('Search for Python article'):
        app.wikipedia_search(text=search_data.search_text)
        app.check_wikipedia_search(text=search_data.expected_search_text)

    with allure.step('Open second article'):
        app.article_open(article_number=1)

    with allure.step('Open article categories'):
        app.open_article_categories()
        app.check_categories_title()


@allure.label('owner', 'Kudaev.m')
@allure.title('Test login with incorrect data')
def test_login_with_invalid_data():
    app.given_opened()

    with allure.step('Open saved page'):
        app.open_saved_page()
        app.check_page_title(text='Saved')

    with allure.step('Login with incorrect data'):
        app.open_login_form()
        app.fill_login_form(
            username=user.fake_username,
            password=user.fake_password
        )
        app.submit_form()

    with allure.step('Check for login with incorrect data'):
        app.check_login_with_incorrect_data()


@allure.label('owner', 'Kudaev.m')
@allure.title('Test login successfully')
def test_login_successfully():
    app.given_opened()

    with allure.step('Open saved page'):
        app.open_saved_page()
        app.check_page_title(text='Saved')

    with allure.step('Login with correct data'):
        app.open_login_form()
        app.fill_login_form(
            username=user.username,
            password=user.password
        )
        app.submit_form()

    with allure.step('Check user has been logged'):
        app.check_saved_articles_after_login()
