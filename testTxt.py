import re

f = open("message.txt","r")
lines = f.readlines()#读取全部内容
for line in lines:
    list = re.split(';',line)
    print(list[0])
    print(list[1])
f.close()