from playwright.sync_api import expect, Page


def verify_radio_btn_selected(page: Page, sub_card_name):
    expect(page.locator('h1')).to_have_text(sub_card_name)


def select_and_verify_radio_btn_name(page: Page, radio_btn_name):
    is_enabled = page.locator('label').filter(has_text=radio_btn_name).is_enabled()
    if is_enabled:
        page.locator('label').filter(has_text=radio_btn_name).check()
        expect(page.locator('p')).to_have_text(f'You have selected {radio_btn_name}')
    else:
        print(f"'{radio_btn_name}' button is disabled")
