# def say(a, s, d):
#     print(a, s, d,)
#
#
# say(1,2,3)
# say(1,d=1132,s=231232)
#
#
# def register(name,age,sex='male',*args,**kwargs):
#     print(name,age,sex)
#
#
# register('xxxx',18,)
#
#
#
# def show_class_room(classname,students):
#     print(classname,students)
#
#
# show_class_room('3132322',[6654+6,56465,154,'ssss'])
# show_class_room('3132322',[65555,5555,154,'dddd'])
#
#
# def foo(x, y, z):
#     print(x, y, z)
#
#
# foo(*[1, 2, 3])

#
# def foo(x, y, *args,**kwargs):
#     print(x, y)
#     print(args)
#     print(kwargs)
#
# foo(1, 2, *[3, 4, 5],**{'a':1,'b':2,'c':3})


def foo(x, y, *args,**kwargs):
    print(x, y)
    print(*args)
    print(kwargs)
    print(type(kwargs))

# foo(1, 2, *[3, 4, 5],**{'q':1,'w':563,'e':453,'r':453,'t':4534,})
foo(1, 2, *[3, 4, 5],ql=1,sd=3,rde=5)
len()
