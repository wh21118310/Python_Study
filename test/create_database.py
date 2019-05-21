import pymysql
class databse:
    def create_database(self):
      con = pymysql.connect(host='localhost', user='root', password='123456', db='scraping',charset='UTF-8')
      cur = con.cursor()
      cur.execute('CREATE TABLE urls(name varchar(8) not null auto_increment,stuback varchar(8) not null,career varchar(8) null,employtype varchar(20) null,address varchar(30) null ,time varchar(15) not null,primary key(name))')
      cur.close()
      con.commit()
      con.close()
    def insert_data(self,data,cur):
        cur.execute("insert into scraping values()")
        