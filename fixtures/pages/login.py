from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement


class LoginPage:
    def __init__(self, app):
        self.webdriver = app.driver

    def _password_input(self) -> WebElement:
        return self.webdriver.find_element(By.ID, "password")

    def _login_input(self) -> WebElement:
        return self.webdriver.find_element(By.ID, "username")

    def _submit_button(self) -> WebElement:
        return self.webdriver.find_element(By.ID, "loginbtn")

    def auth(self, login: str, password: str):
        self._login_input().send_keys(login)
        self._password_input().send_keys(password)
        self._submit_button().click()
        print(f"Login is {login}, password is {password}")
