from behave import given, when, then
from pages.login_page import LoginPage


@given('I navigate to the login page')
def step_navigate_to_login(context):
    context.login_page = LoginPage(context.page)
    context.login_page.navigate()


@when('I enter valid username "{username}" and password "{password}"')
def step_enter_credentials(context, username, password):
    context.login_page.login(username, password)


@when('I click the login button')
def step_submit_login(context):
    context.login_page.click_login()


@then('I should be redirected to the inventory dashboard')
def step_verify_dashboard(context):
    expected_partial_url = "inventory.html"
    actual_url = context.login_page.get_current_url()

    assert expected_partial_url in actual_url, (
        f"Expected redirect containing '{expected_partial_url}', "
        f"but got '{actual_url}'"
    )