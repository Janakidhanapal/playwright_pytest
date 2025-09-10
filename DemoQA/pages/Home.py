from playwright.sync_api import Page


def verify_card_visible(page: Page, card_name: str):
    page.is_visible(selector=f'h5:has-text("{card_name}")')


def click_card(page: Page, card_name: str):
    page.get_by_role('heading', name=card_name).click()
