import requests
from lxml import etree
from retrying import retry

class Qiushispider():
    def __init__(self):
        self.headers = {
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36"
        }
        self.url = "http://www.qiushibaike.com/8hr/page/{}/"
    @retry(stop_max_attempt_number=5)#最大重试次数5次
    def parse_url(self,url):
        """
        发送请求获取使用etree处理html
        """
        print("数据爬取中。。。。。。。")
        response = requests.get(url,headers=self.headers,timeout=10)
        html = response.text
        return etree.HTML(html)
    
    def get_content(self,html):
        """
        获取糗事百科的相关数据
        """
        data_list = html.xpath('//div[@class="recmd-right"]')
        for data in data_list:
            img_url = data.xpath('.//a[@class="recmd-user"]/img/@src')[0] if len(data.xpath('.//a[@class="recmd-user"]/img/@src')[0])>0 else None
            #获取头像图片的前缀
            if img_url is not None and not img_url.startswith("http:"):
                img_url = "http:"+img_url#获取头像图片的url
                print(img_url)
            username = data.xpath('.//a[@class="recmd-user"]/span[@class="recmd-name"]/text()')[0]#获取用户名
            print(username)
            content = data.xpath('./a[@class="recmd-content"]/text()')[0] if len(data.xpath('./a[@class="recmd-content"]/text()')[0])>0 else None#获取内容
            print(content)
            start_num = ''.join(data.xpath('./div[1]/div[1]/span/text()'))#获取点赞数和评论数
            print(start_num)

    def run(self):
        """
        执行任务
        """
        html = self.parse_url(self.url.format(1))#请求url
        self.get_content(html)#爬取数据

if __name__ == "__main__":
    qiushi = Qiushispider()
    qiushi.run()