#encoding:utf-8
import requests
import json,jsonpath
# def getjson(loc,page_num = 0):
#     #通过百度WEB服务API获取省份中拥有公园的城市
#     headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'}
#     pa = {'query':'公园',
#           'region':loc,
#           'scope':2,
#           'page_size':20,
#           'page_num':page_num,
#           'output':'json',
#           'ak':'itst7iD3oN9C2AfAFjYZaaq6ts9mFUVT'}
#     r = requests.get('http://api.map.baidu.com/place/v2/search',params=pa,headers=headers)
#     decodejson = json.loads(r.text)
#     return decodejson
# jsondata = getjson('北京市')
# js = json.dumps(jsondata,sort_keys=False,separators=(',',':'),indent=4,ensure_ascii=False)
# with open("jsondata.json","a+",encoding="UTF-8") as f:
#     f.write(str(js))
#     f.close()
# province_list = ['江苏省','山东省','浙江省','福建省','江西省',
#                  '广东省','广西壮族自治区','云南省','西藏自治区','新疆维吾尔族自治区',
#                  '宁夏回族自治区','四川省','湖北省','湖南省','河北省','河南省',
#                  '青海省','甘肃省','内蒙古自治区','陕西省','山西省','吉林省','辽宁省',
#                  '黑龙江省','安徽省','海南省','贵州省']
# for eachone in province_list:
#     decodejson = getjson(eachone)
#     for eachcity in decodejson['results']:
#         city = eachcity['name']
#         num = eachcity['num']
#         output = '\t'.join([city,str(num)])+'\r\n'
#         with open('cities.txt','a+',encoding='UTF-8') as f:
#             f.write(output)
#             f.close()
# decodejson = getjson('全国')
# six_cities_list = ['北京市','上海市','重庆市','天津市','香港特别行政区','澳门特别行政区','台湾省']
# for eachone in decodejson['results']:
#     city = eachone['name']
#     num = eachone['num']
#     if city in six_cities_list:
#         output = '\t'.join([city,str(num)])+'\r\n'
#         with open('cities.txt','a+',encoding='UTF-8') as f:
#             f.write(output)
#             f.close()