# CLASSES

> define new classes
 - act as template for creating new obj.
 Format:
```python 
class MyClassName:
```
```python 
class Flight:
  pass
```
> instance methods and self argument
- are functions which can be called on objects, or instances of our classes.
Ex:
```python 
class Flight:

  def number(self):
    return "SN060"
```
- instance methods must accept a reference to the actual 
instance on which the method was called as the
'first argument'. This argument is called 'self'.

> initializers
- _ _ init _ _() for initializing new obj. (dunder init)

```python 
class Flight:

  def __init__(self, number):
    self._number = number
  def number(self):
    return "SN060"
```
why _number?
- to avoid name clash with number()
- single leading underscore variables (_foo) are used in class 'internally'
- double leading (__foo) are used to avoid the variable getting overridden in subclasses. (see link for more defn: https://towardsdatascience.com/whats-the-meaning-of-single-and-double-underscores-in-python-3d27d57d6bd1)

> collaborating classes

> decomposing problems

> separating interface and implementation

> combine programming paradigms

> nominal and duck typing.

> inheritance