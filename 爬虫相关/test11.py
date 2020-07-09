from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from urllib.parse import quote
from pyquery import PyQuery as pq
import pymysql
from multiprocessing.pool import Pool

browser = webdriver.Chrome()
wait = WebDriverWait(browser,10)
keyword = 'ipad'

def index_page(page):
    print('正在爬取第',page,'页')
    try:
        url = 'http://s.taobao.com/search?q='+quote(keyword)
        browser.get(url)
        if page>1:
            input = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR,'#mainsrp-pager div.form>input')))
            submit = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,'#mainsrp-pager div.form>span.btn.J_Submit')))
            input.clear()
            input.send_keys(page)
            submit.click()
            input1 = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR,'div.static-form #J_Form div.username-field>input.login-text')))
            input2 = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR,'div.static-form #J_Form div.pwd-field>input.login-text')))
            submit1 = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,'div.static-form #J_Form div.submit>button.J_Submit')))
            input1.clear()
            input1.send_keys('力量之源power')
            input2.send_keys('10253uxtvop')
            submit1.click()
        wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR,'#mainsrp-pager li.item.active>span'),str(page)))
        wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR,'.m-itemlist .items .item')))
        get_products()
    except TimeoutException:
        index_page(page)

def get_products():
    html = browser.page_source
    doc = pq(html)
    items = doc('mainsrp-itemlist .items .item').items()
    for item in items:
        product = {
            'image':item.find('.pic .img').attr('data-src'),
            'price':item.find('.price').text(),
            'deal':item.find('deal-cnt').text(),
            'shop':item.find('.shop').text(),
            'location':item.find('.location').text()
        }
        print(product)
        save_to_sql(product)

db = pymysql.connect(host='localhost',user='root',password='',port=3306,db='test')
cursor = db.cursor()
def save_to_sql(result):
    table = 'products'
    keys = ','.join(result.keys())
    values = ','.join(['%s']*len(result))
    sql = 'insert into {table}({keys}) values ({values})'.format(table=table,keys=keys,values=values)
    try:
        if cursor.execute(sql,tuple(result.values())):
            print('Successful')
            db.commit()
    except:
        print('Failed')
        db.rollback()
    db.close()

if __name__ == '__main__':
    pool = Pool()
    group = [x for x in range(1,5)]
    pool.map(index_page,group)
    pool.close()
    pool.join()

