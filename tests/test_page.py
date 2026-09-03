import pytest
import pytest_check as check
from config import Config
from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage

user_to_test = [
    (Config.STANDARD_USER, Config.STANDARD_PASS, True),
    (Config.LOCKED_USER, Config.LOCKED_PASS, False),
    (Config.FAILED_USER, Config.FAILED_PASS, False)
]

@pytest.mark.parametrize("username, password, should_succeed", user_to_test)
def test_login_scenarios(page, username, password, should_succeed):
    login_page = LoginPage(page)
    dashboard_page = DashboardPage(page)

    login_page.open()

    check.is_true(login_page.is_element_visible(login_page.username_input), "Username input should be visible")
    check.is_true(login_page.is_element_visible(login_page.password_input), "Password input should be visible")

    login_page.login(username, password)

    if should_succeed:
        page.wait_for_url("**/bank/dashboard", timeout = 5000)
        check.is_true(dashboard_page.is_message_visible(), f"Failed to log in with:{username}")
    else:
        check.is_true("dashboard" not in login_page.get_current_url(), f"Unauthorized acces for user: {username}")