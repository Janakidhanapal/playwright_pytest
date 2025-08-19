import json
from pathlib import Path

import pytest
from playwright.sync_api import Page, expect
from DemoQA.pages import Home, RadioBtn
from DemoQA.util import TearDown, General


def load_json_data() -> dict:
    """Load JSON data from a file located at the project root."""
    root = Path(__file__).parent.parent.resolve()
    path = root / "test_data.json"
    with open(path, "r") as f:  # 'r' for the file is read only
        return json.load(f)


# In this case, we get the data from the fixture in conftest.py
def test_homepage(page: Page, demo_details):
    expect(page).to_have_title("DEMOQA")
    expect(page).to_have_url('https://demoqa.com/')
    Home.verify_card_visible(page, demo_details['radio_btn']['card_name'])
    TearDown.close_browser(page)


def test_elements_page(page: Page):
    data = load_json_data()
    Home.click_card(page, data['radio_btn']['card_name'])
    General.verify_elements_page_loaded(page)
    General.take_screenshot(page)
    page.wait_for_timeout(1000)
    TearDown.close_browser(page)


def test_radio_btn_page(page: Page):
    data = load_json_data()
    Home.click_card(page, data['radio_btn']['card_name'])
    General.verify_elements_page_loaded(page)
    General.select_card_name_from_dropdown(page, data['radio_btn']['card_name'], data['radio_btn']['sub_card_name'])
    RadioBtn.verify_radio_btn_selected(page, data['radio_btn']['sub_card_name'])
    TearDown.close_browser(page)


# parametrize allows you to pass different values in one test fn
@pytest.mark.parametrize("radio_selector", ['Yes', 'Impressive', 'No'])
def test_select_radio_btn_name(page: Page, radio_selector: str):
    data = load_json_data()
    Home.click_card(page, data['radio_btn']['card_name'])
    General.verify_elements_page_loaded(page)
    General.select_card_name_from_dropdown(page, data['radio_btn']['card_name'], data['radio_btn']['sub_card_name'])
    RadioBtn.verify_radio_btn_selected(page, data['radio_btn']['sub_card_name'])
    RadioBtn.select_and_verify_radio_btn_name(page, radio_selector)
    TearDown.close_browser(page)
