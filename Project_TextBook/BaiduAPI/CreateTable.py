import pymysql
conn = pymysql.connect(host='localhost',user='root',
                       passwd='123456',db='baidumap',charset='utf8')
cur = conn.cursor()
sql = """create table if not exists city(
      id int not null primary key auto_increment ,
      city varchar(200) not null, 
      park varchar (200) not null,
      location_lat float ,
      local_lng float ,
      adress varchar (200),
      street_id varchar (200),
      uid varchar (200),
      create_time timestamp default current_timestamp 
      )"""
cur.execute(sql)
cur.close()
conn.commit()
conn.close()
