from multiprocessing import Process,Queue
import time
import requests
link_list = []
with open('alexa.txt','r',encoding="utf-8") as file:
    file_list = file.readlines()
    for eachone in file_list:
        link = eachone.split('\t')[0]
        link = link.replace('\n','')
        link_list.append(link)
start = time.time()
class Myprocess(Process):
        def __init__(self,q):
            Process.__init__(self)
            self.q = q
        def run(self):
            print("Starting ",self.pid)
            while not self.q.empty():
                crawler(self.q)
            print("Exiting ",self.pid)
def crawler(q):
    url = q.get(timeout = 2)
    try:
        r = requests.get(url,timeout = 20)
        print(q.qsize(),r.status_code,url)
    except Exception as e:
        print(q.qsize(),url,"Error:",q)
if __name__ == '_main__':
    ProcessNames = ['Process-1','Process-2','Process-3']
    workQueue = Queue(1000)
    for url in link_list:
        workQueue.put(url)
    for i in range(0,3):
        p = Myprocess(workQueue)
        p.daemon = True
        p.start()
        p.join()
end = time.time()
print("Process+Queue 多进程爬虫的总时间为: ",end-start)
print("Main process Ended!")