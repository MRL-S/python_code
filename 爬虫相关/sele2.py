from selenium import webdriver
from bs4 import BeautifulSoup
import time

driver = webdriver.Chrome()
driver.get('https://localprod.pandateacher.com/python-manuscript/hello-spiderman/')
time.sleep(2)
teacher = driver.find_element_by_id('teacher')
teacher.send_keys('吴枫')
assistant = driver.find_element_by_id('assistant')
assistant.send_keys('都喜欢')
button = driver.find_element_by_class_name('sub')
button.click()
time.sleep(2)
pagesource = driver.page_source
bs = BeautifulSoup(pagesource,'html.parser')
contents = bs.find_all('div',class_='content')
for content in contents:
    print(content.find('p').text)
driver.close()
