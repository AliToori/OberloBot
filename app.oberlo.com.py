#!/usr/bin/env python3
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import WebDriverException, TimeoutException
from selenium.webdriver import ActionChains


# import pyautogui


# **********************************************************************
# This method is for site login
# **********************************************************************
def site_login(url, email, password):
    driver.get(url)
    time.sleep(3)
    try:
        driver.find_element_by_name('email').send_keys(email)
        driver.find_element_by_name('password').send_keys(password)
        driver.find_element_by_tag_name('button').click()
        time.sleep(3)
    except TimeoutException as tex:
        print("EXCEPTION IN SIGNOUT:", tex.msg)
    dashboard = driver.find_element_by_tag_name('h2').text
    if dashboard == 'Dashboard':
        print("Login Successful. Welcome to your dashboard !")
    else:
        print("Login Failed !")


# **********************************************************************
#    The program starts from here
# **********************************************************************
web_url = 'https://app.oberlo.com/login'
email = "humans313@gmail.com"
password = "humans313@oberlo"
options = webdriver.ChromeOptions()
options.add_argument("--incognito")
# driver = webdriver.Chrome('../Desktop/chromedriver', options=options)
driver = webdriver.Chrome(options=options)
site_login(url=web_url, email=email, password=password)

driver.close()
driver.quit()
