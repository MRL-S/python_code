import requests,random,csv,smtplib
from email.mime.text import MIMEText
from email.header import Header
from bs4 import BeautifulSoup
from urllib.request import quote
import schedule

account = input('请输入你的邮箱：')
pwd = input('请输入密码：')
receiver = input('请输入收件人邮箱：')
def download_url():
    csv_file = open('movielist.csv','w',newline='',encoding='utf-8')
    writer = csv.writer(csv_file)
    for x in range(10):
        url = 'https://movie.douban.com/top250?start=' + str(x*25) + '&filter='
        res = requests.get(url)
        bs = BeautifulSoup(res.text,'html.parser')
        bs = bs.find('ol',class_='grid_view')
        for titles in bs.find_all('li'):
            title = titles.find('span',class_='title').text
            list1 = [title]
            writer.writerow(list1)
    csv_file.close()
    read_file = open('movielist.csv','r',newline='',encoding='utf-8')
    reader = csv.reader(read_file)
    i = 0
    movie_list = []
    for data in reader:
        movie_list.append(data)
    read_file.close()    
    a = random.sample(movie_list,3)
    watch_list = []
    for movies in a:
        movie = movies[0]
        gbkmovie = movie.encode('gbk')
        urlsearch = 'http://s.ygdy8.com/plus/so.php?typeid=1&keyword='+quote(gbkmovie)
        res = requests.get(urlsearch)
        res.encoding='gbk'
        soup_movie = BeautifulSoup(res.text,'html.parser')
        urlpart = soup_movie.find('div',class_='co_content8').find_all('table')
        
        if urlpart:
            urlpart=urlpart[0].find('a')['href']
            urlmovie='https://www.ygdy8.com/'+urlpart
            
            content=movie+'\n'+urlmovie
            watch_list.append(content)
        else:
            content='没有'+movie+'的下载链接'
            watch_list.append(content)
    return(watch_list)

def send_mail(watch_list):
    global account,pwd,receiver
    host = 'smtp.qq.com'
    qqmail = smtplib.SMTP()
    qqmail.connect(host,25)

    qqmail.login(account,pwd)

    msg = '\n'.join(watch_list)
    content = MIMEText(msg,'plain','utf-8')
    try:
        qqmail.sendmail(account,receiver,content.as_string())
        print('发送成功')
    except:
        print('发送失败')
    qqmail.quit()

def execute():
    watch_list = download_url()
    send_mail(watch_list)

schedule.every().friday.do(execute)
while True:
    schedule.run_pending()
    time.sleep(1)