#  Bank Login Page Test Automation

Automated testing framework for a online banking login page, built with **Python**, **Playwright**, and **Pytest**, following the **Page Object Model (POM)** design pattern. 

---

##  Tech Stack
* **Language:** Python 3.x
* **Automation Tool:** Playwright (Python)
* **Test Runner:** Pytest
* **Design Pattern:** Page Object Model (POM)
* **Reporting:** Allure Reports (with automatic screenshots on failure)
* **Configuration:** Environment variables (".env")

---

## Project Structure
Bank-login-Page-test-automation/
│
├── pages/
│   ├── __init__.py
│   └── login_page.py       # Page Object containing locators and actions
│
├── tests/
│   ├── __init__.py
│   └── test_login.py       # Test cases
│
├── .env                    # Credentials & URLs (ignored by git)
├── .gitignore              # Made to hide the .env file in git
├── conftest.py             # Fixtures, browser setup & Allure hooks
└── requirements.txt        # Project dependencies to install before launching the program