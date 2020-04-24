# !/usr/bin/env python
# -*- coding:utf-8 -*-

# 导入第三方模块
import smtplib
from email.mime.text import MIMEText
from email.utils import formataddr

# 自定义发送邮件的函数
'''
    配置发邮件所需的基础信息
    my_sender    # 配置发件人邮箱地址
    my_pass      # 配置发件人邮箱密码
    to_user      # 配置收件人邮箱地址
    my_nick      # 配置发件人昵称
    to_nick      # 配置收件人昵称
    mail_msg     # 配置邮件内容
'''


def mail(my_sender, my_pass, to_user, my_nick, to_nick, mail_msg):
    # 必须将邮件内容做一次MIME的转换,MIME是目前互联网邮件普遍采用的格式标准
    msg = MIMEText(mail_msg, 'html', 'utf-8')
    # 配置发件人名称和邮箱地址
    msg['From'] = formataddr([my_nick, my_sender])
    # 配置收件件人名称和邮箱地址
    msg['To'] = formataddr([to_nick, to_user])
    # 配置邮件主题（标题）
    msg['Subject'] = "发送邮件测试"

    # 配置Python与邮件的SMTP服务器的连接通道
    server = smtplib.SMTP_SSL("smtp.qq.com", 465)
    # 模拟登陆
    server.login(my_sender, my_pass)
    # 邮件内容的发送
    server.sendmail(my_sender, [to_user, ], msg.as_string())
    # 关闭连接通道
    server.quit()



# 配置发邮件所需的基础信息
my_sender = '3116860280@qq.com'
my_pass = 'fqwdrgcxnytvdffa'
to_user = ['caopuxjtu@163.com', 'caopu1@cmbc.com.cn', 'wangyanglong@cmbc.com.cn']
my_nick = '曹璞'
to_nick = ['163', 'cmbc', '养龙']

for i in range(3):
    # 配置邮件内容
    mail_msg = """
    <p>尊敬的{}:</p>
    <p>您好，非常抱歉打扰到您，这是一份Python 的邮件测试，看见后可以忽略。</p>
    <p>Q: 有哪些东西你以为很贵，但其实很便宜？</p>
        <p>A: 大学刚毕业的我。</p>
        <p>Q: 为什么人常会在黑夜里，变得矫情万分？</p>
        <p>A: 要渲染的图像少了，CPU就有空闲来思考人生了</p>
    """.format(to_nick[i])

    # 调用函数
    try:
        mail(my_sender, my_pass, to_user[i], my_nick, to_nick[i], mail_msg)
        print('邮件发送成功！')
    except:
        print('邮件发送失败！')




# try:
#     mail_msg = """
#         <p>Q: 有哪些东西你以为很贵，但其实很便宜？</p>
#         <p>A: 大学刚毕业的我。</p>
#         <p>Q: 为什么人常会在黑夜里，变得矫情万分？</p>
#         <p>A: 要渲染的图像少了，CPU就有空闲来思考人生了</p>
#     """
#     # 调用函数
#     # def mail(my_sender, my_pass, to_user, my_nick, to_nick, mail_msg):
#
#     # mail('3116860280@qq.com', 'fqwdrgcxnytvdffa', 'caopuxjtu@163.com', '曹璞', '养龙', mail_msg)
#     # mail('3116860280@qq.com', 'fqwdrgcxnytvdffa', 'caopu1@cmbc.com.cn', '曹璞', '养龙', mail_msg)
#     # mail('3116860280@qq.com', 'fqwdrgcxnytvdffa', 'wangyanglong@cmbc.com.cn', '曹璞', '养龙', mail_msg)
#     mail('3116860280@qq.com', 'fqwdrgcxnytvdffa', 'wangpeng37@cmbc.com.cn', '曹璞', '鹏', mail_msg)
#     print('邮件发送成功！')
# except:
#     print('邮件发送失败！')
