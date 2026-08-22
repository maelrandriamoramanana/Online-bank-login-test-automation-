import pytest
import pytest_check as check
from pages.login_page import LoginPage
from config import Config

user_to_test = [
    (Config.STANDARD_USER, Config.STANDARD_PASS, True),
    (Config.LOCKED_USER, Config.LOCKED_PASS, False),
    (Config.FAILED_USER, Config.FAILED_PWD, True)
]

@pytest.mark.parametrize("username, password, should_succeed", user_to_test)
def test_successful_login(page, username, password, should_succeed):
    login_page = LoginPage(page)

    login_page.open()

    #this line of code makes the program wait for the username input to be visible before continuing the test
    login_page.username_input.wait_for(state="visible", timeout=5000)

    check.is_true(login_page.username_input.is_visible(), "Le champ username n'est pas visible")
    check.is_true(login_page.password_input.is_visible(), "Le champ password n'est pas visible")

    login_page.login(username,password)

    #This condition line makes the progran accept the test as success only when the text "welcome back" is visible on the page
    if should_succeed:
        page.wait_for_url("**/bank/dashboard", timeout=5000)
        check.is_true(page.get_by_text("Welcome back").is_visible(),f"Echec de connexion pour {username}")

    else:
        check.is_true("dashboard" not in login_page.get_current_url(),f"Le compte bloqué n'aurait pas dû accéder au dashboard : {username}")