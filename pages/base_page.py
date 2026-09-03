from playwright.sync_api import Page, Locator, TimeoutError as PlaywrightTimeoutError
from config import Config

class BasePage:
    def __init__(self, page : Page):
        self.page = page

    def navigate(self, endpoint=""):
        url = f"{Config.BASE_URL}{endpoint}"
        self.page.goto(url)

    def get_current_url(self):
        return self.page.url

    def is_element_visible(self, locator: Locator, timeout = 5000) -> bool:
        try:
            locator.wait_for(state="visible", timeout = timeout)
            return True
        except PlaywrightTimeoutError:
            return False