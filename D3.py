"""
@version: ??
@author: coco wang
@license: Apache Licence 
@contact: endoffight@gmail.com
@site: 
@software: PyCharm
@file: D3.py
@time: 2017/12/21 0021 上午 11:04
"""
import matplotlib.pyplot as plt
from nltk.book import *
saying = ['After', 'all', 'is', 'said', 'and', 'done', 'more', 'is', 'said', 'than', 'done']
tokens = set(saying)
tokens = sorted(tokens)
# 取排序后面两个，从倒数的第二个到最后一个，也就是只有后面两个
tokens[-2:]

fdist1 = FreqDist(text1)
vocabulary1 = fdist1.keys()
#  前50个
# vocabulary1[:50]
fdist1['whale']

# 只出现一次的又怎么样呢？
once = fdist1.hapaxes()

# 然后看看高频词的累积频率图，是否能猜出文章的风格和概要呢？
fdist2 = FreqDist(text2)
vocabulary1 = fdist2.keys()

# top50 = vocabulary1[:50]
fdist2.plot(50, cumulative=True)

# 寻找长词，一个单词长度大于15个字符的单词
v = set(text1)
long_words = [w for w in v if len(w) > 15]
sorted(long_words)

# 计算长词以及长词出现的次数大于7
fdist5 = FreqDist(text5)
s = sorted([w for w in fdist5 if len(w) > 7 and fdist5[w] > 7])

# 文本的搭配词，双连词（bigrams)
bi4 = bigrams(text4)
col = text4.collocations()

fdist = FreqDist(text5) #创建包含给定样本的频率分布
fdist.inc(text1) ##计数给定样本出现的次数
fdist.freq('monstrous') #给定样本的频率, 这个是什么意思？
fdist.N() #样本总数
fdist.keys() #以频率递减顺序排序的样本链表
#for sample in fdist: #以频率递减的顺序遍历样本
# fdist.max() #数值最大的样本
fdist.tabulate() #绘制频率分布表
fdist.plot() #绘制频率分布图


#在今天最后安装了jupyter作为可交互式解释器


# 第二章：
from nltk.corpus import gutenberg as gu

#fileid: 文件标识
for fileid in gu.fileids():
    num_chars = len(gu.raw(fileid))
    num_words = len(gu.words(fileid))
    num_sents = len(gu.sents(fileid))
    num_vocab = len([w.lower for w in gu.words(fileid)])
    print('num_chars:', int(num_chars/num_words), int(num_words/num_sents),
          int(num_words/num_vocab), fileid)

"""
这个程序显示每个文本的三个统计量：平均词长、平均句子长度和本文中每个词出现的
平均次数（我们的词汇多样性得分）。
num_chars: 4 24 1 austen-emma.txt
num_chars: 4 26 1 austen-persuasion.txt
num_chars: 4 28 1 austen-sense.txt
num_chars: 4 33 1 bible-kjv.txt
num_chars: 4 19 1 blake-poems.txt
num_chars: 4 19 1 bryant-stories.txt
num_chars: 4 17 1 burgess-busterbrown.txt
num_chars: 4 20 1 carroll-alice.txt
num_chars: 4 20 1 chesterton-ball.txt
num_chars: 4 22 1 chesterton-brown.txt
num_chars: 4 18 1 chesterton-thursday.txt
num_chars: 4 20 1 edgeworth-parents.txt
num_chars: 4 25 1 melville-moby_dick.txt
num_chars: 4 52 1 milton-paradise.txt
num_chars: 4 11 1 shakespeare-caesar.txt
num_chars: 4 12 1 shakespeare-hamlet.txt
num_chars: 4 12 1 shakespeare-macbeth.txt
num_chars: 4 36 1 whitman-leaves.txt

"""

from nltk.corpus import webtext, brown

for fileid in webtext.fileids():
    print(fileid, webtext.raw(fileid)[:65])

c = brown.categories()
w = brown.words(categories='fiction')

for w in w:
    w.lower().startwith('wh')
