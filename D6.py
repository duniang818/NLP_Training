from __future__ import division
"""
@version: ??
@author: coco wang
@license: Apache Licence 
@contact: endoffight@gmail.com
@site: 
@software: PyCharm
@file: D6.py
@time: 2017/12/26 0026 上午 11:41
"""

"""
在一个文件中的变量和函数定义的集合被称为一个 Python 模块（module）。相关模块的
集合称为一个包（package）。处理布朗语料库的 NLTK 代码是一个模块，处理各种不同的语
料库的代码的集合是一个包。NLTK 的本身是包的集合，有时被称为一个库（library）
"""

from nltk.corpus import toolbox

en = toolbox.entries('rotokas.dic')
print(en)

#第二章结束，看的比较糙。下面接着第三章开始
#第三种非常重要的来了，加工原料文本，分词和词干提取。


import nltk, re, pprint

#从已知的url上访问资料
#这里要注意与书中用的库路径问题，基于python3.5
from urllib import request as ureq


url = 'http://www.gutenberg.org/files/2554/2554.txt'
url = 'http://www.gutenberg.org/files/2554/2554-h/2554-h.htm'
raw = ureq.urlopen(url).read()
type(raw)
len(raw)
raw[:75]

tokens = nltk.word_tokenize(raw)
type(tokens)
len(tokens)
tokens[:10]

text = nltk.Text(tokens)
type(text)
#搭配词,文中的搭配词
text.collocations()

#string 的方式
# find是从左边开始找，rfind是从右边（反向）开始找
raw.find('PART I')
raw.rfind("End of Project Gutenberg's Crime")
#切片
raw[0:90]
