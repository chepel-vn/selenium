from fixtures.pages.registration import RegistrationPage


class Application:
    def __init__(self, driver, url):
        self.driver = driver
        self.url = url
        self.registration = RegistrationPage(self)

    def quit(self):
        self.driver.quit()

    def open_page(self):
        self.driver.get(self.url)
