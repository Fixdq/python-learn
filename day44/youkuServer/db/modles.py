from orm_pool.fuckorm_pool import Modles, StringFileld, IntegerFileld


# from orm.fuckorm   import Modles,StringFileld,IntegerFileld
class User(Modles):
    table_name = 'userinfo'
    id = IntegerFileld('id', primary_key=True)
    name = StringFileld('name')
    password = StringFileld('password')
    is_vip = IntegerFileld('is_vip')
    locked = IntegerFileld('locked')
    user_type = StringFileld('user_type')


class Notice(Modles):
    table_name = 'notice'
    id = IntegerFileld('id', primary_key=True)
    name = StringFileld('name')
    content = StringFileld('content')
    create_time = StringFileld('create_time')
    user_id = IntegerFileld('user_id')

class Movie(Modles):
    table_name = 'movie'
    id = IntegerFileld('id', primary_key=True)
    name = StringFileld('name')
    path = StringFileld('path')
    is_free = IntegerFileld('is_free')
    is_delete = IntegerFileld('is_delete')
    create_time = StringFileld('create_time')
    user_id = IntegerFileld('user_id')
    file_md5 = StringFileld('file_md5')