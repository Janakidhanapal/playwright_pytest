import re

from playwright.sync_api import Page
from pygments import highlight

from DemoQA.tests.tmp import result


def click_expand_all(page: Page):
    page.get_by_title('Expand all').click()

def click_collapse_all(page: Page):
    page.get_by_title('Collapse all').click()

def select_checkbox(page: Page, checkbox_name):
    page.locator(f'label:has-text("{checkbox_name}")').click()

def verify_checkbox_selected(page: Page, checkbox_name):
    assert checkbox_name.lower() in  page.locator('#result').inner_text().lower()

def click_checkbox_from_tree_node(page: Page, tree_node):
    tree_nodes = tree_node.split('-')
    for i in range(len(tree_nodes)):
        if i == len(tree_nodes)-1:
            page.locator(f'label:has-text("{tree_nodes[i]}")').click()
        else:
            page.locator(f'xpath=//span[text()="{tree_nodes[i]}"]//ancestor::label//preceding::button[1]').click()

    for tree_node in tree_nodes[::-1]:
        page.locator(f'label:has-text("{tree_node}")').is_checked()

#check given input is a list or not. input is [['a','b'],'c']
def click_checkbox_from_tree_node_list(page: Page, tree_nodes):
    tree_node_type = str(type(tree_nodes))
    tree_node_type = tree_node_type.split("'")[1]
    #input ['a','b'] goes here
    if str(tree_node_type).lower() == "list":
        for tree_node in tree_nodes:
            click_collapse_all(page)
            click_checkbox_from_tree_node(page, tree_node)
    else:
        #input 'c' enters here
        click_checkbox_from_tree_node(page, tree_nodes)

def verify_result_with_selected_checkbox(page:Page, tree_node):
    result = page.locator('#result').inner_text()
    #highlighting the element
    page.eval_on_selector("#result", "element => element.style.border = '2px solid red'")
    tree_node_type = str(type(tree_node)) #output <type 'list'>
    tree_node_type = tree_node_type.split("'")[1]
    if str(tree_node_type).lower() == "list":
        for single_node in tree_node:
            tree_last_name = single_node.split('-')[-1]
            node_name = re.sub(' ', '', tree_last_name)
            checkbox_name = (node_name[0].lower() + node_name[1:]).split('.')[0]
            assert checkbox_name in result
    else:
        #input: "Home-Downloads-Excel File.doc"
        tree_last_name = tree_node.split('-')[-1] #get "Excel File.doc"
        node_name = re.sub(' ', '', tree_last_name) #remove space "ExcelFile.doc"
        checkbox_name = (node_name[0].lower() + node_name[1:]).split('.')[0] #output is "excelFile"
        assert checkbox_name in result
