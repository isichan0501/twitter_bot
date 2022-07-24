# -*- coding:utf-8 -*-
# ------------------------------------------------------------------
import  sys
from random import choice, uniform
import time
import pathlib
import logging
import logging.config
from contextlib import contextmanager, suppress
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import (NoSuchElementException,
                                        StaleElementReferenceException,
                                        TimeoutException)
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
import socket
import pysnooper
from importlib import reload
import os
#from pyvirtualdisplay import Display
import undetected_chromedriver.v2 as uc
from selenium.webdriver.common.proxy import Proxy, ProxyType


lg = logging.getLogger(__name__)


def page_load(driver, myurl):
    waitTime = 5
    for ww in range(1, 4):
        mywait = waitTime * ww
        try:
            driver.get(myurl)
            WebDriverWait(driver, mywait).until(EC.presence_of_all_elements_located)
            break
        except (socket.timeout, NoSuchElementException, TimeoutException, Exception) as e:
            print(e)
            lg.exception(e)


def myClick(driver, by, desc):
    waitn = WebDriverWait(driver, 5)
    try:
        by = by.upper()
        if by == 'XPATH':
            waitn.until(EC.element_to_be_clickable((By.XPATH, desc))).click()
        if by == 'ID':
            waitn.until(EC.element_to_be_clickable((By.ID, desc))).click()
        if by == 'LINK_TEXT':
            waitn.until(EC.element_to_be_clickable((By.LINK_TEXT, desc))).click()
        if by == "NAME":
            waitn.until(EC.element_to_be_clickable((By.NAME, desc))).click()
        if by == "CSS":
            waitn.until(EC.element_to_be_clickable((By.CSS_SELECTOR, desc))).click()
        if by == "OK":
            waitn.until(EC.presence_of_all_elements_located)
            desc.click()
            

    except (socket.timeout, NoSuchElementException, TimeoutException, Exception) as ex:
        print(ex)


def action_click(driver, elem):
    # elemは(By.XPATH, 'xpath')のようなタプル
    waitn = WebDriverWait(driver, 5)
    try:
        elem = waitn.until(EC.element_to_be_clickable(elem))
        webdriver.ActionChains(driver).move_to_element(elem).click().perform()
    except (socket.timeout, NoSuchElementException, TimeoutException, Exception) as ex:
        print(ex)


def slowClick(driver, by, desc):
    waitn = WebDriverWait(driver, 10)
    try:
        by = by.upper()
        if by == 'XPATH':
            waitn.until(EC.element_to_be_clickable((By.XPATH, desc))).click()
        if by == 'ID':
            waitn.until(EC.element_to_be_clickable((By.ID, desc))).click()
        if by == 'LINK_TEXT':
            waitn.until(EC.element_to_be_clickable((By.LINK_TEXT, desc))).click()
        if by == "NAME":
            waitn.until(EC.element_to_be_clickable((By.NAME, desc))).click()
        if by == "CSS":
            waitn.until(EC.element_to_be_clickable((By.CSS_SELECTOR, desc))).click()
        if by == "OK":
            waitn.until(EC.presence_of_all_elements_located)
            desc.click()
        waitn.until(EC.presence_of_all_elements_located)

    except (socket.timeout, NoSuchElementException, TimeoutException, Exception) as ex:
        print(ex)
        raise

        
def mySendkey(driver, by, desc, my_word):
    waitn = WebDriverWait(driver, 10)
    time.sleep(1)
    try:
        by = by.upper()
        if by == 'XPATH':
            waitn.until(EC.element_to_be_clickable((By.XPATH, desc))).clear()
            waitn.until(EC.element_to_be_clickable((By.XPATH, desc))).send_keys(my_word)
        if by == 'ID':
            waitn.until(EC.element_to_be_clickable((By.ID, desc))).clear()
            waitn.until(EC.element_to_be_clickable((By.ID, desc))).send_keys(my_word)
        if by == 'LINK_TEXT':
            waitn.until(EC.element_to_be_clickable((By.LINK_TEXT, desc))).clear()
            waitn.until(EC.element_to_be_clickable((By.LINK_TEXT, desc))).send_keys(my_word)
        if by == "NAME":
            waitn.until(EC.element_to_be_clickable((By.NAME, desc))).clear()
            waitn.until(EC.element_to_be_clickable((By.NAME, desc))).send_keys(my_word)
        if by == "CSS":
            waitn.until(EC.element_to_be_clickable((By.CSS_SELECTOR, desc))).clear()
            waitn.until(EC.element_to_be_clickable((By.CSS_SELECTOR, desc))).send_keys(my_word)
        if by == "OK":
            waitn.until(EC.presence_of_all_elements_located)
            desc.clear()
            desc.send_keys(my_word)

        waitn.until(EC.presence_of_all_elements_located)
    except (socket.timeout, NoSuchElementException, TimeoutException, Exception) as ex:
        print(ex)
        raise



def exe_click(driver, by, desc):
    waitn = WebDriverWait(driver, 10)
    try:
        by = by.upper()
        if by == 'XPATH':
            waitn.until(EC.presence_of_element_located((By.XPATH, desc)))
            driver.execute_script("arguments[0].click();", driver.find_element(By.XPATH, desc))
        if by == 'ID':
            waitn.until(EC.presence_of_element_located((By.ID, desc)))
            driver.execute_script("arguments[0].click();", driver.find_element(By.ID, desc))
        if by == 'LINK_TEXT':
            waitn.until(EC.presence_of_element_located((By.LINK_TEXT, desc)))
            driver.execute_script("arguments[0].click();", driver.find_element(By.LINK_TEXT, desc))
        if by == "NAME":
            waitn.until(EC.presence_of_element_located((By.NAME, desc)))
            driver.execute_script("arguments[0].click();", driver.find_element(By.NAME, desc))
        if by == "CSS":
            waitn.until(EC.presence_of_element_located((By.CSS_SELECTOR, desc)))
            driver.execute_script("arguments[0].click();", driver.find_element(By.CSS_SELECTOR, desc))
        if by == "OK":
            waitn.until(EC.presence_of_all_elements_located)
            driver.execute_script("arguments[0].click();", desc)
        waitn.until(EC.presence_of_all_elements_located)

    except (socket.timeout, NoSuchElementException, TimeoutException, Exception) as ex:
        print(ex)
        raise

def waiting_for_element(driver, element, wait_time):
    try:
        WebDriverWait(driver, wait_time).until(EC.presence_of_element_located(
            element))
    except Exception as e:
        print(e)


def send_keys(driver, element, key):
    action = webdriver.ActionChains(driver)
    action.send_keys_to_element(element, key).pause(uniform(.1, .5)) \
        .send_keys_to_element(element, Keys.ENTER).perform()


def check_element(driver, element_data, el_max_wait_time=10):
    """check if an element exists on the page"""
    element = element_data[0]
    text = element_data[1]
    try:
        wait = WebDriverWait(driver, el_max_wait_time)
        wait.until(EC.presence_of_element_located(element))
        if text and text not in driver.find_element(*element).text:
            return False
    except Exception as e:
        print(e)
        return False
    return True


def submit_bt_click(driver, submit):
    try:
        driver.switch_to.default_content()
        time.sleep(uniform(1.0, 5.0))
        element = driver.find_element(*submit)
        webdriver.ActionChains(driver).move_to_element(element).click().perform()
    except Exception as e:
        print(e)


def smartproxy(host, port):
    DRIVER = 'CHROME'
    
    prox = Proxy()
    prox.proxy_type = ProxyType.MANUAL

    prox.http_proxy = '{hostname}:{port}'.format(hostname = host, port = port)
    prox.ssl_proxy = '{hostname}:{port}'.format(hostname = host, port = port)

    if DRIVER == 'FIREFOX':
        capabilities = webdriver.DesiredCapabilities.FIREFOX
    elif DRIVER == 'CHROME':
        capabilities = webdriver.DesiredCapabilities.CHROME
    prox.add_to_capabilities(capabilities)

    return capabilities
    
    
@contextmanager
def driver_set(use_proxy=False, use_profile=None, user_agent=None):
    co = Options()
    if use_proxy:
        co.add_argument('--proxy-server={0}'.format(use_proxy))
    if use_profile:
        userdir = pathlib.Path.cwd() / "UserData"
        os.makedirs(userdir, exist_ok=True)
        co.add_argument('--user-data-dir={0}'.format(userdir))
        co.add_argument('--profile-directory={}'.format(use_profile))
    if user_agent:
        co.add_argument('--user-agent={}'.format(user_agent))

    #co.add_argument('--start-maximized')
    co.add_argument('--window-size=1440,920')
    co.add_experimental_option("excludeSwitches", ['enable-automation'])
    co.add_argument('--disable-blink-features=AutomationControlled')
    co.add_argument('--disable-gpu')
    co.add_argument('--ignore-certificate-errors')
    co.add_argument('--allow-file-access-from-files')
    co.add_argument('--disable-web-security')
    co.add_argument('--lang=ja')
    ch_r = [os.path.join(os.path.abspath(
        os.path.dirname(__file__))), 'chromedriver']
    chrome_driver = os.path.join(*ch_r)
    driver = webdriver.Chrome(ChromeDriverManager().install(), options=co)
    driver.implicitly_wait(15)
    driver.set_page_load_timeout(60)
    try:
        yield driver
    finally:
        driver.quit()


@pysnooper.snoop()
def compose_driver(proxy_info=None, userdata_dir=None, use_profile=None):
    co = uc.ChromeOptions()
    co.add_argument('--no-first-run --no-service-autorun --password-store=basic')
    if not proxy_info == None:
        co.add_argument('--proxy-server={}'.format(proxy_info))
    co.add_argument('--no-default-browser-check')
    co.add_argument('--lang=ja-JP')
    co.add_argument("--proxy-bypass-list:localhost,127.0.0.1")
    if not userdata_dir == None:
        userdata_dir = os.path.join(os.getcwd(), 'ChromeProfile')
        #userdata_path = pathlib.Path('./ChromeProfile')
        co.add_argument('--user-data-dir={}'.format(userdata_dir))
    if not use_profile == None:
        co.add_argument('--profile-directory={}'.format(use_profile))
    driver = uc.Chrome(options=co)
    driver.implicitly_wait(10)
    driver.set_page_load_timeout(60)
    return driver

@pysnooper.snoop()
def http_check(driver):
  time.sleep(20)
  for i in range(100):
    try:
      driver.get("https://www.cman.jp/network/support/go_access.cgi")
      time.sleep(2)
      tileget = driver.title
      if tileget == "アクセス情報【使用中のIPアドレス確認】":
        print('再起動OK')
        return True
          
    except (socket.timeout, NoSuchElementException, TimeoutException, Exception) as e:
      print('wait 20sec')
      time.sleep(20)

      
@pysnooper.snoop()
def wifi_reboot(driver):
  try:
    page_load(driver,"http://web.setting/html/home.html")
    myClick(driver, "css", "#settings > span")
    time.sleep(2)
    # import pdb; pdb.set_trace()
    myClick(driver, "id", "password")
    time.sleep(1)
    mySendkey(driver,"id","password","admin")
    time.sleep(1)
    myClick(driver, "link_text", "ログイン")
    time.sleep(2)
    driver.refresh()
    myClick(driver, "id", "system")
    myClick(driver, "link_text", "再起動")
    time.sleep(2)
    myClick(driver, "css", ".button_center")
    time.sleep(2)
    myClick(driver, "link_text", "はい")
  except (socket.timeout, NoSuchElementException, TimeoutException, Exception) as e:
    print(e)


def ouath_twitter(driver, myurl, twitter_id, twitter_pw, twitter_mail):
    wait = WebDriverWait(driver, 15)
    try:
        page_load(driver,myurl)
        #Twitterでログインボタンを押す
        action_click(driver, (By.XPATH, "/html/body/div/button"))
        time.sleep(4)
        #最初のログインページ
        send_keys(driver, (By.ID, "username_or_email"), twitter_id)
        mySendkey(driver,"id","username_or_email",twitter_id)
        mySendkey(driver,"id","password",twitter_pw)
        action_click(driver, (By.ID, "allow"))
        time.sleep(2)
        wait.until(EC.presence_of_all_elements_located)
        #メルアド認証を求められるので
        mySendkey(driver,"id","challenge_response",twitter_mail)
        exe_click(driver,"id","email_challenge_submit")
        time.sleep(2)
        wait.until(EC.presence_of_all_elements_located)
        #最後に認証ボタンを押す
        exe_click(driver,"id","allow")
        time.sleep(5)
    except (socket.timeout, NoSuchElementException, TimeoutException, Exception) as e:
        print(e)


@pysnooper.snoop()
def ouath_twitter_not_login(driver, myurl):
    wait = WebDriverWait(driver, 15)
    try:
        page_load(driver,myurl)
        #Twitterでログインボタンを押す
        action_click(driver, (By.XPATH, "/html/body/div/button"))
        time.sleep(4)
        wait.until(EC.presence_of_all_elements_located)
        #最後に認証ボタンを押す
        action_click(driver,(By.ID, "allow"))
        time.sleep(5)
        wait.until(EC.presence_of_all_elements_located)
        apikey_str = driver.find_elements(By.XPATH, "/html/body/div[2]/div/p")
        api_list = [a.text for a in apikey_str]
        #辞書型にする
        api_dict = {}
        for ak in api_list:
          key_val = ak.split(':')
          k, v = key_val[0], key_val[1]
          api_dict[k] = v
        return api_dict
        
    except (socket.timeout, NoSuchElementException, TimeoutException, Exception) as e:
        print(e)


@pysnooper.snoop()
def twitter_login(driver, twitter_id, twitter_pw, twitter_email):
    try:
        page_load(driver, 'https://twitter.com')
        # login button
        waiting_for_element(
            driver,
            (By.XPATH, '//a[@href="/login"]'), 5)
        login_bt = driver.find_element(
            By.XPATH, '//a[@href="/login"]')
        webdriver.ActionChains(driver).move_to_element(login_bt).click().perform()
        time.sleep(2)
        # login input
        waiting_for_element(
            driver,
            (By.CSS_SELECTOR, '#react-root input'), 5)
        inp = driver.find_element(
            By.CSS_SELECTOR,
            '#react-root input')
        send_keys(driver, inp, twitter_id)
        time.sleep(2)
        # password input
        waiting_for_element(
            driver,
            (By.CSS_SELECTOR, '#layers > div:nth-child(2) input'), 5)
        inp = driver.find_elements(
            By.CSS_SELECTOR,
            '#layers > div:nth-child(2) input')[1]
        send_keys(driver, inp, twitter_pw)
        time.sleep(2)
        #inputタグが１つでtype=emailのページだったらメルアド認証　or コード認証
        WebDriverWait(driver, 5).until(EC.presence_of_all_elements_located)
        #inputフォームが１つのページ
        input_tag = driver.find_elements(By.TAG_NAME, "input")
        if len(input_tag) == 1:
            if input_tag[0].get_attribute('type') == 'email':
                inp = input_tag[0]
                send_keys(driver, inp, twitter_email)
            elif input_tag[0].get_attribute('type') == 'text':
                print('認証必要あり')
            time.sleep(2)

        WebDriverWait(driver, 15).until(EC.presence_of_all_elements_located)
        if driver.current_url == "https://twitter.com/home":
            print('{}, login success')
            return True
        else:
            print('{}, login error'.format(twitter_id))
            return False
    except Exception as e:
        print(e)