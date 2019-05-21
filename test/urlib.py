# import urllib.request
# #构建一个HTTPHandler处理器对象,支持处理HTTP请求
# #若在HttpHandler方法中增加参数debuglevel=1,会将 Debug Log也打开,这样程序在执行时,会把收包和抓包的报头自动打印,以便调试
# http_handler = urllib.request.HTTPHandler(debuglevel=1)
# #调用urllib.build_opener()方法,创建支持处理HTTP请求的opener对象
# opener = urllib.request.build_opener(http_handler)
# #构建Request请求
# request = urllib.request.Request('http://www.baidu.com/')
# #调用自定义的opener对象的open()方法,发送request请求
# #(注意区别: 不再通过urllib.request.urlopen()发送请求)
# response = opener.open(request)
# #获取服务器响应内容
# print(response.read())
from urllib import request,parse
url = 'http://www.itcast.cn'
headers={
	'User-Agent':'Mozilla/5.0 (comoatible;MSIE 9.0;windows NT6.0;Trident/5.0)',
	'Host':'httpbin.org'
}
dict_demo = {'name':'itcast'}
data = bytes(parse.urlencode(dict_demo).encode('utf-8'))
requestcontent = request.Request(url,headers=headers,data=data)
respons = request.urlopen(requestcontent)
html = respons.read().decode('utf-8')
print(html)

