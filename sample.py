# -*- coding: utf-8 -*-
from Twitter_Frontend_API import Client, API

import time
from tinydb import TinyDB, Query, where
import json
import requests
from bs4 import BeautifulSoup
import pandas as pd

import os
from dotenv import load_dotenv
import logging

lg = logging.getLogger(__name__)

# 環境変数を参照
load_dotenv()
SHEET_NAME = os.getenv('SHEET_NAME')



from BotHelper import JsonSearch, get_sheet_with_pd, set_sheet_with_pd, writeSheet


sheetname, col_name, row_name, input_val = SHEET_NAME, "badsotaru94", "api", "ok"

df = get_sheet_with_pd(sheetname=SHEET_NAME)

import pdb;pdb.set_trace()
writeSheet(sheetname, col_name, row_name, input_val)

#ログインと認証情報の定義
#認証情報は辞書形式での定義
auth = {'auth_token': '----------', 'ct0': '-----------'}

print(auth)
auth = API.Login("login", "pass")
#ログインあり
api = API(auth)
print(api.generate_ct0())
print(api.generate_authenticity())
print(api.generate_token())



# user info
user_info = api.user_info(screen_name="dsf33")
user_id = user_info['id_str']

# list info
lists = api.lists_all(user_id)
jse = JsonSearch(search_key='id_str')
list_id = jse.get_star(lists)[0]['id_str']

#リストの上限が5,000人なので超えそうだったら作り直す
member_num = jse.get_star(lists)[0]['member_count']


add_list = api.add_list_member(list_id, "1111")


usr = api.user_info(screen_name='1111')

import pdb;pdb.set_trace()




dms = api.get_dm()

keys = dms['inbox_initial_state'].keys()

"""
keys = [
    'last_seen_event_id', 'trusted_last_seen_event_id','untrusted_last_seen_event_id', 
    'cursor', 'inbox_timelines', 'entries', 'users', 'conversations']
    

"""

"""for k,y in dms['inbox_initial_state'].items():
    print(f'--------------{k}---------------------')
    if isinstance(y, list):
        df = pd.json_normalize(y)
        print('list is ')
        import pdb;pdb.set_trace()
    if isinstance(y, dict):
        print('dict is ')
        import pdb;pdb.set_trace()
    
    #
    #print(df)"""
    
    



url = "https://twitter.com/i/api/1.1/account/settings.json"
data = {
  'include_mention_filter': 'true',
  'include_nsfw_user_flag': 'true',
  'include_nsfw_admin_flag': 'true',
  'include_ranked_timeline': 'true',
  'include_alt_text_compose': 'true',
  'allow_dms_from': 'all'
}

import pdb;pdb.set_trace()
res = api._api(url, data)



import pdb;pdb.set_trace()
response = requests.get('https://twitter.com/i/api/1.1/dm/inbox_initial_state.json', headers=api.headers).json()
