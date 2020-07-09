import requests
import threading
from queue import Queue
from retrying import retry
import re
import openpyxl

class Tencentjob():
    def __init__(self,page):
        self.url = "https://careers.tencent.com/tencentcareer/api/post/Query"
        self.headers = {
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36"
        }
        self.page = page

    @retry(stop_max_attempt_number=5)
    def parse_url(self):
        """
        请求数据，获取json数据
        """
        print("正在爬取。。。。。")
        data = []
        for i in range(self.page):
            params = {
                'timestamp': '1592033198862',
                'countryId': '',
                'cityId': '',
                'bgIds': '',
                'productId': '',
                'categoryId': '',
                'parentCategoryId': '',
                'attrId': '',
                'keyword': '',
                'pageIndex': i,
                'pageSize': 10,
                'language': 'zh-cn',
                'area': 'cn'
            }
            response = requests.get(self.url,headers=self.headers,params=params,timeout=3)
            result = response.json()
            data.append(result)
        return data

    def get_content(self,jd):
        """
        获取相关职位信息
        """
        content = []
        for data in jd:
            data = data['Data']['Posts']
            for item in data:
                m = []
                m.append(item['RecruitPostName'])#获取事业名
                m.append(item['Responsibility'])#获取工作内容
                m.append(item['CountryName']+'|'+item['LocationName'])#获取工作地点
                m.append(item['LastUpdateTime'])#获取发布时间
                m.append(item['BGName'])#获取事业名
                # m.append(item['PostURL'])#获取发布url
                match = re.search(r'\d+',item['PostURL'])
                # print(item['PostURL'])
                # print(match.group(0))
                if len(match.group(0)) < 2:
                    #判断url是否正确：’http://careers.tencent.com/jobdesc.html?postId=‘+PostId
                    PostId = item['PostId']
                    m.append(item['PostURL'].replace(match.group(0),PostId))
                    # print(m[5])
                else:
                    m.append(item['PostURL'])#获取发布url
                content.append(m)
        return content

    def save_data(self,content):
        """
        存储数据到excel中
        """
        wb = openpyxl.Workbook()#创建工作簿
        sheet = wb.active#激活工作簿
        sheet.name = "tencentjobmessage"#创建名为tencentjobmessage的工作表
        sheet.append(["职位","主要工作","工作地点","发布时间","事业名","详情页面url"])#添加表格的表头
        try:
            for data in content:
                sheet.append(data)#将获取的工作信息添加进表中
            wb.save("tencentjobmessage.xlsx")
        except Exception as e:
            print(f"Error:{e}")
    
    def run(self):
        """
        启动方法
        """
        for i in range(10):
            data = self.parse_url()
            content = self.get_content(data)
            self.save_data(content)

if __name__ == "__main__":
    tencentjobspider = Tencentjob(10)
    tencentjobspider.run()