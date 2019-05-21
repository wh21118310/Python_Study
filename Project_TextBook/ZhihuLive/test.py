#ajax请求 https://api.zhihu.com/lives/homefeed?includes=live&limit=10&offset=[以10为单位量]
#ajax请求 https://api.zhihu.com/lives/938729029810073600/reviews?limit=10&offset=[以10为单位量]
#获取所有Live
import requests
from pymongo import MongoClient
import json
import time
import random
start = time.time()
client = MongoClient('localhost', 27017)
db = client.zhihu_database
collection = db.live
def scrapy(link): #获取所有Live
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',
        'origin': 'https://www.zhihu.com',
        'referer': 'https://www.zhihu.com/lives',
        'authority': 'api.zhihu.com'
    }
    r = requests.get(link, headers=headers)
    return (r.text)
link = "https://api.zhihu.com/lives/homefeed?includes=live"
is_end = False
while not is_end:
    html = scrapy(link)
    decodejson = json.loads(html)
    collection.insert_one(decodejson)
    link = decodejson['paging']['next']
    is_end = decodejson['paging']['is_end']
    time.sleep(random.randint(2, 3) + random.random())
end = time.time()
print("Total Time: ", end-start)

