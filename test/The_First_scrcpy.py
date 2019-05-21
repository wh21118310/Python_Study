import re
s = 'Hello, Mr.Gumby : 2016/10/26'
p = re.compile("(?P<name>\w+\.\w+).*?(\d+\/\d+\/\d+)(?#comment)")
m = p.search(s)

# 使用别名访问
print(m.group(1))
# output> Mr.Gumby
# 使用分组访问
print(m.group(2))
# output> 2016/10/26
print(type(m.groups()))