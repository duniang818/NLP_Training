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
"""