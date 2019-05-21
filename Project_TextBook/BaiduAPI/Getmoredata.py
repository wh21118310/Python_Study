import requests,pymysql,json
conn = pymysql.connect(host='localhost',user='root',passwd='123456' ,db='baidumap' ,charset='utf8')
cur = conn.cursor()
sql ='select uid from baidumap.city where id>0'
cur.execute(sql)
results = cur.fetchall()
def getjson(uid):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'}
    pa={
        'uid':uid,
        'scope':'2',
        'output':'json',
        'ak': 'itst7iD3oN9C2AfAFjYZaaq6ts9mFUVT'
    }
    r = requests.get("http://api.map.baidu.com/place/v2/detail",
                     params=pa,headers=headers)
    decodejson = json.loads(r.text)
    return decodejson
for row in results:
    uid = row[0]
    decodejson = getjson(uid)
    print (uid)
    info = decodejson['result']
    try:
        park = info['name']
    except:
        park = None
    try:
        location_lat = info['location']['lat']
    except:
        location_lat = None
    try:
        location_lng = info['location']['lng']
    except:
        location_lng = None
    try:
        address = info['address']
    except:
        address = None
    try:
        street_id = info['street_id']
    except:
        street_id = None
    try:
        telephone = info['telephone']
    except:
        telephone = None
    try:
        detail = info['detail']
    except:
        detail = None
    try:
        tag = info['detail_info']['tag']
    except:
        tag = None
    try:
        detail_url = info['detail_info']['detail_url']
    except:
        detail_url = None
    try:
        type = info['detail_info']['type']
    except:
        type = None
    try:
        overall_rating = info['detail_info']['overall_rating']
    except:
        overall_rating = None
    try:
        image_num = info['detail_info']['image_num']
    except:
        image_num = None
    try:
        comment_num = info['detail_info']['comment_num']
    except:
        comment_num = None
    try:
        key_words = ''
        key_words_list = info['detail_info']['di_review_keyword']
        for eachone in key_words_list:
            key_words = key_words + eachone['keyword'] + '/'
    except:
        key_words = None
    try:
        shop_hours = info['detail_info']['shop_hours']
    except:
        shop_hours = None
    try:
        alias = info['detail_info']['alias']
    except:
        alias = None
    try:
        scope_type = info['detail_info']['scope_type']
    except:
        scope_type = None
    try:
        scope_grade = info['detail_info']['scope_grade']
    except:
        scope_grade = None
    try:
        description = info['detail_info']['description']
    except:
        description = None
    sql = """INSERT INTO baidumap.park
    (park, location_lat, location_lng, address, street_id, uid, telephone, detail, tag, detail_url, type, overall_rating, image_num, 
    comment_num, keyword, shop_hours, alias, scope_type, scope_grade, description)
    VALUES
    (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);"""

    cur.execute(sql, (park, location_lat, location_lng, address, street_id, uid, telephone, detail, tag, detail_url,type, overall_rating, image_num, comment_num, key_words, shop_hours, alias, scope_type, scope_grade, description,))
    conn.commit()
cur.close()
conn.close()