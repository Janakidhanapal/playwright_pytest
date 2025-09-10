from playwright.sync_api import Page, expect

from DemoQA.conftest import load_test_data
from DemoQA.pages import Home, WebTables
from DemoQA.test_data.EnumTableHeaders import TableHeader
from DemoQA.test_data.EnumUserDetails import UserDetails
from DemoQA.util import TearDown, General


def test_homepage(page: Page):
    data = load_test_data()
    expect(page).to_have_title("DEMOQA")
    expect(page).to_have_url('https://demoqa.com/')
    Home.verify_card_visible(page, data['web_tables']['card_name'])
    TearDown.close_browser(page)


def test_elements_page(page: Page, test_data):
    Home.click_card(page, test_data['web_tables']['card_name'])
    General.verify_elements_page_loaded(page)
    TearDown.close_browser(page)


def test_web_tables_page(page: Page, test_data):
    Home.click_card(page, test_data['web_tables']['card_name'])
    General.verify_elements_page_loaded(page)
    General.select_card_name_from_dropdown(page, test_data['web_tables']['card_name'], test_data['web_tables']['sub_card_name'])
    TearDown.close_browser(page)


def test_click_add_button_and_verify_popup_opened(page: Page, test_data):
    Home.click_card(page, test_data['web_tables']['card_name'])
    General.verify_elements_page_loaded(page)
    General.select_card_name_from_dropdown(page, test_data['web_tables']['card_name'], test_data['web_tables']['sub_card_name'])
    WebTables.click_add_btn_and_verify_popup_opened(page)
    TearDown.close_browser(page)


def test_fill_the_user_details_in_popup(page: Page, test_data):
    user_details = test_data['web_tables']['user']
    Home.click_card(page, test_data['web_tables']['card_name'])
    General.verify_elements_page_loaded(page)
    General.select_card_name_from_dropdown(page, test_data['web_tables']['card_name'], test_data['web_tables']['sub_card_name'])
    WebTables.click_add_btn_and_verify_popup_opened(page)
    WebTables.fill_input_fields_in_popup_and_submit(page, user_details)
    TearDown.close_browser(page)


def test_verify_user_available_on_the_table_using_row_count(page: Page, test_data):
    user_details = test_data['web_tables']['user']
    Home.click_card(page, test_data['web_tables']['card_name'])
    General.verify_elements_page_loaded(page)
    General.select_card_name_from_dropdown(page, test_data['web_tables']['card_name'], test_data['web_tables']['sub_card_name'])
    WebTables.click_add_btn_and_verify_popup_opened(page)
    WebTables.fill_input_fields_in_popup_and_submit(page, user_details)
    # verify if the data is added using filter
    WebTables.check_data_added_in_table_using_row_count(page, user_details[UserDetails.FIRSTNAME])
    TearDown.close_browser(page)

def test_verify_user_details_displayed_on_the_table_using_search_box(page: Page, test_data):
    user_details = test_data['web_tables']['user']
    Home.click_card(page, test_data['web_tables']['card_name'])
    General.verify_elements_page_loaded(page)
    General.select_card_name_from_dropdown(page, test_data['web_tables']['card_name'], test_data['web_tables']['sub_card_name'])
    WebTables.click_add_btn_and_verify_popup_opened(page)
    WebTables.fill_input_fields_in_popup_and_submit(page, user_details)
    WebTables.search_for(page, user_details[UserDetails.EMAIL])
    WebTables.verify_actual_and_expected_row_values_equal(page, user_details)
    TearDown.close_browser(page)

def test_verify_cell_value_same(page: Page, test_data):
    user_details = test_data['web_tables']['user']
    Home.click_card(page, test_data['web_tables']['card_name'])
    General.verify_elements_page_loaded(page)
    General.select_card_name_from_dropdown(page, test_data['web_tables']['card_name'], test_data['web_tables']['sub_card_name'])
    WebTables.click_add_btn_and_verify_popup_opened(page)
    WebTables.fill_input_fields_in_popup_and_submit(page, user_details)
    WebTables.get_cell_text_by_email(page, TableHeader.EMAIL, user_details[UserDetails.EMAIL])
    TearDown.close_browser(page)

