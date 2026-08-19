from playwright.sync_api import Page
from pages.base_page import BasePage


class HomePage(BasePage):
    Txtbx_User = "[name='username']"
    Txtbx_Pwd = "[name='password']"
    Btn_LogIn = "//input[@value='Log In']"
    Link_Solutions = "//*[text()='Solutions']"
    Link_AboutUs = "//*[text()='About Us']"
    Link_Services = "//*[text()='Services']"
    Link_Products = "//*[text()='Products']"
    Link_Locations = "//*[text()='Locations']"
    Icon_Home = ".home"
    Icon_AboutUs = ".aboutus"
    Icon_Contact = ".contact"
    Lnk_Register = "//*[text()='Register']"
    Btn_Register = "input[value='Register']"

    main_menu_items_check = False

    def __init__(self, page: Page):
        super().__init__(page)

    def navigate_home(self):
        self.open_url(self.URL)

    def validate_login_elements(self):
        self.element_is_present(self.Txtbx_User)
        self.element_is_present(self.Txtbx_Pwd)
        self.element_is_present(self.Btn_LogIn)

    def validate_main_menu_items(self):
        self.element_is_present(self.Link_Solutions)
        self.element_is_present(self.Link_AboutUs)
        self.element_is_present(self.Link_Services)
        self.element_is_present(self.Link_Products)
        self.element_is_present(self.Link_Locations)
        self.main_menu_items_check = True

    def validate_welcome_section_elements(self):
        self.element_is_present(self.Icon_Home)
        self.element_is_present(self.Icon_AboutUs)
        self.element_is_present(self.Icon_Contact)
        self.main_menu_items_check = True

    def navigate_registration(self):
        self.click_element(self.Lnk_Register)
        self.element_is_present(self.Btn_Register)
