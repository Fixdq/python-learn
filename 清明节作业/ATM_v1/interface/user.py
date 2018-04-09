from db import db_handler

def get_userinfo_interface(name):
    '''
    通过用户名获取用户信息接口
    :param name:
    :return:
    '''
    return db_handler.select(name)
