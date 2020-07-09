import requests

url = 'https://www.shanbay.com/api/v1/vocabtest/category/'
params = {'_':'1563673231336'}
headers = { 'user-agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'}
res = requests.get(url,params=params,headers=headers)
content = res.json()
choice_list = content['data']
list1 = [] 
for item in choice_list:
    list1.append(item[0])
choice = int(input('请选择词库0：GMAT 1：考研 2：高考 3：四级 4：六级 5：英专 6：托福 7：GRE 8：雅思 9：任意'))
params1 = {'category':list1[choice],'_':'1563673231336'}

res1 = requests.get(url,params=params1,headers=headers)
content1 = res1.json()
words_list = content1['data']
print(words_list)