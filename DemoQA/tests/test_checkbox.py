import pytest
from playwright.sync_api import Page, expect

from DemoQA.conftest import load_test_data
from DemoQA.pages import Home, CheckBox
from DemoQA.util import TearDown, General

data = load_test_data()


def test_homepage(page: Page):
    expect(page).to_have_title("DEMOQA")
    expect(page).to_have_url('https://demoqa.com/')
    Home.verify_card_visible(page, data['check_box']['card_name'])
    TearDown.close_browser(page)


def test_elements_page(page: Page, test_data):
    Home.click_card(page, test_data['check_box']['card_name'])
    General.verify_elements_page_loaded(page)
    page.wait_for_timeout(1000)
    TearDown.close_browser(page)


def test_checkbox_page(page: Page, test_data):
    Home.click_card(page, test_data['check_box']['card_name'])
    General.verify_elements_page_loaded(page)
    General.select_card_name_from_dropdown(page, test_data['check_box']['card_name'],
                                           test_data['check_box']['sub_card_name'])
    CheckBox.click_expand_all(page)
    CheckBox.select_checkbox(page, test_data['check_box']['checkbox_name'])
    CheckBox.verify_checkbox_selected(page, test_data['check_box']['checkbox_name'])
    page.wait_for_timeout(5000)
    TearDown.close_browser(page)


@pytest.mark.parametrize("tree_list", data['check_box']['checkbox_tree_node'])
def test_click_checkbox_from_tree(page: Page, tree_list):
    Home.click_card(page, data['check_box']['card_name'])
    General.verify_elements_page_loaded(page)
    General.select_card_name_from_dropdown(page, data['check_box']['card_name'], data['check_box']['sub_card_name'])
    CheckBox.click_collapse_all(page)
    CheckBox.click_checkbox_from_tree_node_list(page, tree_list)
    CheckBox.verify_result_with_selected_checkbox(page, tree_list)
    page.wait_for_timeout(5000)
    TearDown.close_browser(page)
