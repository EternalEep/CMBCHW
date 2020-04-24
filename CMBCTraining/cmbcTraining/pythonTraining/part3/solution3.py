# !/usr/bin/env python
# -*- coding:utf-8 -*-

def func(index, obj):
    print('{%d}, %s' % (index, obj))


# 使用多个文件(重要)
"""Python有一个pass语句，可在代码块中使用它来让Python什么都不要做："""
x = ('This will build a very long long '
     'long long long long long long string')
def count_words(file_path):
    """计算一个文件大致包含多少个单词"""
    try:
        with open(file_path) as f_obj:
            contents = f_obj.read()
    except FileNotFoundError:
        msg = "sorry,the file " + file_path + " does not exist."
        func(1, msg)
        # pass
    else:
        words = contents.split()
        num_words = len(words)
        func(2, ("The file " + file_path + " has about " + str(num_words) + " words."))


file_paths = ['/Users/sudo/Documents/test_data/file.txt', '/Users/sudo/Documents/test_data/file1.txt', '/Users/sudo/Documents/test_data/file2.txt']
for file_path in file_paths:
    count_words(file_path)
