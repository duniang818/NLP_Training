"""
@version: ??
@author: coco wang
@license: Apache Licence 
@contact: zhuce_2012@qq.com
@site: 
@software: PyCharm
@file: D18.py
@time: 2018/1/23 0023 上午 10:43
"""

"""
我们将借此机会重新表述前面的命题逻辑的语法规则，并添加量词的形式化规则；所有
这些一起组成一阶逻辑的句法。此外，我们会明确相关表达式的类型。我们将采取约定：<
en
, t>是一种由 n 个类型为 e 的参数组成产生一个类型为 t 的表达式的谓词的类型。在这
种情况下，我们说 n 是谓词的元数
"""
#chap.10需要额外的阅读

# timit
import nltk
from nltk.corpus import timit

timit.fileids()
help(timit)

phonetic = timit.phones('dr1-fvmh0/sa1')
timit.word_times('dr1-fvmh0/sa1')

timitdict = timit.transcription_dict()
timitdict['greasy'] + timitdict['wash'] + timitdict['water']


nltk.corpus.timit.spkrinfo('dr1-fvmh0')

import csv
lexicon = csv.reader(open('dict.csv'))
pairs = [(lexeme, defn) for (lexeme, _, _, defn) in lexicon]
lexemes, defns = zip(*pairs)
defn_words = set(w for defn in defns for w in defn.split())
sorted(defn_words.difference(lexemes))

# python中的ElementTree
nltk.download('shakespeare')
merchant_file = nltk.data.find('corpora/shakespeare/merchant.xml')
raw = open(merchant_file).read()
print(raw[0:168])

from nltk.etree.ElementTree import ElementTree

# The first time is over.

