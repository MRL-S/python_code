from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
import time
import urllib
from pyquery import PyQuery as pq
class tianmaospider():
    def __init__(self):
        self.options = webdriver.ChromeOptions()
        self.options.add_argument('--headless')
        self.options.add_experimental_option('prefs',{"profile.managed_default_content_settings.images":2})
        self.options.add_experimental_option('excludeSwitches',['enable-automation'])
        self.brower = webdriver.Chrome(options=self.options)
        self.action = ActionChains(self.brower)
        self.wait = WebDriverWait(self.brower,10)
    
    def login(self):
        """ 模拟登陆 """
        url = 'https://login.taobao.com/member/login.jhtml'

        self.brower.get(url)
        self.brower.implicitly_wait(10)
        username = self.brower.find_element_by_xpath('//input[@id="fm-login-id"]')
        password = self.brower.find_element_by_xpath('//input[@id="fm-login-password"]')

        username.send_keys("15298195937")
        password.send_keys("10253uxtvop")
        time.sleep(5)
        yanzhen = self.wait.until(
            EC.element_to_be_clickable((By.XPATH,'//span[@id="nc_1_n1z"]'))
        )
        self.action.click_and_hold(on_element=yanzhen).perform()
        self.action.move_by_offset(xoffset=300,yoffset=0).perform()
        self.action.release().perform()
        
        submit = self.brower.find_element_by_xpath('//div[@class="fm-btn"]')
        submit.click()
        self.wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR,".site-nav-bd > ul.site-nav-bd-l > li#J_SiteNavLogin > div.site-nav-menu-hd > div.site-nav-user > a.site-nav-login-info-nick "))
        )

    def product_data(self,keyword):
        """ 爬取商品信息 """
        url = "https://list.tmall.com/search_product.htm?q="+urllib.parse.quote(keyword)
        self.brower.get(url)
        try:
            self.wait.until(
                            EC.presence_of_element_located((By.XPATH,'//div[@id="J_ItemList"]/div[contains(@class,"product")]'))
                        )
            doc = pq(self.brower.page_source)
            with open('taobao.html','w',encoding='utf-8') as f:
                f.write(self.brower.page_source)
            good_items = doc('#J_itemList .product').items()
            for item in good_items:
                good_title = item.find('.productTitle').text().replace('\n',"").replace('\r',"")
                good_status = item.find('.productStatus span:first-child').text().replace('\n','').replace('\r','')
                good_price = item.find('productPrice').text().replace('\n','')
                good_url = item.find('.productImg').attr('href')
                print(good_title+'   '+good_status+'   '+good_price+'   '+good_url+'\n')
            
        except:

            error = self.brower.find_element_by_xpath('//div[@class="searchTip"]')
            if error:
                print('找不到您想要的商品')
                return None
         
    def run(self,keyword):
        self.login()
        self.product_data(keyword)
        self.brower.close()

if __name__ == "__main__":
    product = tianmaospider()
    product.run('羽毛球')
