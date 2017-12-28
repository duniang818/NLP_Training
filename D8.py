"""
@version: ??
@author: coco wang
@license: Apache Licence 
@contact: endoffight@gmail.com
@site: 
@software: PyCharm
@file: D8.py
@time: 2017/12/28 0028 上午 11:59
"""
# 搜索已分词文本
import nltk
from nltk.book import gutenberg, nps_chat

moby = nltk.Text(gutenberg.words('melville-moby_dick.txt'))
moby.findall(r'<a><.*><man>')

chat = nltk.Text(nps_chat.words())
chat.findall(r'<.*><.*><bro>')
chat.findall(r'<l.*>{3,}')

nltk.app.nemo()
nltk.re_show(r'\d', 'we are good friend, and you? how old are you? 25')
import re
re.search(r'\d', 'we are good friend, and you? how old are you? 25')

from  nltk.corpus import brown
hobbies_learend = nltk.Text(brown.words(categories=['hobbies', ['learned']]))
hobbies_learend.findall(r'<\w*><and><other><\w*s>')

# as x as y
x_y = nltk.Text(brown.words(categories=['fiction', 'romance']))
x_y.findall(r'<as><\w*><as><\w*>')

