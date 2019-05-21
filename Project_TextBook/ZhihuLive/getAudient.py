from pymongo import MongoClient
import requests
import json
import time
import random
client = MongoClient('localhost',27017)
db = client.zhihu_database
collection = db.live
def get_audience(live_id):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',
        'origin': 'https://www.zhihu.com',
        'referer': 'https://www.zhihu.com/lives',
        'authority': 'api.zhihu.com'}
    link = 'https://api.zhihu.com/lives/'+live_id+'/reviews?limit=10&offset=0'
    is_end = False
    while not is_end:
       r = requests.get(link,headers = headers)
       html = r.text
       decodejson = json.loads(html)
       decodejson['live_id'] = live_id
       db.live.audience.insert_one(decodejson)
       link = decodejson['paging']['next']
       is_end = decodejson['paging']['is_end']
       time.sleep(random.randint(2,3)+random.random())
for each_page in collection.find():
    for each in each_page['data']:
        live_id = each['live']['id']
        get_audience(live_id)