import pymysql
from orm_pool import mysql_pool
class Mysql:
    def __init__(self):
        self.conn=mysql_pool.POOL.connection()
        self.cursor=self.conn.cursor(cursor=pymysql.cursors.DictCursor)

    def close_db(self):
        self.cursor.close()
        self.conn.close()

    def select(self, sql, args=None):
        #select * from user where id=%s

        self.cursor.execute(sql, args)
        rs = self.cursor.fetchall()
        return rs

    def execute(self, sql, args):
        try:
            #update user set name='oo' where id =%s
            self.cursor.execute(sql, args)
            affected = self.cursor.rowcount
            # self.conn.commit()
        except BaseException as e:
            print(e)
        return affected





if __name__ == '__main__':
    ms=Mysql()
    re=ms.select('select * from user where id=%s',1)
    print(re)