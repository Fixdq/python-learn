# encoding: utf-8
# by fixdq

def f1():
    print('f1')
    def f2():
        print('f2')
        def f3():
            print('f3')
        f3()
    f2()
f1()

print(f1)
print(type(f1))






