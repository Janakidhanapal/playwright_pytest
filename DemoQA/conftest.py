# File name has to be conftest.py
import json
import os
from pathlib import Path

import allure
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

#take the screenshot on test failure and attach it to the Allure report
@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    # Execute all other hooks to obtain the report object
    outcome = yield
    report = outcome.get_result()
    # Only take screenshot on test failure
    if report.when == "call" and report.failed:
        page = item.funcargs.get("page", None)
        if page: screenshot = page.screenshot()
        allure.attach(screenshot, name="failure_screenshot", attachment_type=allure.attachment_type.PNG)


#we have two ways to get user data
#1st way is to get data from the json file
def load_test_data():
    project_root = Path(__file__).resolve().parent
    data_file = open(os.path.join(project_root, 'test_data', 'test_data.json'))
    return json.load(data_file)


@pytest.fixture()
def test_data():
    return load_test_data()


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

