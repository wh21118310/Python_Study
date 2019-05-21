import re,requests,time
Count = 0
start = time.time()
exist_list = []
def scarcpy(url,depth = 1):
     global Count
     try:
         headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36', }
         link = requests.get('https://en.wikipedia.org/wiki/'+url,headers=headers,timeout = 20)
         html = link.text
     except Exception as e:
         print("Failed downloading and saving",url)
         print(e)
         exist_list.append(url)
         return None
     exist_list.append(url)
     link_list = re.findall('<a href="/wiki/([^:#<>]*?)".*?</a>',html)
     unique_list = list(set(link_list)-set(exist_list))
     for eachone in unique_list:
          Count += 1
          output = 'No.'+str(Count)+'\tDepth:'+str(depth)+'\t'+url+'-->'+eachone+"\n"
          print(output)
          #考虑到程序长时间爬取，不知道进度如何，所以一边存储一边打印，显示当前爬取结果
          with open('title.txt','a+',encoding='UTF-8') as f:
               f.write(output)
               f.close()
          if depth <2 :
             scarcpy(eachone,depth+1)
scarcpy('Wikipedia')
end = time.time()
print("Total Time :",end-start)