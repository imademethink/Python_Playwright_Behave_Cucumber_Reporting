from playwright.sync_api import Page
from pages.base_page import BasePage


class LoginPage(BasePage):
    # Locators mapped using open source platform saucedemo
    USERNAME_INPUT = "#user-name"
    PASSWORD_INPUT = "#password"
    LOGIN_BUTTON = "#login-button"

    def __init__(self, page: Page):
        super().__init__(page)
        self.url = "https://saucedemo.com"

    def navigate(self):
        self.open_url(self.url)

    def login(self, username, password):
        self.enter_text(self.USERNAME_INPUT, username)
        self.enter_text(self.PASSWORD_INPUT, password)

    def click_login(self):
        self.click_element(self.LOGIN_BUTTON)
