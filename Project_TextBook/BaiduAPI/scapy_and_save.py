import json,requests,pymysql
city_list = list()
with open('cities.txt','r',encoding='UTF-8') as txt_file:
    for eachLine in txt_file:
        if eachLine != '' and eachLine !='\n':
            fileds = eachLine.split('\t')
            city = fileds[0]
            city_list.append(city)
    txt_file.close()
conn = pymysql.connect(host='localhost',user='root',passwd = '123456',db = 'baidumap',charset='utf8')
cur = conn.cursor()
def getjson(loc, page_num=0):
        # 通过百度WEB服务API获取省份中拥有公园的城市
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'}
        pa = {'query': '公园',
              'region': loc,
              'scope': 2,
              'page_size': 20,
              'page_num': page_num,
              'output': 'json',
              'ak': 'itst7iD3oN9C2AfAFjYZaaq6ts9mFUVT'}
        r = requests.get('http://api.map.baidu.com/place/v2/search', params=pa, headers=headers)
        decodejson = json.loads(r.text)
        return decodejson
for eachcity in city_list:
    not_last_page = True
    page_num = 0
    while not_last_page:
        decodejson = getjson(eachcity,page_num)
        print(eachcity,page_num)
        if decodejson['results']:
            for eachone in decodejson['results']:
                try:
                    park = eachone['name']
                except:
                    park = None
                try:
                    location_lat = eachone['location']['lat']
                except:
                    location_lat = None
                try:
                    location_lng = eachone['location']['lng']
                except:
                    location_lng = None
                try:
                    address = eachone['address']
                except:
                    address = None
                try:
                    uid = eachone['uid']
                except:
                    uid = None
                try:
                    stree_id = eachone['street_id']
                except:
                    stree_id = None
                sql = """ insert into baidumap.city(city, park, location_lat, local_lng, adress, street_id, uid) 
                values (%s,%s,%s,%s,%s,%s,%s);"""
                cur.execute(sql,(eachcity,park,location_lat,location_lng,address,stree_id,uid))
                conn.commit()
            page_num+=1
        else:
            not_last_page = False
cur.close()
conn.close()

                


