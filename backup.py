from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
import openpyxl
import time
import re

wb = openpyxl.Workbook()
sheet = wb.active
browser = webdriver.Chrome()
timeout = 3



try:
    browser.fullscreen_window()
    browser.maximize_window()
except Exception:
    print("Chrome is not able to maximize")

try:
    link = 'https://publicaccess.wycombe.gov.uk/idoxpa-web/search.do?action=advanced'
    browser.get(link)
    time.sleep(1)
except Exception:
    print("URL is wrong")

try:
    element_present = EC.presence_of_element_located((By.ID, 'main'))
    WebDriverWait(browser, timeout).until(element_present)
except TimeoutException:
    print("Timed out waiting for page to load")
finally:
    print("Page loaded")

try:
    time.sleep(1)
    browser.find_element_by_id('applicationValidatedStart').send_keys("01/01/2021")
    time.sleep(1)
    browser.find_element_by_id('applicationValidatedEnd').send_keys("15/01/2021")
    time.sleep(1)
    browser.find_element_by_xpath("// *[ @ id = 'advancedSearchForm'] / div[4] / input[2]").click()

except Exception:
    print("Date enter wrong")

try:
    time.sleep(1)
    browser.find_element_by_xpath("// *[ @ id = 'searchresults'] / li[1] / a").click()
except Exception:
    print("link is wrong")



time.sleep(1)
data_of_proposal=browser.find_element_by_xpath("//*[@id='simpleDetailsTable']/tbody/tr[6]/td").text
print(data_of_proposal)


# time.sleep(2)
browser.close()