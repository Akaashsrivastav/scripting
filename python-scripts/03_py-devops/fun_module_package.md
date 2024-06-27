# Python Functions, Modules and Packages

## 1. Differences Between Functions, Modules, and Packages

### Functions

A function in Python is a block of code that performs a specific task. Functions are defined using the `def` keyword and can take inputs, called arguments. They are a way to encapsulate and reuse code.

**Example:**

```python
def hii(name):
    return f"Hello, {name}!"

message = hii("Akash")
print(message)
```

In this example, `hii` is a function that takes a `name` argument and returns a message.



### Modules

A module is a Python script containing Python code. It can define functions, classes, and variables that can be used in other Python scripts. Modules help organize and modularize our code, making it more maintainable.

**Example:**

Suppose I have a Python file named `ex_module.py`:

```python
# ex_module.py
def square(x):
    return x ** 2

pi = 3.14159265
```

I can use this module in another script:

```python
import ex_module

result = ex_module.square(5)
print(result)
print(ex_module.pi)
```
In this case, `ex_module` is a Python module containing the `square` function and a variable `pi`.
