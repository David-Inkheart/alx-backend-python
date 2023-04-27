### [0. Basic annotations - add](./0-add.py)

Write a type-annotated function `add` that takes a float `a` and `a` float `b` as arguments and returns their sum as a float.
```
bob@dylan:~$ cat 0-main.py
#!/usr/bin/env python3
add = __import__('0-add').add

print(add(1.11, 2.22) == 1.11 + 2.22)
print(add.__annotations__)

bob@dylan:~$ ./0-main.py
True
{'a':  <class 'float'>, 'b': <class 'float'>, 'return': <class 'float'>}
```