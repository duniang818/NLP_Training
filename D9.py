"""
@version: cha 3.6 规范化文本
@author: coco wang
@license: Apache Licence 
@contact: zhuce_2012@@qq.com
@site: 
@software: PyCharm
@file: D9.py
@time: 2018/1/2 0002 上午 6:37
"""

# 词干提取器：Poter,Lancaster

import nltk
porter = nltk.PorterStemmer()
lancaster = nltk.LancasterStemmer()
tokens = nltk.word_tokenize(r'Do schools kill creativity by Sir Ken Robinson. Good morning, How are you? It\'s been great, '
                            r'hasn\'s it?'
                            r'I\'ve been blown away by the whole thing. In fact, I\'m leaving.')
[porter.stem(t) for t in tokens]
[lancaster.stem(t) for t in tokens]

"""
Python 用下划线作为变量前缀和后缀指定特殊变量

_xxx 不能用’from module import *’导入

__xxx__ 系统定义名字

__xxx 类中的私有变量名

核心风格：避免用下划线作为变量名的开始。

因为下划线对解释器有特殊的意义，而且是内建标识符所使用的符号，我们建议程序员避免用下划线作为变量名的开始。一般来讲，
变量名_xxx被看作是“私有 的”，在模块或类外不可以使用。当变量是私有的时候，用_xxx 来表示变量是很好的习惯。因为变量名__xxx__对Python 来说有特殊含义，
对于普通的变量应当避免这种命名风格。

“单下划线” 开始的成员变量叫做保护变量，意思是只有类对象和子类对象自己能访问到这些变量；
“双下划线” 开始的是私有成员，意思是只有类对象自己能访问，连子类对象也不能访问到这个数据。

以单下划线开头（_foo）的代表不能直接访问的类属性，需通过类提供的接口进行访问，不能用“from xxx import *”而导入；以双下划线开头的（__foo）
代表类的私有成员；以双下划线开头和结尾的（__foo__）代表python里特殊方法专用的标识，如 __init__（）代表类的构造函数。
"""

ldisplay = '%*s' % (7, 'There have been three themes running through the conference which are relevant to what i want to talk about.')

# 打印格式：-左对齐，*右对齐
#py3.0+  请查看python的格式化输出

# 词形归并器
# wnl = nltk.WordNetLemmatizer()
# [wnl(t) for t in tokens]

# 用正则表达式来分词
import re
raw = 'One is the extraordinary evidence of human creativity in all of the presentations that we\'ve had and in all of the people' \
      'here.'
re.split(r'\s+', raw)

#r'\s+' 是一种约定简写所有的匹配空白字符。同等等于r'[ \t\n]+'

print(re.findall(r"\w+(?:[-']\w+)*|'|[-.(]+|\S\w*", raw))

text = 'That U.S.A poster-print costs $12.40...'
patter = r'''(?x)([A-Z]\.)+|\w+(-\w+)*|\$?\d+(\.\d+)?%?' \
         r'|\.\.\. |[][.,;'"?():-_`"]'''
nltk.regexp_tokenize(text, patter)

"""
SA:随机寻优算法
模拟退火算法(Simulated Annealing，SA)最早的思想是由N. Metropolis[1]  等人于1953年提出。1983 年,S. Kirkpatrick 等成功地将退火思想引入到
组合优化领域。
它是基于Monte-Carlo迭代求解策略的一种随机寻优算法，其出发点是基于物理中固体物质的退火过程与一般组合优化问题之间的相似性。模拟退火算法从某一较高初温出发，
伴随温度参数的不断下降,结合概率突跳特性在解空间中随机寻找目标函数的全局最优解，即在局部最优解能概率性地跳出并最终趋于全局最优。模拟退火算法是一种通用的优化
算法，理论上算法具有概率的全局优化性能,目前已在工程中得到了广泛应用，诸如VLSI、生产调度、控制工程、机器学习、神经网络、信号处理等领域。
模拟退火算法是通过赋予搜索过程一种时变且最终趋于零的概率突跳性，从而可有效避免陷入局部极小并最终趋于全局最优的串行结构的优化算法。
"""
from random import randint
def segment(text, segs):
    words = []
    last = 0
    for i in range(len(segs)):
        if segs[i] == '1':
            words.append(text[last:i+1])
            last = i + 1
    words.append(text[last:])
    return words

def evaluate(text, segs):
    words = segment(text, segs)
    text_size = len(words)      #有多少分词项
    lexicon_size = len(''.join(list(set(words))))
    return text_size + lexicon_size

def flip(segs, pos):
    return segs[:pos] + str(1 - int(segs[pos])) + segs[pos+1:]

def flip_n(segs, n):
    for i in range(n):
        segs = flip(segs, randint(0, len(segs)-1))
        return segs

def anneal(text, segs, iterations, cooling_rate):
    temperature = float(len(segs))
    while temperature > 0.5:
        best_segs, best = segs, evaluate(text, segs)
        for i in range(iterations):
            guess = flip_n(segs, int(round(temperature)))
            score = evaluate(text, guess)
            if score < best:
                best, best_segs = score, guess
        score, segs = best, best_segs
        temperature = temperature / cooling_rate
        print(evaluate(text, segs), segment(text, segs))
    print()
    return segs


#将结果写入文件
from nltk.corpus import genesis
output_file = open('output.txt', 'w')
words = set(nltk.corpus.genesis.words('english-kjv.txt'))
for word in sorted(words):
    output_file.write(word + '\n')
output_file.close()


"""
python的set和其他语言类似, 是一个无序不重复元素集, 基本功能包括关系测试和消除重复元素. 集合对象还支持union(联合), 
intersection(交), difference(差)和sysmmetric difference(对称差集)等数学运算. 
"""

from textwrap import fill
saying = 'text begins a new ling.'
format = '%s (%d),'
pieces = [format % (word, len(word)) for word in saying]
output = ''.join(pieces)


#cha. 4,字符串赋值和结构化对象赋值
foo = 'python'
bar = foo
