# 1.3 2wNote 

## REPL:交互探索环境


#### REPL:输入什么，立即有什么输出反应
- read:读入
- eval:运行
- print：输出
- loop：循环

#### 探索：

ipython (?)

pyenv(?)

- help()——REPL中，python内置了帮助。学习最快的方式

    - e.g range:生成数组的常用工具 ［具体使用参考help（range)]

- dir:
    - 报告当前环境中有什么对象,e.g dir(a)
    - 以及对象都有什么操作 dir(a.sort)
    - 以及对象的操作有什么内置hook

- print
    - e.g print a
          print a[0]：打印第一个对象
          print a[1]：打印第二个对象
          print a+[4,5,6]：与另一数组相加
          len(a):a的长度


### 1W task详解
- 任务：交互笔记
- 描述：
    - 一次接受输入一行日记
    - 保存为本地文件
    - 再次运行系统时，能打印出过往所有日记
- 展示
    - 环境初
    - 始化：
        - cat mydaily.log
        - rm mydaily.log
        
    - 调用？
        - cat mydaly.log
        - python main.py
    - 目录？ ls

- 期待
    - 直觉的无参数调用 
> 桌面软件虽然便利但无可变性，熟悉命令行的操作模式
    - 直觉的默认帮助  
> ?/h/help
    - 持续的输入
> 试验再试验，体验成功的快感。
    - 直觉的退出 
> q/quit
    - 自动保存
> **不麻烦人的都不应该麻烦……**
- 技术
    - raw_input()  从外界收到数据
    - while+break  用while进行就保持住了输入、交互；break来退出
    - os.path.exists 本地文件是否存在。详见官方文档？？
    - open() 打开文件。内建的函数，随时可以用。
    - for...in  回读时的 for in 循环，in的对象是很任性的……
- <51行（包含注释）


### UTF-8的故事
部分演化史：
- ASC II(128个字符，英文环境）
- Unicode（符号集，100多万种字符）
- UTF-8(编码）——unicode实现之一，当前已是主流，拐点在08年。
> so,why"锟斤拷锟斤拷锟斤拷锟斤拷锟斤拷锟斤拷锟斤拷"?  
——过时的编码，泪……

So, "Keep clam and **be UTF-8.**" 


### 善用搜索
- 如何搜索图片其他副本?

> e.g 《极简python上手导念》
- 快照 
- 七牛 bitbucket.org TW

- DAMA's design collection, including the .png in 《极简python上手导念》。

 ![](Screen Shot 2015-10-26 at 14.54.00.png)
 
 
### python脚本原模版
  ![](Screen Shot 2015-10-26 at 15.09.16.png)
- 头部说明（固定的）：
    - ＃-*- coding: utf-8 -*- 
    - ＃!/user/bin/env python
    - ＃文件说明，作者信息，版本自述……（参考github上排名靠前的模块）
- 全局引用：
   - import sys
   >import是python里做的不太好的一个方面，so:
   1、import 内置模块
   2、import 第三方模块
   3、import 自己工程里的模块