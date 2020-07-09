import requests
import urllib.parse
import pprint
def get_url_page(url):
    """
    url:图片网址
    获取网页数据
    """
    response = requests.get(url).content.decode('utf-8')#向服务器请求数据
    return response

def find_in_page(page,startpart,endpart):
    """
    page:每条网页数据
    startpart:匹配img的url的头字符
    endpart：匹配img的url的尾字符
    提取出img的完整url
    """
    img_url_list = []
    end = 0
    while page.find(startpart,end) != -1:
        start = page.find(startpart,end)+len(startpart)
        end = page.find(endpart,start)
        url = page[start:end]
        img_url_list.append(url)
    return img_url_list

def pages_from_url(search_name):
    """
    search_name:要查找的相关的图片
    获取每页中所有的数据
    """
    data_list = []
    name = urllib.parse.quote(search_name)
    url = 'https://www.duitang.com/napi/blog/list/by_search/?kw={}&start={}&limit=100'
    for i in range(0,1000,100):
        whole_url = url.format(name,i)#url拼接
        response = get_url_page(whole_url)#向服务器请求数据
        data_list.append(response)
    return data_list

def find_all_img_url(data):
    """
    data:pages_from_url的返回列表
    获取所有img的url
    """
    img_url_list = []# 全部的img地址
    for page in data:
        url = find_in_page(page,'path":"','"')
        img_url_list.extend(url) 
    return img_url_list

def download_img(url,num):
    """
    url_list:find_all_img_url 的返回列表
    下载img
    """
    res = requests.get(url)
    path = "tony_img/"+str(num)+".jpg"
    with open(path,'wb+') as f:
        f.write(res.content)
   
        
def main(label):
    res = pages_from_url(label)
    img_url_list = find_all_img_url(res)
    print(img_url_list)
    num = 0
    for url in img_url_list:
        print(url)
        num += 1
        print("正在下载第{}张图片".format(num))
        download_img(url,num)
if __name__ == '__main__':
    main("杨幂")