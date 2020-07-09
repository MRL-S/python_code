from gevent import monkey
monkey.patch_all()
from gevent.queue import Queue
import requests,gevent,csv
from bs4 import BeautifulSoup

url1 = 'http://cd.xiaozhu.com/'
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'
}
proxies = {"https": "https://163.204.243.51:9999"} 
task_list = []
queue = Queue()
for i in range(1,4):
    url2 = url1+'search-duanzufang-p'+str(i)+'-0/'
    res1 = requests.get(url2,headers=headers,proxies=proxies)
    bs1 = BeautifulSoup(res1.text,'html.parser')
    datas = bs1.find('ul',class_='pic_list clearfix').find_all('li')
    for data in datas:
        url_fang = data.find('a',class_='resule_img_a')['href']
        queue.put_nowait(url_fang)
def mission():
    while not queue.empty():
        url3 = queue.get_nowait()
        res2 = requests.get(url3,headers=headers,proxies=proxies)
        bs2 = BeautifulSoup(res2.text,'html.parser')
        title = bs2.find('div',class_='pho_info').find('em').text
        address = bs2.find('div',class_='pho_info').find('span',class_='pr5').text.strip()
        price = bs2.find('div',id='pricePart').text.replace('\n','')
        
        all_detail = bs2.find('ul',class_='house_info clearfix').find_all('li')
        detail1 = all_detail[0].find('h6',class_='h_ico1').text
        detail2 = all_detail[0].find('p').text.split(' ')
        words = [s for s in detail2 if s!=''] 
        area = words[0].split('：')[1]
        house_type = words[1].split('：')[1]
        live_num = all_detail[1].find('h6',class_='h_ico2').text
        bed_num = all_detail[2].find('h6',class_='h_ico3').text
        bed_size = all_detail[2].find('p').text.replace(' ','').replace('\n',' ')
        writer.writerow([title,url3,address,price,detail1,area,house_type,live_num,bed_num,bed_size])

file = open('xiaozhu.csv','w',newline='',encoding='utf-8')
writer = csv.writer(file)
writer.writerow(['名字','URL','地址','价格','出租情况','面积','户型','宜住人口','床数','床大小'])
for i in range(5):
    task = gevent.spawn(mission)
    task_list.append(task)
gevent.joinall(task_list)
file.close()