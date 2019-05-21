# coding=utf-8
import requests
r = requests.get("https://blog.csdn.net/qq_30277453")
# print("文本编码：",r.encoding)
# print("响应状态码：",r.status_code)
# print("字符串方式的响应体：",r.text)
# Requests的定制—传递URL参数
key_dict = {'key1': "value1", "key2": "value2"}
r = requests.get("https://blog.csdn.net/qq_30277453", params=key_dict)
print("URL正确编码：", r.url)
# print("字符串方式的响应体：\n",r.text)
# Requests的定制——定制请求头
headers = {
	'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36',
	#     没有Host信息，所以不写
}
r = requests.get('https://blog.csdn.net/qq_30277453', headers=headers)
print("响应状态码：", r.status_code)
# Requests的定制——发送POST请求
r = requests.get('https://blog.csdn.net/qq_30277453', key_dict)
# print(r.text)
# Requests的定制——超时
r = requests.get("https://blog.csdn.net/qq_30277453", timeout=20)
