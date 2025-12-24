import platform
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService


def get_driver(browser="chrome"):
    browser = browser.lower()

    # FIREFOX
    if browser == "firefox":
        from selenium.webdriver.firefox.service import Service as FirefoxService
        from webdriver_manager.firefox import GeckoDriverManager

        return webdriver.Firefox(
            service=FirefoxService(GeckoDriverManager().install())
        )

    # SAFARI
    if browser == "safari":
        if platform.system() != "Darwin":
            raise RuntimeError("Safari só é suportado no macOS")
        return webdriver.Safari()

    # CHROME (Homebrew)
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")

    service = ChromeService(
        executable_path="/opt/homebrew/bin/chromedriver"
    )

    return webdriver.Chrome(
        service=service,
        options=options
    )