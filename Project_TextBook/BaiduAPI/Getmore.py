import pymysql
conn = pymysql.connect(host = 'localhost',user='root',passwd='123456',
                       db='baidumap',charset='utf8')
cur = conn.cursor()
sql = """CREATE TABLE park (
         id INT NOT NULL AUTO_INCREMENT,
         park VARCHAR(200) NOT NULL,
         location_lat FLOAT,
         location_lng FLOAT,
         address VARCHAR(200),
         street_id VARCHAR(200),
         telephone VARCHAR(200),
         detail INT,
         uid VARCHAR(200),
         tag VARCHAR(200),
         type VARCHAR(200),
         detail_url VARCHAR(800),
         price INT,
         overall_rating FLOAT,
         image_num INT,
         comment_num INT,
         shop_hours VARCHAR(800),
         alias VARCHAR(800),
         keyword VARCHAR(800),
         scope_type VARCHAR(200),
         scope_grade VARCHAR(200),
         description VARCHAR(9000),
         created_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
         PRIMARY KEY (id)
         );"""
cur.execute(sql)
cur.close()
conn.commit()
conn.close()