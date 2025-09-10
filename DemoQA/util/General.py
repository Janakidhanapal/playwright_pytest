import os
from datetime import datetime

from playwright.sync_api import Page, expect


def verify_elements_page_loaded(page: Page):
    expect(page.get_by_text("Please select an item from left to start practice.")).to_be_visible()


def select_card_name_from_dropdown(page: Page, card_name, sub_card_name):
    expect(page.locator('.header-text').nth(0)).to_have_text(card_name)
    page.locator('.menu-list > li').filter(has_text=sub_card_name).click()


def take_screenshot(page: Page, name="screenshot"):
    path = get_unique_file_name('screenshots', 'screenshot')
    os.makedirs(name, exist_ok=True)
    page.screenshot(path=path)


def get_unique_file_name(dir_name, file_prefix):
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    return os.path.join(dir_name, f"{file_prefix}_{timestamp}.png")


def submit_form(page: Page):
    page.locator('#submit').click()
