# Conditional Statements in Python

Conditional statements are a fundamental part of programming that allow you to make decisions and execute different blocks of code based on certain conditions. In Python, we can use `if`, `elif` and `else` to create conditional statements.

## `if` Statement

The `if` statement is used to execute a block of code if a specified condition is `True`. If the condition is `False`, the code block is skipped.

```python
if condition:
    # Code to execute if the condition is True
```

- Example:

```python
x = 10
if x > 5:
    print("x is greater than 5")
```

## `elif` Statement

The `elif` statement allows us to check additional conditions if the previous `if` or `elif` conditions are `False`. We can have multiple `elif` statements after the initial `if` statement.

```python
if condition1:
    # Code to execute if condition1 is True
elif condition2:
    # Code to execute if condition2 is True
elif condition3:
    # Code to execute if condition3 is True
# ...
else:
    # Code to execute if none of the conditions are True
```