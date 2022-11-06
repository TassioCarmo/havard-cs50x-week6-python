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
 
You might want to have someone smart take a language like C and write it at a very low level. It's going to be painful. They're going to have bugs. They're going to have to deal with memory management and the like. But if and when it works correctly, it's going to be much faster,

 we can cache, or save, the interpreted version of our Python program, so it runs faster after the first time. And Python is actually partially compiled too, into an intermediate step called bytecode, which is then run by the interpreter.
 
 the whole point of using newer, modern languages is to use abstractions that other people have created for you.
 
 ## Input, conditions
 
 There is no more Main method
 
 from cs50 import get_string

answer = get_string("What's your name? ")
print("hello, " + answer)

input for python treat its returns as string so if you want to get an interger for example you need to cast

### Exceptions

ValueError is a type of exception, or something that goes wrong when our code is running. In Python, we can try to do something, and detect if there is an exception:

```
try:
    x = int(input("x: "))
except ValueError:
    print("That is not an int!")
    exit()
try:
    y = int(input("y: "))
except ValueError:
    print("That is not an int!")
    exit()
print(x + y)
```
### comparison
We can compare strings directly with ==, and we can use or and and in our Boolean expressions.

### truncation
is no longer an issue in python
(We can get the same behavior as in C, truncation, with the // operator, like z = x // y.)

### Str
There is no data type for individual characters only strs

we can use "" or '' as long as we are consistent

```
check if our string is in a list, after converting it to lowercase first:

from cs50 import get_string

s = get_string("Do you agree? ")

s = s.lower()

if s in ["y", "yes"]:
    print("Agreed.")
elif s in ["n", "no"]:
    print("Not agreed.")

```
We can even just say <code>s = get_string("Do you agree? ").lower()</code> to convert the input to lowercase immediately, before we store it in s.

Not only do Strings have functions built into them, because strings are now what we call objects

And we're going to keep seeing examples of this dot operator. They are also immutable,  Immutable means they cannot be changed, which means, unlike C, you can't go into a string and change its individual characters. You can make a copy of the string that makes a change, but you can't change the original string itself. 

we have define a main function first:
```
def main():
    for i in range(3):
        meow()

def meow():
    print("meow")

main()

```

When learning a new language for the first time. You're not going to have heard all of the answers before. Just apply some logic, as to, like, all right, what could explain this symptom. Start to infer how the language does or doesn't worry

### Do while

```
while True:
    n = get_int("Height: ")
    if n > 0:
        break
```

```
from cs50 import get_int

def main():
    height = get_height()
    for i in range(height):
        print("#")

def get_height():
    while True:
        n = get_int("Height: ")
        if n > 0:
            break
    return n
    
    
    or
    
    def get_height():
    while True:
        n = get_int("Height: ")
        if n > 0:
        return

main()

```
 if you return from a function, you're done, you're going to exit from right at that point


the moment you declare a variable in python is avaible everywhere even if it's nested in a bunch of functions

in Python, you have, not only positional arguments, where you just separate them by commas, to give one or two or three or more arguments. There are also named arguments, which looks weird but is helpful for reasons like this. If you read the documentation, you will see that there is a named argument that Python accepts, called end. And if you set that equal to something, that will be used as the end of every line, instead of the default, which the documentation will also say is quote unquote backslash n. 


same line:
```
for i in range(4):
    print("?", end="")
print()

# you can also print multiple times like this

print("#" *3);
```
