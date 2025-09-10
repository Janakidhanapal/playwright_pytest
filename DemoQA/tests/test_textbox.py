import pytest
from pathlib import Path
import os
import json
from playwright.sync_api import Page, expect

from DemoQA.conftest import demo_details
from DemoQA.pages import Home, TextBox
from DemoQA.util import TearDown, General


def load_test_data():       #it takes the data from the json file
    project_root = Path(__file__).resolve().parent.parent
    data_file = open(os.path.join(project_root, 'test_data.json'))
    return json.load(data_file)

#this decorator is used to generate the pytest-html=report
@pytest.mark.reporting(
    developer="Janaki",
    functional_specification="SPEC-001",
    test_description="Validate Home page"
)
@pytest.mark.category("regression")
def test_homepage(page: Page, logger, demo_details):
    #in this case, we get the data from the fixture in conftest.py
    expect(page).to_have_title("DEMOQA")
    expect(page).to_have_url('https://demoqa.com/')
    Home.verify_card_visible(page, demo_details['card_name'])
    logger.step("Home page is validated successfully")
    TearDown.close_browser(page)

@pytest.mark.reporting(
    developer="Janaki",
    functional_specification="SPEC-001",
    test_description="Validate Home page"
)
@pytest.mark.category("regression")
def test_elements_page(page: Page):
    data = load_test_data()
    Home.click_card(page, data['card_name'])
    General.verify_elements_page_loaded(page)
    General.take_screenshot(page)
    page.wait_for_timeout(5000)
    TearDown.close_browser(page)


@pytest.mark.reporting(
    developer="Janaki",
    functional_specification="SPEC-001",
    test_description="Validate Home page"
)
@pytest.mark.category("regression")
def test_textbox_page(page: Page):
    data = load_test_data()
    Home.click_card(page, data['card_name'])
    General.verify_elements_page_loaded(page)
    General.select_card_name_from_dropdown(page, data['card_name'], data['sub_card_name'])
    TearDown.close_browser(page)


@pytest.mark.reporting(
    developer="Janaki",
    functional_specification="SPEC-001",
    test_description="Validate Home page"
)
@pytest.mark.category("regression")
def test_textbox_fill(page: Page):
    data = load_test_data()
    Home.click_card(page, data['card_name'])
    General.verify_elements_page_loaded(page)
    General.select_card_name_from_dropdown(page, data['card_name'], data['sub_card_name'])
    TextBox.fill_user_details(page, data['user']['name'], data['user']['email'], data['user']['currentAddress'],
                              data['user']['permanentAddress'])
    General.submit_form(page)
    page.wait_for_timeout(5000)
    TearDown.close_browser(page)


@pytest.mark.reporting(
    developer="Janaki",
    functional_specification="SPEC-001",
    test_description="Validate Home page"
)
@pytest.mark.category("regression")
def test_detail_verification(page: Page):
    data = load_test_data()
    Home.click_card(page, data['card_name'])
    General.verify_elements_page_loaded(page)
    General.select_card_name_from_dropdown(page, data['card_name'], data['sub_card_name'])
    TextBox.fill_user_details(page, data['user']['name'], data['user']['email'], data['user']['currentAddress'],
                              data['user']['permanentAddress'])
    General.submit_form(page)
    TextBox.verify_user_detail(page, data['user']['name'], data['user']['email'], data['user']['currentAddress'],
                               data['user']['permanentAddress'])
    TearDown.close_browser(page)


@pytest.mark.smoke
@pytest.mark.reporting(
    developer="Janaki",
    functional_specification="SPEC-001",
    test_description="Validate Home page"
)
@pytest.mark.category("regression")
def test_invalid_email(page: Page):
    data = load_test_data()
    Home.click_card(page, data['card_name'])
    General.verify_elements_page_loaded(page)
    General.select_card_name_from_dropdown(page, data['card_name'], data['sub_card_name'])
    TextBox.fill_user_details(page, ' ', data['invalid_email'], ' ', ' ')
    General.submit_form(page)
    TextBox.verify_email_isvalid(page)
    TearDown.close_browser(page)
