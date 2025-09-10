from DemoQA.conftest import load_test_data
#
data = load_test_data()
user_details: dict = data['web_tables']['user']
print(user_details.values())

a = ['alpha', 'beta', 'gamma']
print(a.index('beta'))
