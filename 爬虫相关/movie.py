import requests, random,openpyxl
from bs4 import BeautifulSoup

wb = openpyxl.Workbook()
sheet = wb.active
sheet.title='top 250'
sheet['A1'] = '排名'
sheet['B1'] = '电影名'
sheet['C1'] = '评分'
sheet['D1'] = '推荐语'
sheet['E1'] = 'url'
header = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'
}
for x in range(10):
    url = 'https://movie.douban.com/top250?start=' + str(x*25) + '&filter='
    res = requests.get(url,headers=header)
    bs = BeautifulSoup(res.text,'html.parser')
    bs = bs.find('ol',class_='grid_view')
    for titles in bs.find_all('li'):
        num = titles.find('em',class_='').text
        title = titles.find('span',class_='title').text
        comment = titles.find('span',class_='rating_num').text
        url_movie = titles.find('a')['href']
        if titles.find('span',class_='inq') !=None:
            tes = titles.find('span',class_='inq').text
            sheet.append([num,title,comment,tes,url_movie])
            print(num + '.' + title + '——' + comment + '\n' + '推荐语：' + tes +'\n' + url_movie)
        else:
            sheet.append([num,title,comment,' ',url_movie])
            print(num + '.' + title + '——' + comment + '\n' +'\n' + url_movie)
wb.save('top250_movie.xlsx')    