### Integers
num = 123
print(num)


num = 100_000_000 # possible to divide
print(num)

### Function type

num = 123
print(type(num))

x = 1.5e2 ## exponential representation

## conversion OK
num = 1250.2
num = int(num)
num = float(num)

# complex numbers
# decimal + fractions modules -->

print(100%1)


#### 1. Euclidean distance ( OK )
x, y = 0, 0
## mutable VS immutable
y = []
x = y
x.append(1)
print(x)
print(y)

#multiple ccomparisson
x = 5
print( 1 < x < 10)

#lazy  logic
# check leap year
year = 1980
# rule: if year is divisible by 4 and not divisible by 100, or divisible by 400
print("-----------------------------")
print("check if year is leap")
is_leap = ( year%4 == 0 ) and ( year%100 > 0 ) or ( year%400 == 0 )
print( "{} is {}".format(year , "Yes" if is_leap else "No"))

import calendar
print(calendar.isleap(1980))

## строки ( str )
print("----------------------------------------")
print("Strings")
example_string = "курс  python на Coursera"
print(type(example_string))

## row string ( backslash is a backslash )
s = r"C:\\"
print(s)

# we can split long string with backslash
s = "abc " \
    "def"
print(s)

# string is immutable
print("string is immutable")
example_string = "Привет"
print(id(example_string))
example_string += ", Мир!"
print(id(example_string))

## substring
example_string = "Курс по Python"
print(example_string[10:15])
# step
print(example_string[::-1]) # sstep -1
# string methods

print("москва".capitalize())
print("3.14" in "3.14 is Pi")

for x in "москва":
    print(x)

# convertation
num_string = str(999.01)
print(type(num_string))
# formatted
# 1.
template = "%s - главное достоинство программиста. (%s)"
template % ("Лень", "Larry Wall")
# with format
# f strirng
subject = "оптимизация"
author = "Donald Knuth"
# python > 3.6
print(f"Преждевременная {subject} - корень всех зол. ({author})")
# modification
num = 2/3
print(f"{num:.3f}")

#byte strigns
#literal b
example_string = b"hello"
for element in example_string:
    print(element)

# codigng utf-8
example_string = "привет"
encoded_string = example_string.encode(encoding = "utf-8")
print(encoded_string)
print(type(encoded_string))


# object None
print("---------------------------")
answer = None
print(type(answer))

print("-----------------")
# if
# ternary operator
x = 1 if 1 == 1 else 0
print(x)
# for range object
for i in range(3):
    print(i)
# pass - nothing happes
# break - go out from cycle  ( for ; while )

### Easy program game.py



















