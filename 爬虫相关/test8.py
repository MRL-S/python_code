import requests
from urllib.parse import urlencode
import os
from hashlib import md5
from multiprocessing.pool import Pool

headers = {
    'referer':'https://www.toutiao.com/search/?keyword=%E8%A1%97%E6%8B%8D',
    'user-agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36',
    'x-requested-with':'XMLHttpRequest'
}
def get_page(offset):
    params = {
        'aid':'24',
        'app_name':'web_search',
        'offset':offset,
        'format':'json',
        'keyword':'街拍',
        'autoload':'true',
        'count':'20',
        'en_qc':'1',
        'cur_tab':'1',
        'from':'search_tab',
        'pd':'synthesis',
        'timestamp':'1567236078140'
    }
    url = 'http://www.toutiao.com/search_content/?' + urlencode(params)
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
    except requests.ConnectionError:
        return None

def get_image(json):
    if json.get('data'):
        for item in json.get('data'):
            if not item.get('title'):
                title = 'sorry'
                continue
            title = item.get('title')
            if item.get('image_list'):
                images = item.get('image_list')
                for image in images:
                    yield {
                    'image':'http:'+image.get('url'),
                    'title':title
                    }

def save_image(item):
    if not os.path.exists(item.get('title')):
        os.mkdir(item.get('title'))
    try:
        response = requests.get(item.get('image'))
        if response.status_code == 200:
            file_path = '{0}/{1}.{2}'.format(item.get('title'),md5(response.content).hexdigest(),'jpg')
            if not os.path.exists(file_path):
                with open(file_path,'wb') as f:
                    f.write(response.content)
            else:
                print('Already Downloaded',file_path)
    except requests.ConnectionError:
        print('Failed to save Image')

def main(offset):
    json = get_page(offset)
    for item in get_image(json):
        print(item)
        save_image(item)

GROUP_START = 1
GROUP_END = 20
if __name__ == '__main__':
    pool = Pool()
    groups = [x*20 for x in range(GROUP_START,GROUP_END+1)]
    pool.map(main,groups)
    pool.close()
    pool.join()