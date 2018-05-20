from orm.mysql_pool import POOL
import pymysql


class MySql:

    def __init__(self):
        self.conn = POOL.connection()
        self.cursor = self.conn.cursor(cursor=pymysql.cursors.DictCursor)

    def select(self, sql, args=None):


        self.cursor.execute(sql, args)
        return self.cursor.fetchall()


    def execute(self, sql, args):
        self.cursor.execute(sql, args)
        return self.cursor.rowcount

    def close(self):
        self.cursor.close()
        self.conn.close()
