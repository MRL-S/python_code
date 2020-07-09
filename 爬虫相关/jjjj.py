import time
from urllib.request import urlretrieve
import subprocess
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
#创建新的Selenium driver
driver = webdriver.Chrome()

# 用Selenium试试Firefox浏览器:
# driver = webdriver.Firefox()

driver.get("http://www.amazon.com/War-Peace-Leo-Nikolayevich-Tolstoy/dp/1427030200")
time.sleep(4)
# 单击图书预览按钮
# while  driver.find_element_by_xpath('//span[@class="a-button-inner"][1]'):
#     driver.find_element_by_xpath('//span[@class="a-button-inner"][1]').click()
driver.find_element_by_id("imgBlkFront").click() 
imageList = set()
# 等待页面加载完成

# 当向右箭头可以点击时,开始翻页
time.sleep(4)
while "pointer" in driver.find_element_by_id("sitbReaderRightPageTurner").get_attribute("style"):
    driver.find_element_by_id("sitbReaderRightPageTurner").click()
    time.sleep(5)
    # 获取已加载的新页面(一次可以加载多个页面,但是重复的页面不能加载到集合中)
    pages = driver.find_elements_by_xpath("//div[@class='pageImage']/div/img")
    for page in pages:
        image = page.get_attribute("src")
        imageList.add(image)
driver.quit()

# 用Tesseract处理我们收集的图片URL链接
for image in sorted(imageList):
    # 保存图片
    urlretrieve(image, "page.jpg")
    p = subprocess.Popen(["tesseract", "page.jpg", "page"], stdout=subprocess.PIPE,stderr=subprocess.PIPE)
    f = open("page.txt", "r",encoding="utf-8")
    p.wait() 
    print(f.read())