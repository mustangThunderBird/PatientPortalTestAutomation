import os
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from dotenv import load_dotenv
from utils.screenshot import screenshot_on_failure

# Load environment variables from .env
load_dotenv()

def pytest_addoption(parser):
    parser.addoption(
        "--browser",
        action="store",
        default=None,
        help="Browser to run tests on: chrome or firefox (default: both)"
    )

@pytest.fixture
def driver(request):
    browser = request.config.getoption("--browser")
    headless = os.getenv("HEADLESS", "true").lower() == "true"

    if not browser:  # default: run both via parametrize
        pytest.skip("No browser specified; use --browser=chrome or --browser=firefox")

    if browser == "chrome":
        options = ChromeOptions()
        if headless:
            options.add_argument("--headless=new")
        options.add_argument("--window-size=1920,1080")
        drv = webdriver.Chrome(options=options)

    elif browser == "firefox":
        options = FirefoxOptions()
        if headless:
            options.add_argument("--headless")
        options.add_argument("--width=1920")
        options.add_argument("--height=1080")
        drv = webdriver.Firefox(options=options)

    else:
        raise ValueError(f"Unsupported browser: {browser}")

    drv.implicitly_wait(5)
    yield drv
    drv.quit()


# Hook to capture screenshots on test failure
@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item):
    """
    PyTest hook to attach screenshots on test failure.
    Runs after each test and checks the result.
    """
    outcome = yield
    rep = outcome.get_result()

    if rep.when == "call" and rep.failed:  # only capture on test execution phase
        driver = item.funcargs.get("driver")
        if driver:
            screenshot_on_failure(driver, item.name)
