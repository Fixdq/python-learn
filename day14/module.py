# encoding: utf-8
# by fixdq

from mysql import say_hi
import oracle
import db2
import sys
# print(mysql.db_exec())
print(oracle.db_exec())
print(db2.db_exec())

# def say_hi():
#     print('say hi in module')
#

say_hi()

print(sys.path)
