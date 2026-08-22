from playwright.sync_api import Page
from config import Config

class BasePage:
    def __init__(self, page: Page):
        self.page = page

    def navigate(self, endpoint =""):
        url = f"{Config.BASE_URL}{endpoint}"
        self.page.goto(url)

    def get_current_url(self):
        return self.page.url