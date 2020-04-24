# !/usr/bin/env python
# -*- coding:utf-8 -*-

###生成词云

import matplotlib.pyplot as plt
from wordcloud import WordCloud
import jieba
import re



#1、首先要对对文本数据进行分词
word = open("/Users/sudo/Documents/test_data/word.txt", "rb").read()
# word = open("/Users/sudo/Documents/cmbc/CMBCTraining/cmbcTraining/pythonTraining/spider/一念永恒.txt", "rb").read()
# word = open("/Users/sudo/Documents/test_data/猫眼TOP100.txt", "rb").read()


# 分词
wordlist = jieba.cut(word, cut_all=True)
wl = " ".join(wordlist)
#print(wl)  # 输出分词之后的txt


# 设置词云
wc = WordCloud(background_color="black",  # 设置背景颜色
               # mask = "图片",  #设置背景图片
               max_words=5000,  # 设置最大显示的字数
               # stopwords = "", #设置停用词
               font_path='Hiragino Sans GB.ttc',
               # width=2000,  # 宽度
               # height=1000,  # 高度
               # 设置中文字体，使得词云可以显示（词云默认字体是“DroidSansMono.ttf字体库”，不支持中文）
               max_font_size=60,  # 设置字体最大值
               random_state=30,  # 设置有多少种随机生成状态，即有多少种配色方案
               )
myword = wc.generate(wl)  # 生成词云

# 展示词云图
plt.imshow(myword)
plt.axis("off")
plt.show()

#保存生成的图片
myword.to_file('/Users/sudo/Documents/test_data/picture/result.png')
