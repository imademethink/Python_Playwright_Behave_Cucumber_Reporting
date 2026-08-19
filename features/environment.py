import allure
from playwright.sync_api import sync_playwright
from utilities.driver_factory import DriverFactory


def before_scenario(context, scenario):
    context.playwright, context.browser, context.browser_context, context.page = (
        DriverFactory.get_driver("chrome")
        # DriverFactory.get_driver("firefox")
        # DriverFactory.get_driver("edge")
    )


def after_scenario(context, scenario):
    if hasattr(context, "page") and context.page:
        context.page.close()

    if hasattr(context, "browser_context") and context.browser_context:
        context.browser_context.close()

    if hasattr(context, "browser") and context.browser:
        context.browser.close()

    if hasattr(context, "playwright") and context.playwright:
        context.playwright.stop()


def after_step(context, step):
    if step.status == "failed":
        screenshot = context.page.screenshot()

        allure.attach(
            screenshot,
            name=f"Failed: {step.name}",
            attachment_type=allure.attachment_type.PNG
        )