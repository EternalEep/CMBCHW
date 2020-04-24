# !/usr/bin/env python
# -*- coding:utf-8 -*-  
# coding=utf-8
import os
import sys
import time
import urllib2
import datetime

listOpenid = ['oTXMbt1eeACSF8p5r89ibsSBZgdg']
clusterURL = 'http://192.168.10.1:8082'
pythonCheck = "/var/hdata/kafka_2.10-0.10.2.0/sh/pythonCheck.sh"


def check(interval, topic, group, pNumbers):
   now_time0 = datetime.datetime.now()  # 当前时间获取 格式化日志输出使用
   f = os.popen(pythonCheck + " " + group)
   l = f.readlines()
   f.close()
   try:
       if len(l) <= 1:  # 增加对结果的空异常校验
           for i in range(len(listOpenid)):
               alarmNetwork(group, listOpenid[i], 'consumerGroupDead', clusterURL)
           return 10 * '==' + str(now_time0) + " consumer group is dead " + 19 * '='

       time.sleep(float(interval))  # sleep

       f2 = os.popen(pythonCheck + " " + group)
       l2 = f2.readlines()
       f2.close()

       errCount = 0
       now_time = datetime.datetime.now()  # 当前时间获取 格式化日志输出使用

       beforList = toList(l)
       afterList = toList(l2)
       print(str(now_time0) + '   ' + str(beforList))
       print(str(now_time) + '   ' + str(afterList))
       for x in beforList:
           # print(str(now_time) + '   p' + str(x) + '     offset ' + beforList[x])

           #每隔几秒钟，执行显示某个消费组的消费详情命令后，判断执行前后各个分区的offset是否相等
           if beforList[x] == afterList[x]:
               errCount = errCount + 1
       if errCount >= int(pNumbers):
           for i in range(len(listOpenid)):
               alarmNetwork(group, listOpenid[i], 'consumerGroupSuccessOffsetFailed', clusterURL)
           return "*****consumer group success but offset failed***"
       return "******************success***********************"
   except RuntimeError as e:
       return "toList failed" + e.message
   except urllib2.HTTPError as e:
       print('HTTPError: ' + str(e.code))


def toList(argv):  # 构建一个基于partition 和 offset的 K-V 字典结构
   count = 0
   new_dict = {}
   try:
       for x in argv:
           # print(x)
           if count < 2:
               count = count + 1
           else:
               list = x.split()
               if list[2].isdigit() == False:
                   raise RuntimeError('parseError')
               else:
                   # tempList.append(list[2])
                   new_dict[list[1]] = list[2]
       return new_dict

   except RuntimeError as e:
       for i in range(len(listOpenid)):
           alarmNetwork(group, listOpenid[i], 'toListFunctionFailed', clusterURL)
       return "consumer group success but offset failed"
       return " toList RuntimeError"


'''
  alarmNetwork 监控工具插件是否正常告警
  调用告警接口进行微信告警
'''


def alarmNetwork(groupId, openid, networkErrorMessage, clusterURL):
   url = "http://195.203.10.84:8088/hweb/hsrv.do?dealcode=E0011&channel=app&amp;keyinfo=abc&openid=%s&groupId=%s&networkErrorMessage=%s&amp;clusterURL=%s" % (
       openid, groupId, networkErrorMessage, clusterURL)

   # url = "http://198.203.66.200/hweb/hsrv.do?dealcode=E0011&channel=app&keyinfo=abc&amp;openid=%s&amp;groupId=%s&networkErrorMessage=%s&clusterURL=%s" % (
   #     openid, groupId, networkErrorMessage, clusterURL)
   request = urllib2.Request(url)
   response = urllib2.urlopen(request)
   # print 'alarmNetwork success'  # 格式化日志使用标识


if __name__ == '__main__':
   input = sys.argv
   interval = input[1]  # 输入需要 定义的间隔时间
   group = input[2]  # 输入需要 监控的消费者组
   pNumbers = input[3]  # 输入需要 定义的分区个数
   topic = input[4]

   resultStr = check(interval, topic, group, pNumbers)
   print(resultStr)
