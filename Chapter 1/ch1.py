Python 3.7.2 (tags/v3.7.2:9a3ffc0492, Dec 23 2018, 23:09:28) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import numpy
>>> from matplotlib import pyplot as plt
>>> plt.hist([1,5,5,7,7,9])
(array([1., 0., 0., 0., 0., 2., 0., 2., 0., 1.]), array([1. , 1.8, 2.6, 3.4, 4.2, 5. , 5.8, 6.6, 7.4, 8.2, 9. ]), <a list of 10 Patch objects>)
>>> plt.show()
>>> from nltk.tokenize import word_tokenize
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    from nltk.tokenize import word_tokenize
ModuleNotFoundError: No module named 'nltk'
>>> from nltk.tokenize import word_tokenize
>>> words=word_tokenize("This is a pretty cool tool!")
>>> word_lengths=[len(w)for w in words]
>>> plt.hist(words.lengths)
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    plt.hist(words.lengths)
AttributeError: 'list' object has no attribute 'lengths'
>>> plt.hist(words_lengths)
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    plt.hist(words_lengths)
NameError: name 'words_lengths' is not defined
>>> plt.hist(word_lengths)
(array([2., 0., 1., 0., 0., 0., 3., 0., 0., 1.]), array([1. , 1.5, 2. , 2.5, 3. , 3.5, 4. , 4.5, 5. , 5.5, 6. ]), <a list of 10 Patch objects>)
>>> plt.show()
>>> 
