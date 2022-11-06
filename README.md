# Introduction to Python

## What did i learn

## learning a new languages 

- how is different is the syntax

## Python syntax (difference in 

### Variable declaration

```
answer = get_string("What's your name? ")

```

- Don't need to specify the type 
- you don't need to use ;

### print

We can also write: with a format string
```
print("hello, " + answer)
print(f"hello, {answer}"
```
diferences:
- we can concatenate two string together with +
- you don't /n because we get it for free if print

### incremention

- there is no ++ in python
- so you have to use <code>counter += 1</code>


## Conditionals

```
Conditionals look like:

if x < y:
    print("x is less than y")
elif x > y:
    print("x is greater than y")
else:
    print("x is equal to y")

```

differences:

- no {} or ()
- Uses :
- identention is important
- else if is now elif

```
while True:
    print("meow")

```

- True is capitalized
- no more ()


for loop, where we can do something for each value in a list:
```
for i in [0, 1, 2]:
    print("hello, world")
  ----------------  
for i in range(3):
    print("hello, world")
```

## types

In Python, there are built-in data types similar to those in C:

 - bool, True or False
 - float, real numbers
 - int, integers which can grow as needed
 - str, strings

Other types in Python include:

 - range, sequence of numbers
 -  list, sequence of mutable values, or values we can change
 -  tuple, sequence of immutable values
 -  dict, dictionaries, collection of key/value pairs, like a hash table
 -  set, collection of unique values, or values without duplicates

Integer overflow is no longer going to be an issue
Floating point imprecision.... oh well there are libraries ¯\\_(ツ)_/¯

### Importing
```
import cs50

from cs50 import get_float
```

## Libraries

There is no compilation per say, you jump right into the execution
<code>python hello.py</code>

Python is also the name of a program whose interpret the language, that is why we say python is an interpreted languange not compiled

Even though it's much faster for us to write, we aren’t able to fully optimize our code by way of managing memory and implementing all of the details ourselves.

 If you have a very large data set, you might want to optimize your code to be as fast and performant as it can be, especially if you're running that code again and again. Maybe you're a company like Google. People are searching a huge database all the time. You really want to squeeze every bit of performance as you can out of the computer. 
 
is if you will. If you have a very large data set, you might want to optimize your code to be as fast and performant as it can be, especially if you're running that code again and again. Maybe you're a company like Google. People are searching a huge database all the time. You really want to squeeze every bit of performance as you can out of the computer. 

You might want to have someone smart take a language like C and write it at a very low level. It's going to be painful. They're going to have bugs. They're going to have to deal with memory management and the like. But if and when it works correctly, it's going to be much faster,
