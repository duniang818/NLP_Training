"""
@version: ??
@author: coco wang
@license: Apache Licence 
@contact: endoffight@gmail.com
@site: 
@software: PyCharm
@file: D7.py
@time: 2017/12/27 0027 上午 11:39
"""

# htlm
from urllib import request
import nltk
from  bs4 import BeautifulSoup as bs
#更多更复杂的有关处理 HTML 的内容，可以使用 http://www.crummy.com/soft
#ware/BeautifulSoup/上的 Beautiful Soup 软件包。这个网址已经不正了，请
#参阅新的网址：https://www.crummy.com/software/BeautifulSoup/bs4/doc/#installing-beautiful-soup
#https://pypi.python.org/pypi/beautifulsoup4/
#pip install beautifulsoap4
#pip install lxml


url = 'http://news.bbc.co.uk/2/hi/health/2284783.stm'
html = request.urlopen(url).read()
type(html)
print(html)

#raise NotImplementedError ("To remove HTML markup, use BeautifulSoup's get_text() function")
#raw = nltk.clean_html(html)
soup = bs(html)

# or soup = bs(html,'lxml')
#格式化输出html内容
print(soup.prettify())

tokens = nltk.word_tokenize(str(soup))
print(tokens)
tokens = tokens[96:399]
#
text = nltk.Text(tokens)
# #含有gene词的索引
text.concordance('gene')

##############rss parser using feedparser
# 源码安装 https://pypi.python.org/pypi/feedparser#downloads
# python setup.py install
import feedparser
llog = feedparser.parse("http://languagelog.ldc.upenn.edu/nll/?feed=atom")
print('llog:\n', llog)
llog['feed']['title']
post = llog.entries[2]
post.title

content = post.content[0].value
content[:70]

# 读取本地文件
# open(), read()
#\v可以作为转义字符，表示纵向制表符，这里你把后斜杠全部改为前斜杠试试。建议以后凡是路径名中的\，全部改为\\或者/，以避免转义字符的歧义。
# r'filepath'
f = open(r'C:\Users\Administrator\PycharmProjects\NLP\document.txt')
file_text = f.read()

# or， 选择下面的方式，避免错误
import os, re
os.listdir('.')
f = open('document.txt', 'rU')
file_text = f.read()

# 从word, pdf，二进制文件中读入数据
# 从用户输入处读入数据,python3 使用的是内置函数input,而不同的是input，输入如果是字符串的时候需要“输入的内容”
i = input('Enter some text:')

# a = ['1', '2', '3', '4', '5', '6', '7', '6', '5', '4', '3', '2', '1']
# b = [' ' * 2 * (7 - i) + 'very' * i for i in a]
# for line in b:
#     print(line)

nacute = u'\u0144'
nacute_utf = nacute.encode('utf-8')
print(repr(nacute_utf))

#.表示匹配任意的单个字符，^匹配开始，$匹配结束，？匹配前面的字符可有可无
# + 表示至少一次，* 表示零次或者多次，是？和+的并集

# 讲日期2009-12-31转换成[2009,12,31]的链表
da = re.findall('[\d]+[^-]', '2009-12-31')

re.findall(r'^.*(ing|ly|ed|ious|ies|ive|es|s|ment)$', 'processing')
#?:
re.findall(r'^.*(?:ing|ly|ed|ious|ies|ive|es|s|ment)$', 'processing')
re.findall(r'^(.*)(ing|ly|ed|ious|ies|ive|es|s|ment)$', 'processing')
#?非贪婪模式
re.findall(r'^(.*?)(ing|ly|ed|ious|ies|ive|es|s|ment)$', 'processes')
re.findall(r'^(.*?)(ing|ly|ed|ious|ies|ive|es|s|ment)?$', 'language')

#提取词干的方法

def stem(word):
    regexp = r'^(.*?)(ing|es|s|ed|ies|ive|ment|ly|ious)?$'
    stem, suffix = re.findall(regexp, word)[0]
    return stem

raw = """DENNIS: Listen, strange women lying in ponds distributing swords
... is no basis for a system of government. Supreme executive power derives from
... a mandate from the masses, not from some farcical aquatic ceremony."""

tokens = nltk.word_tokenize(raw)

[stem(t) for t in tokens]