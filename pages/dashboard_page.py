from playwright.sync_api import Page
from config import Config

class DashboardPage:
    def __init__(self, page:  Page):
        super().__init__(page)
        self.welcome_message = page.get_by_text("welcome back")

    def is_message_visible(self, timeout = 5000):
        return self.is_element_visible(self.welcome_message, timeout)