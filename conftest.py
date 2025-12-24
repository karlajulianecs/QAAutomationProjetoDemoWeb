import pytest
from utils.driver_factory import get_driver


def pytest_addoption(parser):
    parser.addoption(
        "--browser",
        action="store",
        default="chrome",
        help="Browser para execução: chrome, firefox ou safari"
    )

@pytest.fixture(scope="function")
def driver(request):
    browser = request.config.getoption("--browser")

    driver = get_driver(browser)
    yield driver

    driver.quit()