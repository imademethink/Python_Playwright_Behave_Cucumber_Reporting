from playwright.sync_api import Page, expect


class BasePage:
    def __init__(self, page: Page):
        self.page = page
        self.URL = "https://parabank.parasoft.com/parabank/index.htm"
        self.hm_global_data = {}

    def open_url(self, url):
        self.page.goto(url)

    def find_element(self, locator):
        element = self.page.locator(locator)
        expect(element).to_be_visible(timeout=10000)
        return element

    def element_is_present(self, locator, idx=0):
        element = self.page.locator(locator).nth(idx)
        expect(element).to_be_attached(timeout=10000)
        return element

    def click_element(self, locator):
        self.find_element(locator).click()

    def enter_text(self, locator, text):
        element = self.find_element(locator)
        element.fill(text)

    def get_current_url(self):
        return self.page.url

    def get_element_text(self, locator, idx=0):
        element = self.find_element(locator).nth(idx)
        # return element.inner_text()
        return element.text_content()
