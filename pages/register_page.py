from playwright.sync_api import Page
from pages.base_page import BasePage
import secrets
import string


class RegisterPage(BasePage):

    Txtbx_FirstName = "#customer\\.firstName"
    Txtbx_LastName = "#customer\\.lastName"
    Txtbx_Address = "#customer\\.address\\.street"
    Txtbx_City = "#customer\\.address\\.city"
    Txtbx_State = "#customer\\.address\\.state"
    Txtbx_Zip = "#customer\\.address\\.zipCode"
    Txtbx_Phone = "#customer\\.phoneNumber"
    Txtbx_SSN = "#customer\\.ssn"
    Txtbx_UserName = "#customer\\.username"
    Txtbx_Password = "#customer\\.password"
    Txtbx_PasswordAgain = "#repeatedPassword"

    Btn_Register = "input[value='Register']"
    Btn_LogOut = "//*[text()='Log Out']"
    Labl_Account = "//*[text()='Your account was created successfully. You are now logged in.']"

    register_success = False

    def __init__(self, page: Page):
        super().__init__(page)

    def registration_init(self):
        chars = string.ascii_letters + string.digits
        random_string = ''.join(
            secrets.choice(chars) for _ in range(10)
        )
        self.hm_global_data = {"username": random_string}

        self.enter_text(self.Txtbx_FirstName, "Jon")
        self.enter_text(self.Txtbx_LastName, "Doe")
        self.enter_text(self.Txtbx_Address, "221 Baker Street")
        self.enter_text(self.Txtbx_City, "Reading")
        self.enter_text(self.Txtbx_State, "NY")
        self.enter_text(self.Txtbx_Zip, "209876")
        self.enter_text(self.Txtbx_Phone, "7777788888")
        self.enter_text(self.Txtbx_SSN, "1122334455")
        self.enter_text(
            self.Txtbx_UserName,
            self.hm_global_data["username"]
        )
        self.enter_text(self.Txtbx_Password, "demo")
        self.enter_text(self.Txtbx_PasswordAgain, "demo")

        self.click_element(self.Btn_Register)

        self.element_is_present(self.Btn_LogOut)
        self.element_is_present(self.Labl_Account)

        self.register_success = True