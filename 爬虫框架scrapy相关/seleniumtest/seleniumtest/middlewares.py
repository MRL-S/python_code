# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/spider-middleware.html

from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from scrapy.http import HtmlResponse
from logging import getLogger
from selenium.webdriver.common.action_chains import ActionChains
import urllib
import time
class SeleniumMiddleware():
    def __init__(self,timeout=None):
        self.logger = getLogger(__name__)
        self.timeout = timeout
        # self.webdriver = webdriver.Chrome()
        self.webdriver = webdriver.PhantomJS(executable_path=r"E:\phantomjs\bin\phantomjs.exe",service_args=service_args)
        self.webdriver.set_window_size(1400,700)
        self.webdriver.set_page_load_timeout(self.timeout)
        self.wait = WebDriverWait(self.webdriver,self.timeout)
    def __del__(self):
        self.webdriver.close()

    def process_request(self,request,spider):
        """
        phantomjs抓取网页
        :param request: Request对象
        :pram spider: spider对象
        :return: HtmlResponse 
        """
        self.logger.debug("Chrome is Starting")
        page = request.meta.get('page',1)
        try:
            # if self.login_state is False:
            # action = ActionChains(webdriver)
            
            # self.webdriver.get(request.url)
            # self.wait.until(
            #     EC.presence_of_element_located((By.ID,"fm-login-id"))

            # ).send_keys("15298195937")
            # self.wait.until(
                
            #     EC.presence_of_element_located((By.ID,"fm-login-password"))

            # ).send_keys("10253uxtvop")
            # slider = self.wait.until(
            #     EC.presence_of_element_located((By.ID,"nc_1_n1z"))
            # )
            # action.click_and_hold(on_element=slider).perform()
            # action.move_by_offset(xoffset=280,yoffset=0).perform()
            # action.release().perform()
            # button = self.webdriver.find_element_by_class_name('fm-btn')
            # button.click()
            # self.login_state = True
            # base_urls = 'http://s.taobao.com/search?q='
            # keyword = 'ipad'
            # url = base_urls+urllib.parse.quote(keyword)
            self.webdriver.get(request.url)
            if page>1:
                input = self.wait.until(
                    EC.presence_of_element_located((By.CSS_SELECTOR,'#mainsrp-pager > div > div > div > div.form > input'))
                )
                submit = self.wait.until(
                    EC.element_to_be_clickable((By.CSS_SELECTOR,"#mainsrp-pager > div > div > div > div.form > span.btn.J_Submit"))
                )
                input.clear()
                input.send_keys(page)
                submit.click()
                # print(self.webdriver.current_url)
            self.wait.until(
                EC.text_to_be_present_in_element((By.CSS_SELECTOR,"#mainsrp-pager > div > div > div > ul > li.item.active > span"),str(page))
            )
            self.wait.until(
                EC.presence_of_element_located((By.CSS_SELECTOR,"#mainsrp-itemlist > div > div > div:nth-child(1)"))
            )
            return HtmlResponse(url=request.url,body=self.webdriver.page_source,request=request,encoding='utf-8',status=200)
        except TimeoutException:
            return HtmlResponse(request.url,status=500,request=request)
        
    @classmethod
    def from_crawler(cls,crawler):
        return cls(
            timeout=crawler.settings.get("SELENIUM_TIMEOUT"),
            service_args=crawler.settings.get("PHANTOMJS_SERVICE_ARG")
        )