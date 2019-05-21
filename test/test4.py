import sqlite3;

cn = sqlite3.connect('sdut.db');
cur = cn.cursor()
'''cur.execute('create table users(name char(11),age int(2))')
cur.execute('insert into users values ("John",10)')
cur.execute('insert into users values ("Wang",18)')
cur.execute('insert into users values ("Li",20)')
cur.execute('delete from users  where  name  = "Li"')
cur.execute('update users set age = 19 where age = 18')
cn.commit() #保存操作
cur.close() #关闭游标
cn.close() #与数据库断开连接'''
r = cur.execute("select * from users")
for (x,y) in cur.fetchall():
    print('姓名：%s\t年龄: %s'%(x,y))
# fechall()方法循环迭代读取数据
w = cn.execute('select * from users')
while True:
    x = w.fetchone()
    if not x: break
    print('姓名：%s\t年龄：%s'%(x[0],x[1]))
#调用fetchone()方法每次可提取一条数据，但要注意