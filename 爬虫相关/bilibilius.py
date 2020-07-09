import requests
from fake_useragent import UserAgent
import random
import json
import time
from pprint import pprint
from multiprocessing.dummy import Pool as ThreadPool
import mysql#自定义的mysql连接文件
import pymysql

conn = mysql.get_cursor()#获取mysql连接对象

cursor = conn.cursor()#获取mysql操作游标
ua = UserAgent()#使用随机的useragent
session = requests.Session()#创建会话
def make_mid():
    """ 生成用户mid """
    item = []
    for i in range(5214,5215):
        for j in range(i*100,(i+1)*100):
            item.append(str(j))
    return item

def get_proxy():
    """ 从代理池里获取随机代理ip """
    url = "http://127.0.0.1:5555/random"
    proxy = requests.get(url).text
    return proxy
    
def user_spider(mid):
    """ 获取各个up的信息 """
    headers = {
        'User-Agent':ua.random,
        'Refer': 'https://space.bilibili.com/' + mid + '?from=search&seid=' + str(random.randint(10000, 50000))
    }#生成请求头
    up_info_url = 'https://api.bilibili.com/x/space/acc/info?mid='+mid
    item = {}
    print("开始爬取用户{}\n".format(mid))
    try:
        
        proxy = get_proxy()
        if proxy is not None:   
            proxy = {
                'http': get_proxy(),
                'https':get_proxy()
            }#利用代理池生成随机的代理ip
        else:
            raise Exception("not get proxy")

        up_info_list = requests.get(up_info_url,headers=headers,proxies=proxy,timeout=2)
        if up_info_list.status_code == 200:
            up_info_list = up_info_list.json()

        if up_info_list['code'] == 0:
            up_info = up_info_list['data']
            item['mid'] = mid
            item['up_name'] = up_info['name']
            item['up_gender'] = up_info['sex']
            item['rank'] = up_info['rank']
            item['up_face'] = up_info['face']
            item['up_birth'] = up_info['birthday']
            item['up_sign'] = up_info['sign']
            item['up_level'] = up_info['level']
            
            
            vip_status = up_info['vip']['status']
            if vip_status == 1:
                item['up_vip'] = "年度大会员"
            elif vip_status == 0:
                item['up_vip'] = "普通用户"
            else:
                item['up_vip'] = "普通会员"
            # print(item)
            try:
                res = session.get("https://api.bilibili.com/x/space/upstat?mid="+mid,headers=headers,proxies=proxy).json()
                # print(res)
                viewinfo = session.get("https://api.bilibili.com/x/relation/stat?vmid="+mid,headers=headers,proxies=proxy).json()
                item['up_likes_num'] = res['data']['likes']
                item['up_fans_num'] = viewinfo['data']['follower']
                
                item['up_view_num'] = res['data']['article']['view']
                # try:
                cursor.execute("insert into bilibili_user_info(mid,name,sex,rank,face,birthday,sign,level, \
                    viptype,likes,fans,viewnum) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(item['mid'],item['up_name'],item['up_gender'], \
                        item['rank'],item['up_face'],item['up_birth'],item['up_sign'],item['up_level'],item['up_vip'],item['up_likes_num'],item['up_fans_num'],item['up_view_num']))
                conn.commit()
                # except:
                #     conn.rollback()
                pprint(item)
                print("*"*50)
            except Exception as e:
                print(e)

        else:
            print("没有该用户")
            print("*"*50)
    except Exception as e:
        print("重新爬取用户{}\n".format(mid))
        print("*"*50)
        return user_spider(mid)

if __name__ == "__main__":
    pool = ThreadPool(1)
    mid_list = make_mid()
    try:
        pool.map(user_spider,mid_list)
    except Exception as e:
        print(e)


    