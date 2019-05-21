import requests
from bs4 import BeautifulSoup
import json,time,random

def get_soup_obj(url):
	url_obj = requests.get(url)
	soup = BeautifulSoup(url_obj.content,'html.parser')
	return soup

def get_second(city_aqi_item):
	items = dict()
	items['link'] = city_aqi_item
	city_aqi = requests.get(city_aqi_item)
	aqi_item = BeautifulSoup(city_aqi.content,'html.parser')
	aqi_items = aqi_item.find_all('div',{'class':'span1'})
	for item in aqi_items[:8]:
		value = item.find(class_='value').get_text()
		value = value.strip()
		print(value)
		key = item.find(class_='caption').get_text()
		key = key.strip()
		print(key)
		items[key] = value
	return items

def get_fistpage_and_secondpage(url,soup):
	city_aqi_list = []
	city_list = soup.find('div',{'class':'all'})
	cities = city_list.find_all('li')
	for tag in cities:
		city_dict = dict()
		city_name = tag.find('a').text.strip()
		city_link = tag.find('a')['href']
		city_aqi_item = url+city_link
		items = get_second(city_aqi_item)
		city_dict[city_name] = items
		city_aqi_list.append(city_dict)
		time.sleep(random.randint(0,3)+random.random())
	return city_aqi_list

def write_city_aqi(city_aqi_data):
	file_path = './dataFile/city_aqi.json'
	with open(file_path,'a+') as f:
		city_aqi_data = json.dumps(city_aqi_data,ensure_ascii = False,indent=4)
		f.write(city_aqi_data)
		f.close()


if __name__ == "__main__":

	#     需要分析的url
	url = 'http://www.pm25.in/'

	#     获得url的解析数据
	soup = get_soup_obj(url)

	#     获得从一级网址和二级网址获得的结果数据综合
	city_aqi_list = get_fistpage_and_secondpage(url, soup)

	#     对爬取到的热门城市名称、城市链接、城市的各种指数数据进行遍历
	for city_aqi in city_aqi_list:
		print(city_aqi)

	#     将得到的数据写入json文件
	write_city_aqi(city_aqi_list)