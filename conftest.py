import pytest
from playwright.sync_api import sync_playwright
import allure
from config import Config

@pytest.fixture(scope="function")
def page():

    with sync_playwright() as p:
        browser_type = getattr(p, Config.BROWSER)
        browser = browser_type.launch(headless= Config.HEADLESS, slow_mo = 1000)

        context = browser.new_context()
        page = context.new_page()
        page.set_default_timeout(Config.TIMEOUT)

        yield page

        context.close()
        browser.close()

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:
        page = item.funcargs.get("page", None)
        if page:
            screenshot_bytes = page.screenshot(full_page=True)
            allure.attach(
                screenshot_bytes,
                name=f"Echec_{item.name}",
                attachment_type=allure.attachment_type.PNG
            )
            print(f"\n[ALLURE]Capture d'ecran attachee pour le test: {item.name}")