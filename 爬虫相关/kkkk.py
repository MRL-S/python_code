# from redis import StrictRedis

# redis = StrictRedis(host='localhost',port=6379,db=0)
# redis.set('name','Bob')
# print(redis.get('name'))
# from redis import StrictRedis,ConnectionPool

# url = 'redis://@localhost:6379/0'
# pool = ConnectionPool.from_url(url)
# redis = StrictRedis(connection_pool=pool)
# print(redis.get('name'))
# import re
# a= '''[2891] =&gt; array(5) {
#     [&quot;id&quot;] =&gt; string(4) &quot;2892&quot;
#     [&quot;name&quot;] =&gt; string(13) &quot;'''
# indexs = re.findall(r'; array\((.*?)\)',a,re.S)[0]
# print(type(indexs))
# number = 0
# indexs = [1, 2, 3, 4, 5, 11, 12, 13, 'a', 'b', 'c', 'd']
# contents = [6, 7, 8, 9, 10, 14, 15, 16, 'e', 'f', 'g', 'h']
# datas = []
# param = {}
# for index, content in zip(indexs, contents):

#     if len(param) < 4:
#         param[index] = content
#     else:

#         datas.append(param)
#         param = {}
#         param[index] = content
# else:
#     datas.append(param)
# print(datas)
# print(param)
# a = """        
#                 童书                        """
# print(a.strip())
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import urllib
from selenium.webdriver.common.action_chains import ActionChains
# webdriver = webdriver.PhantomJS(executable_path=r"E:\phantomjs\bin\phantomjs.exe",service_args=service_args)
cookies = {
    'value':"F21BAB01AD08B9CC5DF48F8DD6E352D8",
    'name':"JSESSIONID"
}
webdriver = webdriver.Chrome()

login_state = False
# webdriver.set_window_size(1400,700)
# webdriver.set_page_load_timeout(timeout)
wait = WebDriverWait(webdriver,10)
def index_page(page):
    global login_state
    try:
        if login_state is False:
            action = ActionChains(webdriver)
            urls = 'http://login.taobao.com'
            webdriver.get(urls)
            wait.until(
                EC.presence_of_element_located((By.ID,"fm-login-id"))

            ).send_keys("15298195937")
            wait.until(
                
                EC.presence_of_element_located((By.ID,"fm-login-password"))

            ).send_keys("10253uxtvop")
            slider = wait.until(
                EC.presence_of_element_located((By.ID,"nc_1_n1z"))
            )
            action.click_and_hold(on_element=slider).perform()
            action.move_by_offset(xoffset=280,yoffset=0).perform()
            action.release().perform()
            button = webdriver.find_element_by_class_name('fm-btn')
            button.click()
            login_state = True
        base_urls = 'http://s.taobao.com/search?q='
        keyword = 'ipad'
        url = base_urls+urllib.parse.quote(keyword)
        webdriver.get(url)
        
        if page > 1:
            input = wait.until(
                EC.presence_of_element_located((By.CSS_SELECTOR,'#mainsrp-pager > div > div > div > div.form > input'))
            )
            submit = wait.until(
                EC.element_to_be_clickable((By.CSS_SELECTOR,"#mainsrp-pager > div > div > div > div.form > span.btn.J_Submit"))
            )
            input.clear()
            input.send_keys(page)
            submit.click()
            wait.until(
                EC.text_to_be_present_in_element((By.CSS_SELECTOR,"#mainsrp-pager > div > div > div > ul > li.item.active > span"),str(page))
            )
            wait.until(
                EC.presence_of_element_located((By.CSS_SELECTOR,"#mainsrp-itemlist > div > div > div:nth-child(1)"))
            )
            
    except TimeoutException:
        return index_page(page)

if __name__=="__main__":
    for i in range(1,10):
        index_page(i)