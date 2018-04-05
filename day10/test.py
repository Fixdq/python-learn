# encoding: utf-8
# by fixdq
#
# import time
# def timmer(func):
#     def wrapper(*args,**kwargs):
#         start_time=time.time()
#         res=func(*args,**kwargs)
#         stop_time=time.time()
#         print('run time is %s' %(stop_time-start_time))
#         return res
#     return wrapper
#
# @timmer
# def foo():
#     time.sleep(1)
#     print('from foo')
# foo()

def auth(driver='file'):
    def auth2(func):
        def wrapper(*args,**kwargs):
            name=input("user: ")
            pwd=input("pwd: ")

            if driver == 'file':
                if name == 'egon' and pwd == '123':
                    print('login successful')
                    res=func(*args,**kwargs)
                    return res
            elif driver == 'ldap':
                print('ldap')
        return wrapper
    return auth2



@auth(driver='ldap')
def foo(name):
    print(name)

foo('egon')