#-*- coding:utf-8 -*-
#!/user/bin/env python

from sys import argv
import time

script, filename = argv

# 记录时间函数
def GetTime():
    localtime = time.asctime( time.localtime(time.time()) )
    print ("Now it is:", localtime)
    return localtime

# 写日记函数
def writeDiary():
    localtime = GetTime()
    diary = open(filename,'a+')
    diary.write(localtime +'\n')

    while True:
        print "Press RETURN to continue writing. Input 'end' to quit."
        dailydiary = raw_input('Here we go.>>')

        if dailydiary.upper() in ['end','END']:
            break
        diary.write(dailydiary +'\n')

# 读取日记函数
def readHistory():
    history = open (filename,'r')
    print history.read()
    history.close()

# 调用写日记函数
print "Hey, wanna talk?"
writeDiary()

# 调用读取日记函数
print """
    Hey there. Wanna review the history?
    Input Y to continue. Input N to abort.
    """
next = raw_input(" Y/N ")

if 'y' in next or 'Y' in next:
    readHistory()

else:
    print "Ok then, bye~"
  
