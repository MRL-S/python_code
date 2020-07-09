from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from urllib.parse import quote
from pyquery import PyQuery as pq
import time

browser = webdriver.Chrome()
wait = WebDriverWait(browser,10)
keyword = 'ipad'
url = 'http://s.taobao.com/search?q='+quote(keyword)
browser.get(url)
# input = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR,'#mainsrp-pager div.form>input')))
# submit = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,'#mainsrp-pager div.form>span.btn.J_Submit')))
# input.clear()
# input.send_keys('')
# submit.click()
input1 = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,'#J_StaticForm div.username-field #TPL_username_1')))
input2 = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,'#J_StaticForm div.pwd-field input.login-text')))
submit1 = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,'#J_StaticForm div.submit button.J_Submit')))
input1.clear()
input1.send_keys('力量之源power')
input2.send_keys('10253uxtvop')
submit1.click()