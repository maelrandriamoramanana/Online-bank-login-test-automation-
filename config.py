import os 
from dotenv import load_dotenv

load_dotenv()

class Config:
    BASE_URL = os.getenv("BASE_URL", "https://qaplayground.com")
    TIMEOUT = int(os.getenv("TIMEOUT", 3000))

    BROWSER = os.getenv("BROWSER", "chromium")
    HEADLESS = os.getenv("HEADLESS", "False").lower() == "true"

    STANDARD_USER = os.getenv("STANDARD_USER", "standard_user")
    STANDARD_PASS = os.getenv("STAND_PWD", "bank_sauce")

    LOCKED_USER = os.getenv("LOCKED_USER", "locked_user")
    LOCKED_PASS = os.getenv("LOCKED_PWD", "bank_sauce")

    FAILED_USER = os.getenv("FAILED", "Inexistant_user")
    FAILED_PWD = os.getenv("FAILED_PWD", "Impossible")