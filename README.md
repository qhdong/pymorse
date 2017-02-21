pymorse
=======

> **pymorse** 是一个使用 python 编写的支持 Unicode 的摩斯电码编码解码库，当然也支持中文。

[![PyPi Status](https://img.shields.io/pypi/v/pymorse2.svg)](https://pypi.python.org/pypi/pymorse2) [![PyPi Downloads](https://img.shields.io/pypi/dm/pymorse2.svg)](https://pypi.python.org/pypi/pymorse2)

Install
-------

```sh
pip install pymorse2
```

Usage
-----

```python
from pymorse import Morse

Morse.encode('你好')
Morse.decode('...././.-../.-../---')
```

Output
------

```py
In [7]: Morse.decode('...././.-../.-../---')
Out[7]: 'HELLO'

In [8]: Morse.encode('你好')
Out[8]: '-..----.--...../-.--..-.-----.-'
```
