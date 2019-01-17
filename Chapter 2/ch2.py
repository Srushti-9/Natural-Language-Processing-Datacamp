Python 3.7.2 (tags/v3.7.2:9a3ffc0492, Dec 23 2018, 23:09:28) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> from nltk.tokenize import word_tokenize
 
>>> from collections import Counter
>>> Counter(word_tokenize("The cat is in teh box.The cat likes teh box.The box is over the cat."))
Counter({'cat': 3, 'is': 2, 'teh': 2, 'box.The': 2, 'The': 1, 'in': 1, 'likes': 1, 'box': 1, 'over': 1, 'the': 1, '.': 1})
>>> 
counter.most
Traceback (most recent call last):
  File "<pyshell#3>", line 2, in <module>
    counter.most
NameError: name 'counter' is not defined
>>> counter.most_commomn(2)
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    counter.most_commomn(2)
NameError: name 'counter' is not defined
>>> counter.most_common(2)
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    counter.most_common(2)
NameError: name 'counter' is not defined
>>> Counter.most_common(2)
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    Counter.most_common(2)
  File "C:\Users\Srushti\AppData\Local\Programs\Python\Python37\lib\collections\__init__.py", line 583, in most_common
    return sorted(self.items(), key=_itemgetter(1), reverse=True)
AttributeError: 'int' object has no attribute 'items'
>>> 
