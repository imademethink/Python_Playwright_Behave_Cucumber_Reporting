from playwright.sync_api import sync_playwright


class DriverFactory:

    @staticmethod
    def get_driver(browser_name="chrome"):
        browser = browser_name.lower()

        playwright = sync_playwright().start()

        if browser == "chrome":
            browser_instance = playwright.chromium.launch(headless=False, args=["--start-maximized"])
        elif browser == "firefox":
            browser_instance = playwright.firefox.launch(headless=False, args=["--start-maximized"])
        elif browser == "edge":
            browser_instance = playwright.chromium.launch(channel = "msedge", headless=False, args=["--start-maximized"])
        else:
            playwright.stop()
            raise ValueError(f"Browser '{browser_name}' is not supported.")

        context = browser_instance.new_context(no_viewport=True)
        page = context.new_page()

        return playwright, browser_instance, context, page