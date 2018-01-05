"""
@version: ??
@author: coco wang
@license: Apache Licence 
@contact: zhuce_2012@qq.com
@site: 
@software: PyCharm
@file: D11.py
@time: 2018/1/4 0004 下午 2:43
"""
import nltk


sent = 'I have hearned from many of you today about the ' \
       'presendential election.'
text = nltk.word_tokenize(sent)
taged = nltk.pos_tag(text)
# [nltk.tag.str2tuple(t) for t in taged]

nltk.corpus.brown.tagged_words()

from nltk.corpus import brown
brown_news_tagged = brown.tagged_words(categories='news')
tag_fd = nltk.FreqDist(tag for (word, tag) in brown_news_tagged)
tag_fd.most_common(5)
tag_fd.plot(5)

word_tag_pairs = nltk.bigrams(brown_news_tagged)
# output:((',', ','), ('read', 'VB'))

#找出最频繁的名词标记的程序
def findtags(tag_prefix, tagged_text):
       cfd = nltk.ConditionalFreqDist((word, tag)
                                      for (word, tag)
                                      in tagged_text
                                      if tag.startswith(tag_prefix))
       return dict((word, cfd[word]) for word in cfd.conditions())

tagdict = findtags('NN', nltk.corpus.brown.tagged_words(categories='news'))


brown_learned_text = brown.words(categories='learned')

#找出跟在often后面的词汇
sorted(set(b for (a,b) in nltk.bigrams(brown_learned_text) if a == 'often'))


brown_learned_text = brown.tagged_words(categories='news')
tags = [b[1] for (a, b) in nltk.bigrams(brown_learned_text) if a[0] == 'often']
fd = nltk.FreqDist(tags)
fd.tabulate()

# output: VB  JJ  AT  CS VBD QLP VBZ   .   , DOD  IN
#         3   2   1   1   1   1   1   1   1   1   1


#例 5-2. 使用 POS 标记寻找三词短语

from nltk.corpus import brown
def process(sentence):
       for (w1, t1), (w2, t2), (w3, t3) in nltk.trigrams(sentence):
              if (t1.startswith('V') and t2 == 'TO'
                      and t3.startswith('V')):
                     print(w1, w2, w3)

for tagged_sent in brown.tagged_sents():
       process(tagged_sent)


# 映射{}：它是映射不是序列。其键值不是按赋值顺序存放的

#字典的键是唯一的，但是一个键可以存在多个值，用链表赋值：pos['sleep'] =['V','N']

#请注意：字典的键必须是不可改变的类型，如字符串和元组。如果我们尝试使用可变键
#定义字典会得到一个 TypeError

# 我们可以使用键-值对格式创建字典。有两种方式做这个，我们通常会使用第一个：
# >>> pos = {'colorless': 'ADJ', 'ideas': 'N', 'sleep': 'V', 'furiously': 'ADV'}
# >>> pos = dict(colorless='ADJ', ideas='N', sleep='V', furiously='ADV')

alice = nltk.corpus.gutenberg.words('carroll-alice.txt')
vocab = nltk.FreqDist(alice)
v1000 = sorted(vocab)[:1000]
mapping = nltk.defaultdict(lambda : 'UNK')
for v in v1000:
       mapping[v] = v

alice2 = [mapping[v] for v in alice]
alice2[:100]

#递增更新字典，按值排序
counts = nltk.defaultdict(int)
for (word, tag) in brown_news_tagged:
       counts[tag] += 1

from operator import itemgetter
sorted(counts.items(), key=itemgetter(1), reverse=True)
[t for t, c in sorted(counts.items(), key=itemgetter(1), reverse=True)]

# 按最后两个字母索引词汇
last_letters = nltk.defaultdict(list)
words = nltk.corpus.words.words('en')
for word in words:
       key = word[-2:]
       last_letters[key].append(word)

last_letters['ly']

# words = words[:5]
anagrams = nltk.defaultdict(list)
for word in words:
       print('word:', word)
       # 按照词的字母排序后，也就是只要含有这些字母的词都可以放到同一个key里面
       # 这个功能就是看由相同字母组成的词有哪些
       key = ''.join(sorted(word))
       print('key:', key)
       anagrams[key].append(word)

anagrams = nltk.Index((''.join(sorted(w)), w) for w in words)
anagrams['aeilnrt']


#反向创建一个键值对字典
pos = {'colorless': 'ADJ', 'ideas': 'N'}
pos2 = dict((value, key) for (key, value) in pos.items())