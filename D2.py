# 确保python引用的是浮点数除法
from __future__ import division
from nltk.book import *

"""
@version: ??
@author: coco wang
@license: Apache Licence 
@contact: endoffight@gmail.com
@site: 
@software: PyCharm
@file: D2.py
@time: 2017/12/20 0020 下午 4:47
"""

"""
text1: Moby Dick by Herman Melville 1851 《白鲸记》
text2: Sense and Sensibility by Jane Austen 1811 《理智与情感》
text3: The Book of Genesis  <<创世纪>>
text4: Inaugural Address Corpus 《就职演说语料》
text5: Chat Corpus 《NPS 聊天语料库》
text6: Monty Python and the Holy Grail
text7: Wall Street Journal
text8: Personals Corpus
text9: The Man Who Was Thursday by G . K . Chesterton 1908
sent1: Call me Ishmael .
sent2: The family of Dashwood had long been settled in Sussex .
sent3: In the beginning God created the heaven and the earth .
sent4: Fellow - Citizens of the Senate and of the House of Representatives :
sent5: I have a problem with people PMing me to lol JOIN
sent6: SCENE 1 : [ wind ] [ clop clop clop ] KING ARTHUR : Whoa there !
sent7: Pierre Vinken , 61 years old , will join the board as a nonexecutive director Nov. 29 .
sent8: 25 SEXY MALE , seeks attrac older single lady , for discreet encounters .
sent9: THE suburb of Saffron Park lay on the sunset side of London , as red and ragged as a cloud of sunset .
"""


texts()
sents()
# concordance:用语索引
text1.concordance('monstrous')
text1.similar('monstrous')
# 索引多个词相同的上下文
text2.common_contexts(['monstrous', 'very'])
# 离散图，计算词在文本中出现的位置
text4.dispersion_plot(['citizens', 'democracy', 'freedom', 'duties', 'America'])
# 这个方法目前不能直接调用，待查
text3.generate('')
"""
text3.generate()
Traceback (most recent call last):
  File "<input>", line 1, in <module>
TypeError: generate() missing 1 required positional argument: 'words'
"""

len(text3)
sorted(set(text3))
len(sorted(set(text3)))
text3.count('smote')
text3.count('smote') / len(text3) * 100
# 计算一个文本使用词汇的多样性
len(text1) / len(set(text1))

100 * text5.count('lol') / len(text5)


def lexical_diversity(text):
    return len(text) / len(set(text))


def percentage(text, words):
    return 100 * text.count(words) / len(set(text))


add_list = sent2 + sent3
# list slice
add_list[:9]
add_list[1:]
add_list.append('appendings')

"""
注意！
为 Python 变量选择名称（或标识符）时请注意：首先，应该以字母开始，
后面跟数字（0 到 9）或字母。因此，abc23 是好的，23abc 会导致一个语
法错误。名称是大小写敏感的。这意味着 myVar 和 myvar 是不同的变量。
变量名不能包含空格，但可以用下划线把单词分开，如 my_var。注意不要
插入连字符来代替下划线：my-var 不对，因为 Python 会把-解释为减号

"""

# 字符串可以做乘法和加法
str = 'Wednesday'
str = str * 2
# 用list讲string连接为一个str
j = ' '.join(['111', '2222'])
# 将一个string分割为一个list
s = j.split(' ')


