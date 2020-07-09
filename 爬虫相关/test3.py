from selenium import  webdriver 
import time

driver = webdriver.Chrome() 



driver.get('https://y.qq.com/n/yqq/song/000xdZuV2LcQ19.html')
time.sleep(2)
link = driver.find_element_by_class_name('comment__show_all_link ')
link.click()
time.sleep(2)
comments = driver.find_elements_by_class_name('comment__list_item ')
for comment in comments:
    print(comment.text)
driver.close()