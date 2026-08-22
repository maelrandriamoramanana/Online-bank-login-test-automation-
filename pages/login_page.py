from playwright.sync_api import Page
from pages.base_page import BasePage

class LoginPage(BasePage):
    def __init__(self, page : Page):
        super().__init__(page)

        self.username_input = self.page.get_by_test_id("login-username-input")
        self.password_input = self.page.get_by_test_id("login-password-input")
        self.submit_btn = self.page.get_by_test_id("login-submit-btn")

    def open(self):
        self.navigate("/bank/login")

    def login(self, username, password):
        self.username_input.fill(username)
        self.password_input.fill(password)
        self.submit_btn.click()