import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    BASE_URL = os.getenv("BASE_URL", "https://qaplayground.com")
    TIMEOUT = int(os.getenv("TIMEOUT", 30000))

    BROWSER = os.getenv("BROWSER", "chromium")
    HEADLESS = os.getenv("HEADLESS", "False").lower() == "true"
    SLOW_MO = int(os.getenv("SLOW_MO", 1000))

    STANDARD_USER = os.getenv("STANDARD_USER")
    STANDARD_PASS = os.getenv("STANDARD_PWD")

    LOCKED_USER = os.getenv("LOCKED_USER")
    LOCKED_PASS = os.getenv("LOCKED_PWD")

    FAILED_USER = os.getenv("FAILED")
    FAILED_PWD = os.getenv("FAILED_PWD")