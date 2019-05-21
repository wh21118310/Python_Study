import requests
import jsonpath
import json
url = 'http://www.lagou.com/lbs/getAllCitySearchLabels.json'
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36',
    'Host':'www.lagou.com'
}
r = requests.get(url,headers = headers)
print(r.text)
jsonobj = json.loads(r.text)
city_list = jsonpath.jsonpath(jsonobj,'$..name')
file = open('city.json','w')
content = json.dumps(city_list,ensure_ascii=False,indent=4)
print(content)
file.write(content)
file.close()