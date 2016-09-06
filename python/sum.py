Python 2.7.12 (v2.7.12:d33e0cf91556, Jun 27 2016, 15:19:22) [MSC v.1500 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> a.append(i)

Traceback (most recent call last):
  File "<pyshell#0>", line 1, in <module>
    a.append(i)
NameError: name 'a' is not defined
>>> 
=============================== RESTART: Shell ===============================
>>> from array import *
>>> a = array('i',[1,2,5,10,255,3])
>>> for i in a:
	sum(a[i])

	

Traceback (most recent call last):
  File "<pyshell#5>", line 2, in <module>
    sum(a[i])
TypeError: 'int' object is not iterable
>>> from array import *
>>> a=array('i',[1,2,5,10,255,3])
>>> for i in a:
	b = sum(a):
		
SyntaxError: invalid syntax
>>> from array import *
>>> a = array ('i',[1,2,5,10,255,3])
>>> 
=============================== RESTART: Shell ===============================
>>> a=[1,2,5,10,255,3]
>>> sum(a)
276
>>> 
