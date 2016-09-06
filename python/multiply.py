Python 2.7.12 (v2.7.12:d33e0cf91556, Jun 27 2016, 15:19:22) [MSC v.1500 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> a=[2,4,10,16]
>>> def multiply(arr):
	for i in range(len(arr)):
		arr[i] = arr[i] * 5
	return arr
b = multiply(a)
SyntaxError: invalid syntax
>>> 
=============================== RESTART: Shell ===============================
>>> a = [2,4,10,16]
>>> def multiply(arr):
	for i in range(len(arr)):
		arr[i] = arr[i] * 5
	return arr

>>> b = multiply(a)
>>> print b
[10, 20, 50, 80]
>>> 
