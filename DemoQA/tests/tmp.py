import json
import os
from pathlib import Path


project_root = Path(__file__).resolve().parent.parent
data_file = open(os.path.join(project_root, 'test_data.json'))
data = json.load(data_file)
print(data)
print(data['users']['name'])
