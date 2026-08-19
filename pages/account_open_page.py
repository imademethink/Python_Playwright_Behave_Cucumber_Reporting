import time
from playwright.sync_api import Page
from pages.base_page import BasePage


class OpenAccountPage(BasePage):

    Lnk_OpenNewAccount = "//a[@href='openaccount.htm']"
    Btn_OpenNewAccount = "//input[@value='Open New Account']"
    Labl_AccountOpenSuccess = "//*[text()='Account Opened!']"
    # Labl_AccountId = "//*[@id='newAccountId']"
    Labl_AccountId = "//*[@id='fromAccountId']"
    Btn_TransferFunds = "//*[text()='Transfer Funds']"
    Txtbx_TransferAmount = "//*[@id='amount']"
    Btn_Transfer = "//input[@type='submit']"
    Labl_TransferComplete = "//*[text()='Transfer Complete!']"

    account_open_success = False

    def __init__(self, page: Page):
        super().__init__(page)

    def open_new_account(self):
        self.click_element(self.Lnk_OpenNewAccount)
        self.element_is_present(self.Btn_OpenNewAccount)
        self.click_element(self.Btn_OpenNewAccount)

    def new_account_validation(self):
        self.element_is_present(self.Labl_AccountOpenSuccess)
        self.element_is_present(self.Labl_AccountId)
        print(self.get_element_text(self.Labl_AccountId))
        self.account_open_success = True

    def init_fund_transfer(self, transfer_amount):
        self.click_element(self.Btn_TransferFunds)
        self.element_is_present(self.Txtbx_TransferAmount)
        self.enter_text(self.Txtbx_TransferAmount, transfer_amount)

    def fund_transfer_validation(self):
        self.click_element(self.Btn_Transfer)
        self.element_is_present(self.Labl_TransferComplete)