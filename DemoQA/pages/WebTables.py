import pytest
from playwright.sync_api import Page, Error, expect

from DemoQA.test_data.EnumTableHeaders import TableHeader
from DemoQA.test_data.EnumUserDetails import UserDetails


def click_add_btn_and_verify_popup_opened(page: Page):
    try:
        page.locator('#addNewRecordButton').click()
        page.wait_for_selector("[role='document']", timeout=3000)
    except TimeoutError:
        page.locator("[class='close']").click()
        raise AssertionError("No popup opened within Timeout")
    except Error as e:
        page.locator("[class='close']").click()
        pytest.fail(f"Popup window not found: {e}")


def fill_input_fields_in_popup_and_submit(page: Page, user_details):
    page.get_by_placeholder("First Name").fill(user_details[UserDetails.FIRSTNAME])
    page.fill("#lastName", user_details[UserDetails.LASTNAME])
    page.fill("#userEmail", user_details[UserDetails.EMAIL])
    page.fill("#age", user_details[UserDetails.AGE])
    page.fill("#salary", user_details[UserDetails.SALARY])
    page.fill("#department", user_details[UserDetails.DEPARTMENT])
    page.get_by_text("Submit").press("Enter")
    expect(page.locator('#addNewRecordButton')).to_be_visible()


def check_data_added_in_table_using_row_count(page: Page, fname):
    row_count = get_row_count(page, fname)
    assert row_count > 0, f"Could not find '{fname}' in the table"

def search_for(page: Page, value):
    page.fill("#searchBox", value)

def get_row_count(page: Page, fname):
    rows = page.locator("//div[@class='rt-tbody']//div[@role='row']", has_text=fname)
    row_count = rows.count()
    print(row_count)
    return row_count

def get_cell_text(page: Page, column_name: TableHeader, row_number=1):
    if row_number > 10:
        pytest.fail('Row index should not be greater than 10')
    table_headers = page.locator('[role="columnheader"]').all_text_contents()
    expected_column_index = table_headers.index(column_name)
    column_value = page.locator('[role="row"]').nth(row_number).locator('[role="gridcell"]').all_inner_texts()[expected_column_index]
    print(column_value)
    return column_value

def get_cell_text_by_email(page: Page, column_name: TableHeader, email):
    search_for(page, email)
    return get_cell_text(page, column_name)

def verify_actual_and_expected_row_values_equal(page: Page, user_detail):
    row_count = get_row_count(page, user_detail[UserDetails.FIRSTNAME])
    if row_count > 0:
        # list_expected_user_details = ['Anu', 'Rahul', '23', 'anu@gmail.com', '5000', 'CSE']
        expected_row_value = list(user_detail.values())
        actual_row_value = page.locator('[role="row"]').nth(1).locator('[role="gridcell"]').all_text_contents()
        print(actual_row_value)
        for i in range(len(expected_row_value)-1):
            assert expected_row_value[i] == actual_row_value[i]
    else:
        pytest.fail("Entered user detail is not available in the table")

