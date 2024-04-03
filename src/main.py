from services.data_scapping.scrapper import scrappy
from utils.constraints import *
from utils.create_csv import convert_json_files_list
import json
import pandas as pd
import os 

if __name__ == '__main__':
    with open(CONFIG_FILE_PATH, 'r') as config:
        data = json.load(config)
    
    url = data['url']
    print(url)
    item = data['item'] 
    
    scrapper = scrappy(url)
    scrapper.direct_to_items(item)
    print('Creating list from all JSON files')
    all_urls = convert_json_files_list()
    pre_df = []
    for url in all_urls:
        details = scrapper.connect_item(url, item)
        pre_df.append(details)
    df = pd.DataFrame.from_dict(pre_df)
    os.makedirs(OUTPUT_FILE_PATH, exist_ok=True)
    df.to_csv(f'{OUTPUT_FILE_PATH}/details.csv', index=False, header=True)
    print(f"File saved in {OUTPUT_FILE_PATH}/detail.csv")   
    