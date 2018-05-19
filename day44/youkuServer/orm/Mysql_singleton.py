import pymysql

class Mysql:
    __instense=None
    def __init__(self):
        self.conn=pymysql.connect(
            host='127.0.0.1',
            port=3306,
            user='fixd',
            password='123',
            charset='utf8',
            database='youku',
            autocommit=True
        )
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
    @classmethod
    def singleton(cls):
        if not cls.__instense:

            cls.__instense=cls()

        return  cls.__instense




if __name__ == '__main__':
    ms=Mysql()
    re=ms.select('select * from user where id=%s',1)
    print(re)