import re
import requests
import openpyxl

class News36kr_spider():
    def __init__(self):
        self.headers = {
            'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36',
            'Accept-Encoding':'gzip, deflate, br',
            'Accept-Language':'zh-CN,zh;q=0.9'
        }
        
        self.url = 'https://36kr.com/'

    def load_data(self,url):
        """
        可以复用的页面请求方法
        """
        response = requests.get(url,headers=self.headers)
        if response.status_code == 200:
            # print(response.headers)
            return response.content.decode("utf-8")
        else:
            raise ValueError("status_code:",response.status_code)
    
    def get_content(self,content):
        """
        筛选出有用的数据
        """
        m = re.findall(r'<a class="article-item-title weight-bold".*?>(.*?)</a></p>.*?>(.*?)</a>',content,re.S)
        # print(m)
        result = []
        for i in m:
            temp = []
            for j in i:
                temp.append(j)
            # print(temp)
            result.append(temp)
        return result
    
    def save_data(self,result):
        """
        保存到excel表中
        """
        wb = openpyxl.Workbook()
        sheet = wb.active
        sheet.title = "test"
        try:
            for row in result:
                sheet.append(row)
            wb.save("test.xlsx")    
        except Exception as r:
            print(r)
        
        
if __name__ == '__main__':
    test = News36kr_spider()

    content = test.load_data(test.url)
    result = test.get_content(content)
    test.save_data(result)