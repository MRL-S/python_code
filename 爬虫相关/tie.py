import requests
from lxml import etree
import json
class Tieba_spider():
    def __init__(self,keywords):
        self.keywords = keywords
        self.headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'
}
    
    def get_total_url_list(self):
        '''获取所有的urllist'''
        url = "https://tieba.baidu.com/f?kw="+self.keywords+"&ie=utf-8&pn={}&"
        url_list = []
        for i in range(1): #通过循环拼接100个url
            url_list.append(url.format(i*50))
        return url_list #返回100个url的urllist

    def parse_url(self,url):
        """
        请求服务器获得响应，并用etree处理html
        """
        response = requests.get(url,headers=self.headers)#发送请求
        html = response.text#获取html字符串
        print(html)
        html = etree.HTML(html)#获取element的html
        return html
    
    def get_title_href(self,html):
        """
        获取标题和地址
        """
        html = self.parse_url(html)
        # print(etree.tostring(html).decode('utf-8'))
        data_list = html.xpath('//ul[@id="thread_list"]')#分组
        # print(data_list)
        item_list = []
        # for data in data_list:
        #     title = data.xpath('./a/text()')
        #     title = title[0] if len(title)>0 else None#tiba标题
        #     href = "https://tieba.baidu.com/"+data.xpath('./a/@href') if len(data.xpath('./a/@href'))>0 else None#tiba详情页面url
        #     item = {'href':href,'title':title}
        #     item_list.append(item)
        return item_list
    
    def get_img(self,url):
        """
        获取img图片url
        """
        html = self.parse_url(url)
        img_data = html.xpath('//img[@class="BDE_Image"]/@src')#图片地址
        return img_data

    def save_item(self,item):
        """
        保存img的url
        """
        with open("tibaspider.txt","a") as f:
            f.write(json.dumps(item,ensure_ascii=False,indent=2))
            f.write("\n")
        
    def run(self):
        """
        运行全部方法
        """
        url_list = self.get_total_url_list()
        # print(url_list)
        for url in url_list:
            title_href = self.get_title_href(url)
            # print(title_href)
            # for item in title_href:
            #     print(item)
            #     item['img']=self.get_img(item['href'])
            #     self.save_item(item)

if __name__ == "__main__":
    tibaspider = Tieba_spider('猫')
    tibaspider.run()