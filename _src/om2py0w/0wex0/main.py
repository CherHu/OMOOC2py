# -*-coding: utf-8 -*-
# !/usr/bin/env python
# quick python script explanation for programmers

import os

def main():
    print "Hello, world!"
    print "这是Cher的问候。"
    
    foo(5,10)

    print '=' * 10
    print '这将直接执行'
    os.getcwd()

    counter = 0
    counter += 1

    food = ['苹果','杏子','李子','梨']
    for i in food:
        print "我就爱整只：" +i 

    print '数到10'
    for i in range(10):
        print i 

def foo(paraml, secondParam):
    res = paraml + secondParam
    print '%s 加 %s 等于 %s' %(paraml, secondParam, res)
    if res<50:
        print "好的。"
    elif (res >= 50) and ((paraml == 42) or (secondParam == 24)):
        print "行吧。"
    else:
        print "天哪凸^-^凸"
    return res


if __name__ =='__main__':
    main()
