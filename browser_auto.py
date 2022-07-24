# -*- coding:utf-8 -*-
import pandas as pd
import time
from BotHelper import JsonSearch, get_sheet_with_pd, set_sheet_with_pd, line_push, writeSheet
from BotHelper.util_driver import compose_driver, twitter_login, ouath_twitter_not_login, http_check, wifi_reboot

import pysnooper
from importlib import reload
import os
from contextlib import contextmanager

from dotenv import load_dotenv
import logging

lg = logging.getLogger(__name__)


# 環境変数を参照
load_dotenv()
API_URL = os.getenv('API_URL')
CHROME_PROFILE_DIR = os.getenv('CHROME_PROFILE_DIR')
SHEET_NAME = os.getenv('SHEET_NAME')



@contextmanager
def driver_set(prox=False, profdir=None, prof_name=None):
  
    driver = compose_driver(proxy_info=prox, userdata_dir=profdir, use_profile=prof_name)
    try:
        yield driver
    finally:
        driver.quit()

        
if __name__ == "__main__":
  
    #スプレッドシートからtwitterアカウントのIDなどを取得
    df = get_sheet_with_pd(sheetname=SHEET_NAME)
    #idのないセルを除去
    df.dropna(subset=['screen_name'], inplace=True)
    #まだアクセストークンを取得していない行のINDEXだけ
    no_end_index = df.loc[df['api'].isnull()].index
    #import pdb; pdb.set_trace()
    for loop_num, n in enumerate(no_end_index):
        #with Display(visible=0, size=(2160, 1440)) as disp:
        tw_info = df.iloc[n,:]
        twitter_id = tw_info['screen_name']
        twitter_pw = tw_info['password']
        twitter_email = tw_info['mail']
        user_id = tw_info['user_id']
        #---driver---
        user_profile = f"Profile {user_id}"
        driver = compose_driver(proxy_info=None, userdata_dir=CHROME_PROFILE_DIR, use_profile=user_profile)
        is_login = twitter_login(driver, twitter_id, twitter_pw, twitter_email)
        if is_login == True:
          #screen_name, user_id, oauth_token_secret, oauth_tokenの辞書
          apikey_dict = ouath_twitter_not_login(driver, API_URL)
          #完了した証にuser_idを入力
          writeSheet(SHEET_NAME, twitter_id, "oauth_token", apikey_dict['oauth_token'])
          writeSheet(SHEET_NAME, twitter_id, "oauth_token_secret", apikey_dict['oauth_token_secret'])
        else:
          line_push('{} is login error'.format(twitter_id))
          import pdb; pdb.set_trace()

        import pdb; pdb.set_trace()
        #wifi再起動
        wifi_reboot(driver)
        reboot_check = http_check(driver)
        driver.close()