from bs4 import BeautifulSoup
import requests
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36'
}
for i in range(2):
    urls = 'https://book.douban.com/top250?start='+str(25*i)
    res = requests.get(urls,headers=headers)
    bs = BeautifulSoup(res.text,'html.parser')
    datas = bs.find_all('div',class_='pl2')
    for data in datas:
        url = data.find('a')['href']
        resp = requests.get(url,headers=headers)
        bs1 = BeautifulSoup(resp.text,'html.parser')
        name = bs1.find(id='wrapper').find('span').text
        print(name)