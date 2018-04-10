from db import db_handler


def get_userinfo_interface(name):
    '''
    通过用户名获取用户信息接口
    :param name:
    :return:
    '''
    return db_handler.select(name)


def register_user(name, pwd, credit=15000):
    """
    注册用户接口
    :param name: 
    :param pwd: 
    :param credit: 
    :return: 
    """
    user_dic = {
        'name': name,
        'password': pwd,
        'locked': False,
        'account': credit,
        'credit': credit,
        'shopping_cart': {},
        'bankflow': [],
    }
    db_handler.update(user_dic)


def lock_user(name):
    """
    锁定用户接口
    :param name: 
    :return: 
    """
    user_dic = get_userinfo_interface(name)
    user_dic['lodked'] = False
    db_handler.update(user_dic)


def unlock_user(name):
    """
    锁定用户接口
    :param name: 
    :return: 
    """
    user_dic = get_userinfo_interface(name)
    user_dic['lodked'] = True
    db_handler.update(user_dic)
