import pytest
import allure


@allure.epic('Web Application')
@allure.feature('System access')
@allure.story('Authorization')
@allure.title("Login failure")
@allure.description('User enter invalid credentials and system display error message')
@allure.severity('allure.severity_level.CRITICAL')
def test_login_failure_user_invalid_credentials(login_page):
    with allure.step('Open login page'):
        login_page.navigate()
    with allure.step('User enter invalid credentials'):
        login_page.login("invalid_username", "invalid_password")
    with allure.step('User sees error message when invalid credentials are entered'):
        assert login_page.get_error_message() == 'Invalid credentials. Please try again.'


@allure.title("Login success")
@allure.description('User enter valid credentials and system display welcome message')
@allure.severity('allure.severity_level.CRITICAL')
@pytest.mark.parametrize('username, password', [
    ("user", "user"),
    ("admin", "admin"),
])
def test_login_success(login_page, dashboard_page, username, password):
    with allure.step('Open login page'):
        login_page.navigate()
    with allure.step('User enter valid credentials'):
        login_page.login(username, password)

    with allure.step('User sees welcome message'):
        dashboard_page.assert_welcome_message(f'Welcome {username}')
