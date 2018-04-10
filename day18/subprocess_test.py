#!/usr/bin/env python3
# encoding: utf-8
# by fixdq
import subprocess

obj = subprocess.Popen('ifconfig',
                       shell=True,
                       stdout=subprocess.PIPE,# 将正确的信息丢入到管道管道中
                       stderr=subprocess.PIPE,# 将错误的信息丢入到管道管道中
                       )

res = obj.stdout.read()
print(res.decode('utf-8'))

err = obj.stderr.read()
print(err.decode('utf-8'))


# obj.stderr.read() 只能取走一次内容，之后取不到内容的