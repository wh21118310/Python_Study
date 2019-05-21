import requests
from bs4 import  BeautifulSoup
import time
import csv
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
Type = sys.getfilesystemencoding()

headers = {'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'}
for i in range(1,2):
    link1 =  'https://beijing.anjuke.com/sale/p'
    link = link1+str(i)
    r = requests.get(link,headers = headers)
    soup = BeautifulSoup(r.text,'lxml')
    house_list = soup.find_all('li',class_='list-item')
    for house in house_list:
      x = list()
      name = house.find('div',class_ = 'house-title').a.text.strip()
      x.append(name)
      price = house.find('span',class_='price-det').strong.text.strip()
      x.append(price)
      no_room = house.find('div',class_='details-item').contents[1].text.strip()
      x.append(no_room)
      area = house.find('div',class_='details-item').contents[3].text.strip()
      x.append(area)
      floor = house.find('div',class_='details-item').contents[5].text.strip()
      x.append(floor)
      year = house.find('div',class_='details-item').contents[7].text.strip()
      x.append(year)
      price_area = house.find('span', class_='unit-price').text.strip()
      x.append(price_area)
      broker = house.find('span',class_='brokername').text.strip()
      broker = broker[1:]
      x.append(broker)
      address = house.find('span',class_='comm-address').text.strip()
      address = address.replace('\xa0\xa0\n                    ','')
      x.append(address)
      tag_list = house.find_all('span',class_='item-tags')
      tags = [i.text for i in tag_list]
      x.append([ i.text for i in tag_list])
      with open('test.csv','a+',encoding='gbk',newline='') as f:
          w = csv.writer(f)
          w.writerow(x)
      print(name, price, price_area, no_room, area, floor, year, broker, address, tags, "\n")
    time.sleep(3)
