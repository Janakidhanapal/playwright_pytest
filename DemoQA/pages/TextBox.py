from playwright.sync_api import Page, expect, Locator

def fill_user_details(page: Page, fullname, email, c_address, p_address):
    page.get_by_placeholder('Full Name').fill(fullname)
    page.get_by_placeholder("name@example.com").fill(email)
    page.fill("#currentAddress", c_address)
    page.locator("#permanentAddress").fill(p_address)


def verify_user_detail(page: Page, fullname, email, c_address, p_address):
    page.wait_for_selector('#output > div')
    output: Locator = page.locator('#output')
    name = output.locator('#name').text_content().strip()
    assert name.split(":")[1].strip() == fullname
    email_id = output.locator('#email').text_content().strip()
    assert email_id.split(":")[1].strip() == email
    current_address = output.locator('#currentAddress').text_content().strip()
    assert current_address.split(":")[1].strip() == c_address
    permanent_address = output.locator('#permanentAddress').text_content().strip()
    assert permanent_address.split(":")[1].strip() == p_address

def verify_email_isvalid(page: Page):
    expect(page.locator('#userEmail')).to_have_css('border', '0.8px solid rgb(255, 0, 0)')