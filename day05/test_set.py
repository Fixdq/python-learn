linux  = {'张全蛋','李铁单','oldboy','alex','egon'}
python  = {'李二丫','刘德华','wxx','alex','egon'}

#交集
print(linux & python)
#并集
print(linux | python)
#linux 的差集
print(linux- python)
print(python-linux)
#交叉补集
print(linux ^ python)