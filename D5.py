"""
@version: ??
@author: coco wang
@license: Apache Licence 
@contact: endoffight@gmail.com
@site: 
@software: PyCharm
@file: D5.py
@time: 2017/12/25 0025 下午 3:07
"""
# 载入自己的语料库
import nltk
from nltk.corpus import PlaintextCorpusReader
from nltk.corpus import brown
import os

corpus_text = ''.join(os.getcwd() + '/usr/share/dict')
print(corpus_text)
wordlists = PlaintextCorpusReader(corpus_text, '.*')
print(wordlists)
wordlists.fileids()
wordlists.words()

"""
处理布朗语料库的新闻和言情文体，找出一周中最有新闻价值并且是
最浪漫的日子。定义一个变量 days 包含星期的链表，如['Monday', ...]。然
后使用 cfd.tabulate(samples=days)为这些词的计数制表。接下来用绘图替
代制表尝试同样的事情。你可以在额外的参数 conditions=['Monday', ...]的
帮助下控制星期输出的顺序。
"""
#genre 表示条件，word表示要统计的分布

cfd = nltk.ConditionalFreqDist(
    (genre, word)
    for genre in ['news', 'romance']
    for word in brown.words(categories=genre))

# list(cfd['news'])[:4]
#Out[44]: ['picture', 'center', 'Munoz', 'Motor']

days=['Monday', 'Tuesday', 'Wednesday','Thursday', 'Friday', 'Saturday', 'Sunday']
#制表形式显示
cfd.tabulate(samples=days)
cfd.plot(samples=days)


