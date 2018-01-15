"""
@version: ??
@author: coco wang
@license: Apache Licence 
@contact: zhuce_2012@qq.com
@site: 
@software: PyCharm
@file: D16.py
@time: 2018/1/15 0015 下午 3:43
"""
#简单评估和基准

import nltk
from nltk.corpus import conll2000

cp = nltk.RegexpParser("")
test_sents = conll2000.chunked_sents('test.txt', chunk_types=['NP'])
print(cp.evaluate(test_sents))

grammar = r"NP: {<[CDJNP].*>+}"
cp = nltk.RegexpParser(grammar)
print(cp.evaluate(test_sents))


class UnigramChunker(nltk.ChunkParserI):
    def __init__(self, train_sents):
        train_data = [[(t, c) for w, t, c in
                       nltk.chunk.tree2conlltags(sent)
                       for sent in train_sents]]


import re

# (?!...) 取反
IN = re.compile(r'.*\bin\b(?!\b.+ing)')
for doc in nltk.corpus.ieer.parsed_docs('NYT_19980315'):
    for rel in nltk.sem.extract_rels('ORG', 'LOC',
                                     doc,
                                     corpus='ieer',
                                     pattern= IN):
        # print(nltk.sem.rtuple(rel))
        print(nltk.sem.rtuple(rel, lcon=True, rcon=True))


# 第5/6/7三章，完全不太懂
# 下面继续第8章：
