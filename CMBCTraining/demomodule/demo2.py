# !/usr/bin/env python
# -*- coding:utf-8 -*-


# 日志模块
# 可以保存成一个文件，方便之后查看使用
"""
print也可以输入日志，logging相对print来说更好控制输出在哪个地方，怎么输出及控制消息级别来过滤掉那些不需要的信息
级别排序:CRITICAL > ERROR > WARNING > INFO > DEBUG
低于该级别的就不输出了
debug : 打印全部的日志,详细的信息,通常只出现在诊断问题上

info : 打印info,warning,error,critical级别的日志,确认一切按预期运行

warning : 打印warning,error,critical级别的日志,一个迹象表明,一些意想不到的事情发生了,
或表明一些问题在不久的将来(例如。磁盘空间低”),这个软件还能按预期工作

error : 打印error,critical级别的日志,更严重的问题,软件没能执行一些功能

critical : 打印critical级别,一个严重的错误,这表明程序本身可能无法继续运行
如果需要显示低于WARNING级别的内容，可以引入NOTSET级别来显示
logging.basicConfig(level=logging.NOTSET)  # 设置日志级别
"""

import logging  # 引入logging模块

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s')  # logging.basicConfig函数对日志的输出格式及方式做相关配置
# 由于日志基本配置中级别设置为DEBUG，所以一下打印信息将会全部显示在控制台上
logging.info('this is a loggging info message')
logging.debug('this is a loggging debug message')
logging.warning('this is loggging a warning message')
logging.error('this is an loggging error message')
logging.critical('this is a loggging critical message')
