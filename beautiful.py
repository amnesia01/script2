import requests
#r = requests.get('https://unsplash.com')
#print(r.text)

from bs4 import BeautifulSoup  #导入BeautifulSoup 模块

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36'}  #给请求指定一个请求头来模拟chrome浏览器
web_url = 'https://unsplash.com'
r = requests.get(web_url, headers=headers) #像目标url地址发送get请求，返回一个response对象
all_a = BeautifulSoup(r.text, 'lxml').find_all('a', class_='cV68d')  #获取网页中的class为cV68d的所有a标签
for a in all_a:
    img_str = a['style']
    #print(a['style']) #循环获取a标签中的style
    print(img_str[img_str.index('"') + 1: img_str.index('"', img_str.index('"') + 1)])
