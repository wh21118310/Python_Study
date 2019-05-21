import requests,csv,time,random
from bs4 import BeautifulSoup
def outputOneCommentResult(page_id,soup,output_list):
    for item in soup.find(id='shop-all-list').ul:
        try:
            title = item.find(class_='tit').a.text.strip()
        except:
            title = ''
        try:
            link = item.find(class_='tit').a['href']
        except:
            link = ''
        try:
            star = item.find(class_='comment').span['title']
        except:
            star = ''
        try:
            comment_list = item.find(class_='review-num')['href']
        except:
            comment_list = ''
        try:
            comment = item.find(class_='review-num').b.text.strip()
        except:
            comment = ''
        try:
            price = item.find(class_='mean-price').b.text.strip()
        except:
            price = ''
        try:
            tag = item.find(class_='tag').text.strip()
        except:
            tag = ''
        try:
            address = item.find(class_='addr').text.strip()
        except:
            address = ''
        try:
            commentlist = item.find(class_='comment-list').text.strip()
            commentlist = commentlist.replace('\n','|')
        except:
            commentlist = ''
        if title != "":
            output_list.append([str(page_id),title,link,star,comment_list,comment,price,tag,address,commentlist])
    return output_list
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36',
    'Host':'www.dianping.com',
}
start = time.time()
for i in range(1,51):
    link = 'http://www.dianping.com/shenzhen/ch10/p'+str(i)
    r = requests.get(link,headers = headers)
    soup = BeautifulSoup(r.text,'lxml')
    output_list = []
    output_list = outputOneCommentResult(i,soup,output_list)
    print(output_list)
    with open('resurant_list.csv','a+',encoding='UTF-8',newline='') as f:
        spamwriter = csv.writer(f,dialect='excel')
        spamwriter.writerows(output_list)
    time.sleep(random.randint(0,1)+random.random())
end = time.time()
print('Total Time: ',end-start)

            