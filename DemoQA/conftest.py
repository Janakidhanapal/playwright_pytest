# File name has to be conftest.py

import pytest
from playwright.sync_api import Page


@pytest.fixture(scope="session")
def browser_type_launch_args():
    return {
        "headless": False,
        "channel": "msedge",
        "slow_mo": 1000
    }

#this fixture will run before every test function starts
@pytest.fixture(autouse=True)
def setup(page: Page):
    page.goto('https://demoqa.com/')

#we have two ways to get user data
#1st way is to get data from the json file
#another way is to get from the fixture like the below
@pytest.fixture()
def demo_details():
    return {
        "card_name": "Elements",
        "sub_card_name": "Text Box",
        "user": {
            "name": "Alpha",
            "email": "alpha@gmail.com",
            "currentAddress": "Bangalore",
            "permanentAddress": "Chennai"
        },
        "invalid_email": "a@gmail"
    }

