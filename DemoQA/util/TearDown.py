from playwright.sync_api import Page


def close_browser(page: Page):
    page.close()
