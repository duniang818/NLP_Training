"""
@version: ??
@author: coco wang
@license: Apache Licence 
@contact: zhuce_2012@qq.com
@site: 
@software: PyCharm
@file: D17.py
@time: 2018/1/17 0017 上午 9:37
"""
# 分析句子结构
import nltk


groucho_grammar = nltk.parse_cfg("""
... S -> NP VP
... PP -> P NP
... NP -> Det N | Det N PP | 'I'
... VP -> V NP | VP PP
... Det -> 'an' | 'my'
... N -> 'elephant' | 'pajamas'
... V -> 'shot'
... P -> 'in'
... """)

sent = ['I', 'shot', 'an', 'elephant', 'in', 'my', 'pajamas']
parser = nltk.ChartParser(groucho_grammar)
trees = parser.nbest_parse(sent)
for tree in trees:
    print(tree)



sr_parse = nltk.ShiftReduceParser(groucho_grammar)
sent = 'Mary saw a dog'.split()
print(sr_parse.parse(sent))


#wfst:符合文法的子串链表

#8.6 文法开发
from nltk.corpus import treebank


t = treebank.parsed_sents('wsj_0001.mrg')[0]
print(t)

def filter(tree):
    child_nodes = [child.node for child in tree
                   if isinstance(child, nltk.tree)]
    return (tree.node == 'VP') and ('S' in child_nodes)

[subtree for tree in treebank.parsed_sents()
 for subtree in tree.subtree(filter)]

# 文法是难点，也是重点
#Chap.9 还是继续文法，需要扩充阅读

#9-1.基于特征的文法例子
nltk.data.show_cfg('grammars/book_grammars/feat0.fcfg')

tokens = 'Kim likes children'.split()
from nltk import load_parser


cp = load_parser('grammars/book_grammars/feat0.fcfg', trace=2)
trees = cp.parse_one(tokens)

fs1 = nltk.FeatStruct(TENSE='past', NUM='sg')
print(fs1)

fs1 = nltk.FeatStruct(PER=3, NUM='pl', GND='fem')
fs2 = nltk.FeatStruct(POS='N', AGR=fs1)
print(fs2['AGR']['PER'])

#将特征结构看作为有向无环图（directed acyclic graphs, DAGs）
#当两条路径具有相同的值时，它们被称为是
# 为了在我们的矩阵式表示中表示重入，我们将在共享的特征结构第一次出现的地方加一
# 个括号括起的数字前缀，例如（1）。以后任何对这个结构的引用将使用符号->(1)，如下所
# 示。
# 等价的。
print nltk.FeatStruct("""[NAME='Lee', ADDRESS=(1)[NUMBER=74, STREET='rue Pascal'],
... SPOUSE=[NAME='Kim', ADDRESS->(1)]]""")

#合并两个特征结构的信息被称为统一，由方法 unify()支持
print(fs1.unify(fs2))

fs1 = nltk.FeatStruct("[ADDRESS1=[NUMBER=74, STREET='rue Pascal']]")
fs2 = nltk.FeatStruct("[ADDRESS1=?x, ADDRESS2=?x]")
print fs2.unify(fs1)