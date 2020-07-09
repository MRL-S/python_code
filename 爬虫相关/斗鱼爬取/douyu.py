from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait#显示等待
from selenium.webdriver.support import expected_conditions as EC
import time
import json

class Douyu():
    def __init__(self):
        self.driver = webdriver.PhantomJS(executable_path=r"E:\phantomjs\bin\phantomjs.exe")
        self.driver.get("https://www.douyu.com/directory/all")#请求斗鱼首页
        time.sleep(5)

    def get_content(self):
        """
        获取斗鱼首页相关信息
        """
        try:
            element = WebDriverWait(self.driver,10).until(
                #页面一直循环直到信息出现
                EC.presence_of_element_located((By.XPATH,'//section[@class="layout-Container"]'))
            )
            data_list = self.driver.find_elements(By.XPATH,'//section[@class="layout-Container"]//ul[@class="layout-Cover-list"]')#获取所需信息列表   
            all_data = []#用于存储全部的信息
            for data in data_list:
                all_info = data.find_elements(By.XPATH,'./li')
                for info in all_info:
                    item = {}#用于存储每一个直播间的相关信息
                    item['img_url'] = info.find_element(By.XPATH,'.//img[contains(@class,"DyImg-content")]').get_attribute('src')#获取直播间的照片地址
                    item['category'] = info.find_element(By.XPATH,'.//div[@class="DyListCover-info"][1]/span').text#获取直播间的分类
                    item['title'] = info.find_element(By.XPATH,'.//div[@class="DyListCover-info"][1]/h3').text#获取直播间的标题
                    item['hot'] = info.find_element(By.XPATH,'.//div[@class="DyListCover-info"][2]/span').text#获取直播间的热度
                    item['name'] = info.find_element(By.XPATH,'.//div[@class="DyListCover-info"][2]/h2').text#获取直播间主播的名字
                    all_data.append(item)
            # print(all_data)
        except Exception as e:
            print(e)
        return all_data
    
    def save_content(self,content):
        """
        存储数据为json
        """
        with open("douyu.json","a",encoding='utf-8') as f:
            json.dump(content,f,ensure_ascii=False,indent=2)
    
    def run(self):
        """
        执行程序
        """
        content = self.get_content()
        self.save_content(content)
        for i in range(2):
            #判断还有没下一页最多循环5页
            if self.driver.find_element(By.CLASS_NAME,'dy-Pagination-item-custom'):
                #判断有没有下一页
                self.driver.find_element(By.CLASS_NAME,'dy-Pagination-item-custom').click()
                content = self.get_content()#获取下一页数据
                self.save_content(content)#保存下一页的数据

    def __del__(self):
        self.driver.close()

if __name__ == "__main__":
    douyu = Douyu()
    douyu.run()