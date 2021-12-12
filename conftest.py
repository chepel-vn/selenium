import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from fixtures.pages.application import Application


def pytest_addoption(parser):
    parser.addoption(
        "--url",
        action="store",
        default="https://qacoursemoodle.innopolis.university/login/signup.php?",
        help="Moodle url",
    )


@pytest.fixture()
def app(request):
    url = request.config.getoption("--url")
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.maximize_window()
    app = Application(driver, url)
    yield app
    app.quit()
