# Arithmetic Operators
num1 = 25
num2 = 6

addition = num1 + num2
difference = num1 - num2
product = num1 * num2
division_float = num1 / num2
division_floor = num1 // num2

print("Addition:", addition)
print("Difference:", difference)
print("Product:", product)
print("Division Floor:", division_floor)
print("Division Float:", division_float)


print("===================================================================================================")
# Assignment Operators
num1 = 25
num2 = 6

less_than = num1 < num2
greater_than = num1 > num2
less_than_or_equal = num1 <= num2
greater_than_or_equal = num1 >= num2
equal = num1 == num2
not_equal = num1 != num2

print("num1 < num2:", less_than)
print("num1 > num2:", greater_than)
print("num1 <= num2:", less_than_or_equal)
print("num1 >= num2:", greater_than_or_equal)
print("num1 == num2:", equal)
print("num1 != num2:", not_equal)


print("===================================================================================================")
# Relational Operators
x = True
y = False

and_result = x and y
or_result = x or y
not_result_x = not x
not_result_y = not y

print("x and y:", and_result)
print("x or y:", or_result)
print("not x:", not_result_x)
print("not y:", not_result_y)


print("===================================================================================================")
# Logical Operators
num3 = 20

num3 += 8
num3 -= 5
num3 *= 11
num3 /= 9

print("Final total:", num3)


print("===================================================================================================")
# Identity Operators
list1 = [11, 24, 43, 74, 45]

a = list1
b = [11, 24, 43, 74, 45]

is_same_object = a is list1
is_not_same_object = b is not list1

# Membership operators
element_in_list = 43 in list1
element_not_in_list = 77 not in list1

print("a is list1:", is_same_object)
print("b is not list1:", is_not_same_object)
print("43 in list1:", element_in_list)
print("77 not in list1:", element_not_in_list)