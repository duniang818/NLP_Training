"""
@version: ??
@author: coco wang
@license: Apache Licence 
@contact: zhuce_2012@qq.com
@site: 
@software: PyCharm
@file: D13.py
@time: 2018/1/9 0009 下午 10:33
"""

#停止了三天，我的手机拿去扩容，结果被修理工农坏了，把主板的一个线断了，多么糟糕的事情，这几天好多事情都没有正常运转，手机越来越重要了。。。

#cha.6 学习分类文本
# 性别分类器
from nltk.corpus import names
import nltk
import random
name_g = ([(name, 'male') for name in names.words('male.txt')] +
         [(name, 'female') for name in names.words('female.txt')])

random.shuffle(name_g)

def gender_features(word):
    return {'last_lestter' : word[-1]}


featuresets = [(gender_features(n), g) for (n, g) in name_g]
train_set, test_set = featuresets[500:], featuresets[:500]
# 朴素贝叶斯分类器，监督学习，离散分类
classifer = nltk.NaiveBayesClassifier.train(train_set)

classifer.classify(gender_features('Neo'))

print(nltk.classify.accuracy(classifer, test_set))

# 似然比
classifer.show_most_informative_features(5)

# error analyse
# 用开发测试集来进行错误分析，用测试集来进行最终的评估
# 训练集用于训练模型分类器

# 文档分类
from nltk.corpus import movie_reviews
documents = [(list(movie_reviews.words(fileid)), category)
             for category in movie_reviews.categories()
             for fileid in movie_reviews.fileids(category)]
random.shuffle(documents)

all_words = nltk.FreqDist(w.lower() for w in movie_reviews.words())
word_features = all_words.keys()[:200]

def document_features(document):
    document_words = set(document)
    features = {}
    for word in word_features:
        features['contains(%s)' % word] = (word in document_words)
    return features


# 注意集合中搜索要比list中快
print(document_features(movie_reviews.words('pos/cv957_8737.txt')))


def pos_features(sentence, i):
    features = {
        "suffix(1)": sentence[i][-1:],
        "suffix(2)": sentence[i][-2:],
        "suffix(3)": sentence[i][-3]
    }
    if i == 0:
        features["prev-word"] = '<START>'
    else:
        features["prev-word"] = sentence[i-1]
    return features

from nltk.corpus import brown

#第一个句子的第8个词
pos_features(brown.sents()[0], 8)

#给句子做标注,以句子为一个链表元素，标记句子里面每个词的词性
tagged_sents = brown.tagged_sents(categories='news')
featuresets = []


# 给标注的词添加位置信息，但是为什么要这么做？而且之前标注的词tag没有变
# 怎么就提高了tag的准确性呢？没有看明白
for tagged_sent in tagged_sents:
    #消除标注
    untagged_sent = nltk.tag.untag(tagged_sent)
    for i, (word, tag) in enumerate(tagged_sent):
        featuresets.append(
            (pos_features(untagged_sent, i), tag)
        )

size = int(len(featuresets) * 0.1)
train_set, test_set = featuresets[size:], featuresets[:size]
classifer = nltk.NaiveBayesClassifier.train(train_set)
nltk.classify.accuracy(test_set)

#前面的分类都是独立词的分类
#而优势需要上下文相关性的联合分类
# 序列分类



def pos_features2(sentence, i, history):
    features = {
        "suffix(1)": sentence[i][-1:],
        "suffix(2)": sentence[i][-2:],
        "suffix(3)": sentence[i][-3]
    }
    if i == 0:
        features["prev-word"] = '<START>'
        features["prev-tag"] = '<START>'
    else:
        features["prev-word"] = sentence[i-1]
        features["prev-tag"] = history[i-1]
    return features

class ConsecutivePosTagger(nltk.TaggerI):
    def __init__(self, train_sents):
        train_set = []
        for tagged_sent in train_sents:
            untagged_sent = nltk.tag.untag(tagged_sent)
            history = []
            for i, (word, tag) in enumerate(tagged_sent):
                featureset = pos_features(untagged_sent, i, history)
                train_set.append(featureset, tag)
                history.append(tag)
            self.classifier = nltk.NaiveBayesClassifier.train(train_set)

        def tag(self, sentence):
            history =[]
            for i, word in enumerate(sentence):
                featureset = pos_features(sentence, i ,history)
                tag = self.classifier.classify(featureset)
                history.append(tag)
            return zip(sentence, history)


