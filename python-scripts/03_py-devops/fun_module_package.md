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


### Packages

A package is a collection of modules organized in directories. Packages help you organize related modules into a hierarchy. They contain a special file named `__init__.py`, which indicates that the directory should be treated as a package.

**Example:**

Suppose you have a package structure as follows:

```
my_package/
    __init__.py
    module1.py
    module2.py
```

I can use modules from this package as follows:

```python
from my_package import module1

result = module1.function_from_module1()
```

In this example, `my_package` is a Python package containing modules `module1` and `module2`.


## 2. How to Import a Package

Importing a package or module in Python is done using the `import` statement. We can import the entire package, specific modules, or individual functions/variables from a module.

**Example:**

```python
# Import the entire module
import math

# Use functions/variables from the module
result = math.sqrt(16)
print(result)

# Import specific function/variable from a module
from math import pi
print(pi)
```

In this example, we import the `math` module and then use functions and variables from it. We can also import specific elements from modules using the `from module import element` syntax.

