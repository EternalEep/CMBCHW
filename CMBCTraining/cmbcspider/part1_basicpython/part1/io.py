# !/usr/bin/env python
# -*- coding:utf-8 -*-
#
# try:
#     f = open(r'/Users/sudo/Documents/test_data/file.txt').read()
#     print(f)
# finally:
#     if f:
#         f.close()

#代替上面的方法，使用with

with open(r'/Users/sudo/Documents/test_data/file.txt') as fileReader:
    print(fileReader.read())


with open(r'/Users/sudo/Documents/test_data/file.txt') as fileReader:
    for line in fileReader.readlines():
        print(line.strip())


import pickle

d = dict(url='index.html',title='首页',content='首先')
result = pickle.dumps(d)
print(result)

#使用dump方法，将序列化对象写入文件
f = open(r'/Users/sudo/Documents/test_data/dump.txt','wb')

result1 = pickle.dump(d,f)
f.close()

#使用load方法将文件反序列化为对象
f1 = open(r'/Users/sudo/Documents/test_data/dump.txt','rb')
result2 = pickle.load(f1)
print(result2)
f1.close()