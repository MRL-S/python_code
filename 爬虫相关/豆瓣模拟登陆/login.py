from selenium import webdriver
import time

url = 'https://www.douban.com'
browser = webdriver.PhantomJS(executable_path=r"E:\phantomjs\bin\phantomjs.exe")
browser.get(url)

browser.implicitly_wait(10)

# 重点1要先切换到子框架
browser.switch_to.frame(browser.find_elements_by_tag_name('iframe')[0])

# 重点2要先点击用账号密码登录的按钮，不然会找不到输入账号和密码的地方
bottom1 = browser.find_element_by_xpath('/html/body/div[1]/div[1]/ul[1]/li[2]')
bottom1.click()

input1 = browser.find_element_by_id('username')
input1.clear()
input1.send_keys('your phone number')

input2 = browser.find_element_by_id('password')
input2.clear()
input2.send_keys('xxxxxxxxxxxx')

time.sleep(10)
# 手动输入验证码。。这个后面再弄

bottom = browser.find_element_by_class_name('account-form-field-submit ')
bottom.click()

