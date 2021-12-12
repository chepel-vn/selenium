from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement


class RegistrationPage:
    def __init__(self, app):
        self.webdriver = app.driver

    def _username_input(self) -> WebElement:
        return self.webdriver.find_element(By.ID, "id_username")

    def _password_input(self) -> WebElement:
        return self.webdriver.find_element(By.ID, "id_password")

    def _email_input(self) -> WebElement:
        return self.webdriver.find_element(By.ID, "id_email")

    def _email2_input(self) -> WebElement:
        return self.webdriver.find_element(By.ID, "id_email2")

    def _firstname_input(self) -> WebElement:
        return self.webdriver.find_element(By.ID, "id_firstname")

    def _lastname_input(self) -> WebElement:
        return self.webdriver.find_element(By.ID, "id_lastname")

    def _city_input(self) -> WebElement:
        return self.webdriver.find_element(By.ID, "id_city")

    def _country_input(self) -> WebElement:
        return self.webdriver.find_element(By.ID, "id_country")

    def _submit_button(self) -> WebElement:
        return self.webdriver.find_element(By.ID, "id_submitbutton")

    def register(
        self,
        username: str,
        password: str,
        email: str,
        email2: str,
        firstname: str,
        lastname: str,
        city: str,
        country: str,
    ):
        self._username_input().send_keys(username)
        self._password_input().send_keys(password)
        self._email_input().send_keys(email)
        self._email2_input().send_keys(email2)
        self._firstname_input().send_keys(firstname)
        self._lastname_input().send_keys(lastname)
        self._city_input().send_keys(city)
        self._country_input().send_keys(country)
        self._submit_button().click()
        print(
            f"Registration is '{username}', "
            f"password is '{password}', "
            f"email is {email} "
            f"email2 is {email2} "
            f"firstname is {firstname} "
            f"lastname is {lastname} "
            f"city is {city} "
            f"country is {country} "
        )
