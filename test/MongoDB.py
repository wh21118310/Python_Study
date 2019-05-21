import requests
import datetime
from bs4 import BeautifulSoup
from pymongo import MongoClient
client = MongoClient('localhost',27017)
db  = client.blog_database
collection = db.blog
link = 'http://www.santostang.com/'
headers = {'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'}
r = requests.get(link,headers = headers,timeout = 30)
soup = BeautifulSoup(r.text,'lxml')
title_list = soup.find_all("h1",class_='post-title')
for eachone in title_list:
    url = eachone.a['href']
    title = eachone.a.text.strip()
    post = {
        'url':url,
        'title':title,
        'data':datetime.datetime.utcnow()
    }
    collection.insert_one(post)
