
from orm_pool import Mysql_poo

class Fileld:
    def __init__(self,name,column_type,primary_key,default):
        self.name=name
        self.column_type=column_type
        self.primary_key= primary_key
        self.default=default



class StringFileld(Fileld):
    def __init__(self,name=None,column_type='varchar(200)',primary_key=False,default=None):
        super().__init__(name,column_type,primary_key,default)



class IntegerFileld(Fileld):
    def __init__(self,name=None,column_type='int',primary_key=False,default=0):
        super().__init__(name,column_type,primary_key,default)


class ModlesMetaclass(type):
    def __new__(cls, name,bases,attrs):

        if name=='Modles':
            return type.__new__(cls,name,bases,attrs)
        table_name=attrs.get('table_name',None)
        # table_name=attrs['table_name']

        primary_key=None
        mappings=dict()
        for k,v in attrs.items():
            if isinstance(v,Fileld):#v 是不是Field的对象
                mappings[k]=v
                if v.primary_key:

                    #找到主键
                    if primary_key:
                        raise TypeError('主键重复：%s'%k)
                    primary_key=k

        for k in mappings.keys():
            attrs.pop(k)
        if not primary_key:
            raise TypeError('没有主键')
        attrs['table_name']=table_name
        attrs['primary_key']=primary_key
        attrs['mappings']=mappings
        return type.__new__(cls,name,bases,attrs)









class Modles(dict,metaclass=ModlesMetaclass):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)


    def __setattr__(self, key, value):

        self[key]=value

    def __getattr__(self, item):
        try:
          return self[item]
        except TypeError:
            raise ('没有该属性')

    @classmethod
    def select_one(cls,**kwargs):
        #只查一条
        key=list(kwargs.keys())[0]
        value=kwargs[key]
        #select * from user where id=%s
        sql='select * from %s where %s=?'%(cls.table_name,key)
        #
        sql=sql.replace('?','%s')
        ms=Mysql_poo.Mysql()
        re=ms.select(sql,value)
        if re:
            #attrs={'name':'123','password':123}
            #u=User(**attrs)
            #相当于 User(name='123',password=123)
            u=cls(**re[0])
            return u
        else:
            return

    @classmethod
    def select_many(cls,**kwargs):
        ms = Mysql_poo.Mysql()
        if kwargs:
            key=list(kwargs.keys())[0]
            value=kwargs[key]
            sql = 'select * from %s where %s=?' % (cls.table_name, key)
            #
            sql = sql.replace('?', '%s')

            re = ms.select(sql, value)
        else:
            sql = 'select * from %s'%(cls.table_name)
            re = ms.select(sql)

        if re:
            lis_obj=[cls(**r) for r in re]
            return lis_obj
        else:
            return

    def update(self):
        ms = Mysql_poo.Mysql()
        #update user set name=?,password=? where id=1

        filed=[]
        pr=None
        args=[]
        # mapping={id:inter的对象，name：strfil的对象，password：stringfile 的对象}
        # user：1 table_name   2 primary_key  3 mapping
        #       4 name='123'5 id=1 6 password=123
        for k,v in self.mappings.items():

            if v.primary_key:

                pr=getattr(self,v.name,None)#v.name = id

            else:
                filed.append(v.name + '=?')
                args.append(getattr(self,v.name,v.default))
                getattr(self, 'name', None)  # 拿到123

        sql = 'update %s set %s where %s =%s'%(self.table_name,','.join(filed),self.primary_key,pr)
        #'update user set name=?,password =? where id =1'
        sql=sql.replace('?','%s')
        ms.execute(sql,args)
    def save(self):
        ms = Mysql_poo.Mysql()
        #insert into user (name,passwword) values (?,?)
        filed=[]
        values=[]
        args=[]
        for k,v in self.mappings.items():
            if not v.primary_key:
                filed.append(v.name)
                values.append('?')
                args.append(getattr(self,v.name,None))
        sql ='insert into %s (%s) VALUES (%s)'%(self.table_name,','.join(filed),','.join(values))
        sql= sql.replace('?','%s')
        ms.execute(sql,args)






