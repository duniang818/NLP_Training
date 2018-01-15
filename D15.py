"""
@version: ??
@author: coco wang
@license: Apache Licence 
@contact: zhuce_2012@qq.com
@site: 
@software: PyCharm
@file: D15.py
@time: 2018/1/12 0012 上午 11:01
"""

# 怎么总是记不住正则中的*是0次或多次呢？，该死
import nltk
cp = nltk.RegexpParser('CHUNK: {<V.*><TO><V.*>}')
brown = nltk.corpus.brown
for sent in brown.tagged_sents():
    tree = cp.parse(sent)
    for subtree in tree.subtrees():
        # 请大家注意，因为这本书历史有点久远，有很多方法已经改变了
        if subtree.label() == 'CHUNK':
            print(subtree)

"""
将上面的例子封装在函数 find_chunks()内，以一个如"CHUN
K: {<V.*> <TO><V.*>}"的块字符串作为参数。用它来搜索语料库寻
找其他几个模式，如四个或更多的连续的名词即"NOUNS:{<N.*>{4,}}
"
"""
def find_chunk(cp, train_sents):
    for sent in train_sents:
        tree = cp.parse(sent)
        for subtree in tree.subtrees():
            if subtree.label == 'CHUNK':
                print(subtree)

cp = nltk.RegexpParser("NOUNS:{<N.*>{4,}}")
sents = nltk.corpus.brown.tagged_sents()

find_chunk(cp, sents)