"""
@version: 正则表达式标注器
@author: coco wang
@license: Apache Licence 
@contact: zhuce_2012@qq.com
@site: 
@software: PyCharm
@file: D12.py
@time: 2018/1/5 0005 上午 11:53
"""

import nltk
from nltk.corpus import brown

brown_tagged_sents = brown.tagged_sents(categories='news')
brown_sents = brown.sents(categories='news')
patters = [(r'.*ing$', 'VBG'), (r'.*ed$', 'VBD'), (r'.*es$', 'VBZ'),
           (r'.*ould$', 'MD'), (r'.*\'s$', 'NN$'), (r'.*s$', 'NNS'),
           (r'^-?[0-9]+(.[0-9]+)?$', 'CD'), (r'.*', 'NN')]

regexp_tagger = nltk.RegexpTagger(patters)
regexp_tagger.tag(brown_sents[3])

regexp_tagger.evaluate(brown_tagged_sents)

# 查找标注器的性能，使用不同大小的模型
def performance(cfd, wordlist):
    lt = dict((word, cfd[word].max()) for word in wordlist)
    baseline_tagger = nltk.UnigramTagger(model=lt, backoff=nltk.DefaultTagger('NN'))
    return baseline_tagger.evaluate(brown.tagged_sents(categories='news'))

def display():
    import pylab
    words_by_freq = list(nltk.FreqDist(brown.words(categories='news')))
    cfd = nltk.ConditionalFreqDist(brown.tagged_words(categories='news'))
    sizes = 2 ** pylab.arange(15)
    perfs = [performance(cfd, words_by_freq[:size]) for size in sizes]
    pylab.plot(sizes, perfs, '-bo')
    pylab.title('Lookup Tagger Performance with Varying Model Size')
    pylab.xlabel('Model Size')
    pylab.ylabel('Performance')
    pylab.show()

display()

###为了查看，brown_sents, brown_tagged_sents的内容组成，将其输出到本地文件brow_sents
f = open('brown_sents.txt', 'w')
for string in [len(brown_sents), brown_sents, 'tagged sents begin:', brown_tagged_sents]:
    f.write(str(string) + '\n')
    if string == brown_sents:
        f.write(str(brown_sents[3]) + '\n')
        f.write(str(brown_sents[2007]) + '\n')
f.close()
#5.5

unigram_tagger = nltk.UnigramTagger(brown_tagged_sents)
unigram_tagger.tag((brown_sents[2007]))
unigram_tagger.evaluate(brown_tagged_sents)

#分离训练数据和测试数据
size = int(len(brown_tagged_sents) * 0.9)
train_sents = brown_tagged_sents[:size]
test_sents = brown_tagged_sents[size:]
unigram_tagger = nltk.UnigramTagger(train_sents)
unigram_tagger.evaluate(test_sents)


# n-gram tagger
# n 元标准器
bigram_tagger = nltk.BigramTagger(train_sents)
#对已经训练过的数据标准表现的还不错
bigram_tagger.tag(brown_sents[2007])
#但是对没有见过的数据标注表现很差
bigram_tagger.tag(brown_sents[4203])

# N-gram 标注器不应考虑跨越句子边界的上下文。因此，NLTK 的标注器被
# 设计用于句子链表，一个句子是一个词链表。在一个句子的开始，tn-1和前
# 面的标记被设置为 None。

t0 = nltk.DefaultTagger('NN')
t1 = nltk.UnigramTagger(train_sents, backoff=t0)
t2 = nltk.BigramTagger(train_sents, backoff=t1)
t3 = nltk.TrigramTagger(train_sents, backoff=t2)






