import requests
import random
import time
from apscheduler.schedulers.blocking import BlockingScheduler


def sendDanmu(content):
    """
    param：发送内容
    发送弹幕    
    """
    URL = "https://api.live.bilibili.com/msg/send"
    header = {
        "Cookie":"_uuid=12ECBC16-F059-C262-1327-7CDC7A4E388498161infoc; LIVE_BUVID=AUTO6315680287012312; sid=8gjlrnl0; buvid3=AB4B382F-5DD4-46A5-8BE9-8A0C496B1F11155840infoc; UM_distinctid=16d15cb9c95e5-01b1952ef6b2c6-3c604504-1fa400-16d15cb9c972b2; CURRENT_FNVAL=16; stardustvideo=1; rpdid=|(u~)RJmY|R)0J'ulY)|k)~YJ; CURRENT_QUALITY=64; DedeUserID=38329045; DedeUserID__ckMd5=1e2448eaa040530b; SESSDATA=6f37e28e%2C1575722985%2Cd6388bb1; bili_jct=622bd414de8b0f351810c1557450dddb; Hm_lvt_8a6e55dbd2870f0f5bc9194cddf32a02=1573132329,1573132442,1573384891,1573558322; __guid=166593518.2174130135193084000.1573560066933.4238; _dfcaptcha=99c80373f4d8f723dd86b853c89aea6f; monitor_count=2; Hm_lpvt_8a6e55dbd2870f0f5bc9194cddf32a02=1573569010",
        "Host":"api.live.bilibili.com",
        "Origin":"https://live.bilibili.com",   
        "Referer":"https://live.bilibili.com/21624186?visit_id=l1knacomixo",
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36"
    }
    data = {
        "color":"16777215",
        "fontsize":"25",
        "mode":"1",
        "msg":f"{content}",
        "rnd":"1573569001",
        "roomid":"21624186",
        "bubble":"0",
        "csrf_token":"622bd414de8b0f351810c1557450dddb",
        "csrf":"622bd414de8b0f351810c1557450dddb"
    }
    response = requests.post(URL,headers=header,data=data)

def main():
    arr = ['666','2333',"五五开","鸡你太美","python spider666"]
    content = random.choice(arr)
    sendDanmu(content)    

if __name__ == "__main__":
    sched = BlockingScheduler()
    sched.add_job(main, 'interval', seconds=5)
    sched.start()
