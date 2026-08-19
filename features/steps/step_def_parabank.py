from behave import given, when, then

from pages.account_open_page import OpenAccountPage
from pages.home_page import HomePage
from pages.register_page import RegisterPage


@given('User is in on home page')
def step_user_is_in_on_home_page(context):
    context.home_page = HomePage(context.page)
    context.home_page.navigate_home()
    context.home_page.validate_login_elements()


@when('User validates main menu items')
def step_user_validates_main_menu_items(context):
    context.home_page.validate_main_menu_items()


@then('Main menu item validation should be successful')
def step_main_menu_item_validation_should_be_successful(context):
    assert context.home_page.main_menu_items_check, \
        "Log: Main menu item validation failed"


@when('User validates welcome section items')
def step_user_validates_welcome_section_items(context):
    context.home_page.validate_welcome_section_elements()


@then('Welcome section item validation should be successful')
def step_welcome_section_item_validation_should_be_successful(context):
    assert context.home_page.main_menu_items_check, \
        "Log: Main menu item validation failed"


@when('User perform registration')
def step_user_perform_registration(context):
    context.home_page.navigate_registration()
    context.register_page = RegisterPage(context.page)
    context.register_page.registration_init()


@then('Registration should be successful')
def step_registration_should_be_successful(context):
    assert context.register_page.register_success, \
        "Log: Registration failed"

# this step is failed on purpose to see failure in allure report
@then('Account opening should not be successful')
def step_account_opening_should_not_be_successful(context):
    context.open_account_page = OpenAccountPage(context.page)
    # assert not context.open_account_page.account_open_success, \
    #     "Log: Account opened without user intention!"
    assert context.open_account_page.account_open_success, \
        "Log: Account opened without user intention!"


@given('User registration is successful')
def step_user_registration_is_successful(context):
    context.home_page = HomePage(context.page)
    context.home_page.navigate_home()
    context.home_page.navigate_registration()
    context.register_page = RegisterPage(context.page)
    context.register_page.registration_init()


@when('User initiate New Account Opening')
def step_user_initiate_new_account_opening(context):
    context.open_account_page = OpenAccountPage(context.page)
    context.open_account_page.open_new_account()


@then('New Account Opening should be successful')
def step_new_account_opening_should_be_successful(context):
    context.open_account_page.new_account_validation()


@when('User initiate Fund Transfer "{transfer_amount}"')
def step_user_initiate_fund_transfer(context, transfer_amount):
    context.open_account_page = OpenAccountPage(context.page)
    context.open_account_page.init_fund_transfer(transfer_amount)


@then('Fund Transfer should be successful')
def step_fund_transfer_should_be_successful(context):
    context.open_account_page.fund_transfer_validation()