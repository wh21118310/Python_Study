# coding=utf-8
import urllib.parse,urllib.request
def spider(url,begin_page,end_page):
    '''
    作用： 贴吧爬虫调度器，负责组合处理每个页面的url
    :param url: 贴吧url前半部分
    :param begin_page: 起始页码
    :param end_page: 结束页
    '''
    for page in range(begin_page,end_page+1):
         pn = (page-1)*50
         file_name = "第"+str(page)+"页.html"
         full_url = url +"&pn="+str(pn)
         html = load_page(full_url,file_name)
         write_page(html,file_name)
def load_page(url,filename):
    '''
    作用：根据url发送请求，获取服务器响应文件
    :param url:需要爬取的url
    '''
    headers = {
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36',
        'Host':'tieba.baidu.com'
    }
    request = urllib.request.Request(url,headers=headers)
    return urllib.request.urlopen(request).read()
def write_page(html,file_name):
    '''
    作用: 将html内容x写入本地文件
    :param html:服务器响应文件内容
    '''
    print('正在保存'+file_name)
    with open(file_name,'w',encoding='UTF-8') as file:
        file.write(html.decode('UTF-8'))
if __name__ == '__main__':
    kw = input('请输入需要爬取的贴吧名： ')
    begin_page = int(input('请输入起始页： '))
    end_page = int(input('请输入结束页：'))
    url = 'http://tieba.baidu.com/f?'
    key = urllib.parse.urlencode({'kw':kw})
    url = url+key
    spider(url,begin_page,end_page)