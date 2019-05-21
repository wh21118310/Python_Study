import  requests
import datetime
from bs4 import BeautifulSoup
import re
import time
def get_page(link,headers):
    r = requests.get(link,headers=headers)
    html = r.content
    html = html.decode('utf-8')
    soup = BeautifulSoup(html,'lxml')
    return soup
def get_data(post_list):
     date_list = []
     for post in post_list:
         title = post.find('div', class_='titlelink box').text.strip()
         title = re.sub('\n|\xa0|zt|','',title)
         post_link = post.find('div',class_='titlelink box').a['href']
         post_link = 'https://bbs.hupu.com'+post_link
         author = post.find('div',class_='author box').a.text.strip()
         author_page = post.find('div',class_='author box').a['href']
         start_date = post.find('div',class_='author box').contents[5].text.strip()
         start_date = datetime.datetime.strptime(start_date,'%Y-%m-%d').date()
         reply_view = post.find('span',class_='ansour box').text.strip()
         reply = reply_view.split('/')[0].strip()
         view = reply_view.split('/')[1].strip()
         reply_time = post.find('div',class_='endreply box').a.text.strip()
         last_reply = post.find('div',class_='endreply box').span.text.strip()
         if ':' in reply_time:
              date_time = str(datetime.date.today())+" "+reply_time
              date_time = datetime.datetime.strptime(date_time,'%Y-%m-%d %H:%M')
         else :
             date_time = datetime.datetime.strptime('2017-'+reply_time,'%Y-%m-%d').date()
         date_list.append([title,post_link,author,author_page,start_date,reply,view,last_reply,date_time])
     return date_list
from pymongo import MongoClient
class MongoAPI(object):
    def __init__(self,db_ip,db_port,db_name,table_name):
        self.db_ip =db_ip
        self.db_port = db_port
        self.db_name = db_name
        self.table_name = table_name
        self.conn = MongoClient(host=self.db_ip,port=self.db_port)
        self.db = self.conn[self.db_name]
        self.table = self.db[self.table_name]
    def get_one(self,query):
        return self.table.find_one(query,projection={'_id':False})
    def get_all(self,query):
        return self.table.find(query)
    def add(self, kv_dict):
        return self.table.insert(kv_dict)
    def delete(self,query):
        return self.table.delete_many(query)
    def check_exist(self,query):
        ret = self.table.find_one(query)
        return ret !=None
    #没有则重建
    def update(self,query,kv_dict):
        self.table.update_one(query,{
            "$set":kv_dict
        },upsert=True)
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36', }
hupu_post = MongoAPI('localhost',27017,'hupu','post')
for i in range(1,101):
    link = "https://bbs.hupu.com/bxj-" +str(i)
    soup = get_page(link, headers)
    post_all = soup.find('ul', class_='for-list')
    post_list = post_all.find_all('li')
    data_list = get_data(post_list)
    for each in data_list:
      hupu_post.update(
          {'post_link':each[1]},
         {
            'title':each[0],
            'post_link':each[1],
            'author':each[2],
            'auhthor_page':each[3],
            'start_date':str(each[4]),
            'reply':each[5],
            'view':each[6],
            'last_reply':each[7],
            'last_reply_time':str(each[8])
         })
    time.sleep(2)
    print('第',i,'页获取完成，休息2秒')
#实战出现的问题：当采集到第10页，出现报错AttributeError: 'NoneType' object has no attribute 'find_all'