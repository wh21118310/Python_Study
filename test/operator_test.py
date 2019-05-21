import operator
x = {1:2,3:4,4:3,2:1,0:0}
sorted_x = sorted(x.items(),key = operator.itemgetter(0))
print(sorted_x)
#测试正则表达式中关于.group()与.group(0)
import re
r1 = re.match('w*w', 'www.163.com')  # 在起始位置匹配
r2 = re.match('com', 'www.163.com')  # 不在起始位置匹配
if r1!=None:
    print('r1:',r1.group(0))
    print('r1:',r1.groups())
if r2!=None:
    print('r2:',r2.group(0))
    print('r2:',r2.groups())