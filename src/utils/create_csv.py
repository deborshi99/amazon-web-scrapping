import os 
from .constraints import *
import json
import shutil

def convert_json_files_list():
    files = os.listdir(STG_FILES_PATH)
    all_url = []
    for file in files:
        with open(f'{os.path.join(STG_FILES_PATH, file)}', 'r') as f:
            result_array = json.load(f)
        print(result_array)
        for url in result_array:
            all_url.append(url)
    shutil.rmtree(STG_FILES_PATH)
    print(f'total {len(all_url)} urls found')
    return all_url
