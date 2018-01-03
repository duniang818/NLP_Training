"""
@version: Chap.4
@author: coco wang
@license: Apache Licence 
@contact: zhuce_2012@qq.com
@site: 
@software: PyCharm
@file: D10.py
@time: 2018/1/3 0003 上午 9:04
"""
w = ()
word = w
w is word
id(w) is id(word)

# assert isinstance(word, w), 'word is in the different memory with w.'
assert isinstance(word, w), "argument to tag() must be a string"

filter(lambda w: len(w for w in 'word, that, what'), range(10))
map(lambda w: len(filter(lambda c: c.lower() in "aeiou", w)), 'we are women.')
[len([c for c in w if c.lower() in "aeiou"]) for w in 'we are women.']

"""
这些被称为关键字参数。如果我们混合使用这两种参数，就必须确保未命名的参数在命
名的参数前面。必须是这样，因为未命名参数是根据位置来定义的。我们可以定义一个函数，
接受任意数量的未命名和命名参数，并通过一个就地的参数链表*args 和一个就地的关键
字参数字典**kwargs 来访问它们。

当*args 作为函数参数时，它实际上对应函数所有的未命名参数。下面是另一个这方
面的 Python 语法的演示，思考处理可变数目的参数的函数 zip()。我们将使用变量名*son
g 来表示名字*args 并没有什么特别的。

注意！
注意不要使用可变对象作为参数的默认值。这个函数的一系列调用将使用
同一个对象，有时会出现离奇的结果，就像我们稍后会在关于调试的讨论
中看到的那样。

模块的一些变量和函数仅用于模块内部。它们的名字应该以下划线开头，如_
helper()，因为这将隐藏名称。如果另一个模块使用习惯用法：from modul
e import * 导入这个模块，这些名称将不会被导入。你可以选择性的列出一
个模块的外部可访问的名称，使用像这样的一个特殊的内置变量：__all__ =
['edit_distance', 'jaccard_distance']。
"""

import pdb
import nltk


def find_words(text, wordlength, result=[]):
    for word in text:
        if len(word) == wordlength:
            result.append(word)
    return result


find_words(['cat'], 3)
pdb.run("find_words(['dog'], 3)")

# 算法设计
def factorial2(n):
    if n == 1:
        return 1
    else:
        return n * factorial2(n-1)

# dynamic programming这个在chap.8.4时再详细看
#matlabplot

#4-10.

import pylab
colors = 'rgcmyk'      #red, green, blue, cyan, magenta, yellow, black
def bar_chart(categories, words, counts):
    """Plot a bar char showing counts for each word by category"""

    ind = pylab.arange(len(words))
    width = 1/(len(categories) + 1)
    bar_groups = []
    for c in range(len(categories)):
        bars = pylab.bar(ind + c * width, counts[categories[c]], width, color=colors[c % len(colors)])
        bar_groups.append(bars)
        print('ind:\n', ind,
              'width: \n', width,
              'ind + c*width:\n', ind + c * width,
              'categories[c]:\n', categories[c],
              'counts[categories[c]]:\n', counts[categories[c]])
    pylab.xticks(ind + width, words)
    pylab.legend([b[0] for b in bar_groups], categories, loc='upper left')
    pylab.ylabel('Frequency')
    pylab.title('Frequency of Six Modal Verbs by Genre')
    pylab.show()


genres = ['news', 'religion', 'hobbies', 'government', 'adventure']
modals = ['can', 'could', 'may', 'might', 'must', 'will']
cfdist = nltk.ConditionalFreqDist((genre, word) for genre in genres
                                  for word in nltk.corpus.brown.words(categories=genre) if word in modals)

# 在相应分类下的情态动词各自的个数
counts = {}
for genre in genres:
    counts[genre] = [cfdist[genre][word] for word in modals]
bar_chart(genres, modals, counts)

import matplotlib
matplotlib.use('TkAgg')
pylab.savefig('modal.png')
print('Content-Type: text/html')
print()
print('<html><body>')
print('<img src="modal.png"/>')
print('</body></html>')

# Networkx
import networkx as nx
import matplotlib
from nltk.corpus import wordnet as wn
"""
need install: networkx, graphviz, pygraphviz(needs vs build tools)
"""


def traverse(graph, start, node):
    graph.depth[node.name] = node.shortest_path_distance(start)
    for child in node.hyponyms():
        graph.add_edge(node.name, child.name)
        traverse(graph, start, child)

def hyponym_graph(start):
    G = nx.Graph()
    G.depth = {}
    traverse(G, start, start)
    return G

def graph_draw(graph):
    nx.draw_graphviz(graph, node_size = [16 * graph.degree(n)
                                         for n in graph],
                     node_color = [graph.depth[n] for n in graph],
                     with_labels = False)
    matplotlib.pyplot.show()

dog = wn.synset('dog.n.01')
graph = hyponym_graph(dog)
graph_draw(graph)
