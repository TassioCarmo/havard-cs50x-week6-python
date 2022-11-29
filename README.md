# Introduction to Python

## What did i learn?

## learning a new languages 

- the goal, when playing around with some new language and learning it, is not to learn it exhaustively. Just like in English or any human language, there's always going to be vocab words you don't know, ways of presenting the same information in some language.

- how is different is the syntax?

## Python syntax 

**INDENT YOUR CODE**

### Variable declaration

```
answer = get_string("What's your name? ")

```

- Don't need to specify the type 
- you don't need to use ;

## print

We can also write: with a format string
```
print("hello, " + answer)
print(f"hello, {answer}"
```
diferences:
- we can concatenate two string together with +
- you don't /n because we get it for free if print

## incremention

- there is no syntax sugar "++" in python.
- so you have to use <code>counter += 1</code>


## Conditionals

```
Conditionals look like:

if x < y:
    print("x is less than y")
elif not x == y:
    print("x is greater than y")
else:
    print("x is equal to y")

```

## Differences:

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

- Python is also the name of a program whose interpret the language, that is why we say python is an interpreted languange not compiled

- There is no compilation per say, you jump right into the execution
<code>python hello.py</code>

- Even though it's much faster for us to write, we aren’t able to fully optimize our code by way of managing memory and implementing all of the details ourselves.

 
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
We can compare strings directly with <code>==</code>, and we can use or and and in our Boolean expressions.

### truncation
is no longer an issue in python
(We can get the same behavior as in C, truncation, with the // operator, like z = x // y.)

### Str

- There is no data type for individual characters aka <code>char</code> only strs

- we can use "" or '' as long as we are consistent

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

Strings have functions built into them, because strings are now what we call objects

<strong>And we're going to keep seeing examples of this dot operator. They are also immutable,  Immutable means they cannot be changed, which means, unlike C, you can't go into a string and change its individual characters. You can make a copy of the string that makes a change, but you can't change the original string itself.</strong>

we have define a main function first:
```
def main():
    for i in range(3):
        meow()

def meow():
    print("meow")

main()

```

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
- if you return from a function, you're done, you're going to exit from right at that point


 - the moment you declare a variable in python is avaible everywhere even if it's nested in a bunch of functions

in Python, you have, not only positional arguments, where you just separate them by commas, to give one or two or three or more arguments. There are also named arguments, which looks weird but is helpful for reasons like this.

same line:
```
for i in range(4):
    print("?", end="")
print()

# you can also print multiple times like this

print("#" *3);
```

## Lists, strings
```
from cs50 import get_int

scores = []
for i in range(3):
    score = get_int("Score: ")
    scores.append(score)

  
average = sum(scores) / len(scores)
print(f"Average: {average}")
```


We can also concacatenate lists in python


 in Python, there aren't technically characters individually. There's only strings, anyway. So I might as well do them all at once. So if I rerun the code now, Python of Uppercase.py.
 
 <code>after = before.upper()</code>


## Command-line arguments, exit codes

In python you have to import command args from the sys library

<code>from sys import argv</code>

```

if len(argv) == 2:
    print(f"hello, {argv[1]}")
else:
    print("hello, world")
```

 Python is not included in argv, whereas in C, dot slash whatever was the first thing. If the analog in Python is that the name of your Python program is the first thing, in bracket 0, which is why David is in bracket 1, the word Python does not appear in the argv list


Slicing a list in python which means starting from somewhere beisdes 0

```
for arg in argv[1:]:    #or argv[:-1] for the end of the list
    print(arg)
```

## Search

in python Just ask that question. No need for a loop or anything like that. If 0 is in the numbers, go ahead and print out found. And then let's just exit successfully, with 0, else, if we get down here, let's just say print not found. And then we'll CIS exit with 1. 

```
import sys

numbers = [4, 6, 8, 2, 7, 5, 0]

if 0 in numbers:
    print("Found")
    sys.exit(0)

print("Not found")
sys.exit(1)

```

A list of strings, too, can be searched with:
```
import sys

names = ["Bill", "Charlie", "Fred", "George", "Ginny", "Percy", "Ron"]

if "Ron" in names:
    print("Found")
    sys.exit(0)

print("Not found")
sys.exit(1)
```
If we have a dictionary, a set of key-value pairs, we can also check for a particular key, and look at the value stored for it:
```
from cs50 import get_string

people = {
    "Carter": "+1-617-495-1000",
    "David": "+1-949-468-2750"
}

name = get_string("Name: ")
if name in people:
    number = people[name]
    print(f"Number: {number}")
```

## Files

open a CSV file, with comma-separated values:
```
import csv
from cs50 import get_string

file = open("phonebook.csv", "a")

name = get_string("Name: ")
number = get_string("Number: ")

writer = csv.writer(file)
writer.writerow([name, number])

file.close()

```

with keyword, which will close the file for us after we’re finished:

```
with open("phonebook.csv", "a") as file:
    writer = csv.writer(file)
    writer.writerow((name, number))
```


Python is so popular for data science and analytics,because is that it's  really easy to manipulate data, and run analytics.

Reading a file and printing the houses
```
import csv

houses = {
    "Gryffindor": 0,
    "Hufflepuff": 0,
    "Ravenclaw": 0,
    "Slytherin": 0
}

with open("hogwarts.csv", "r") as file:
    reader = csv.reader(file)
    next(reader)
    for row in reader:
        house = row[1]
        houses[house] += 1

for house in houses:
    count = houses[house]
    print(f"{house}: {count}")
----------------------------------------
#improving
with open("hogwarts.csv", "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        house = row["House"]
        houses[house] += 1

```

### fun libraries

More libraries

 On our own Mac or PC, we can use another library to convert text to speech (since VS Code in the cloud doesn’t support audio):

    import pyttsx3

    engine = pyttsx3.init()
    engine.say("hello, world")
    engine.runAndWait()

   By reading the documentation, we can use a Python library called pyttsx3 to play some string as audio.
    We can even pass in a format string with engine.say(f"hello, {name}") to say some input.
  We can use another library, face_recognition, to find faces in images with detect.py:

    # Find faces in picture
    # https://github.com/ageitgey/face_recognition/blob/master/examples/find_faces_in_picture.py
      
    from PIL import Image
    import face_recognition

    # Load the jpg file into a numpy array
    image = face_recognition.load_image_file("office.jpg")

    # Find all the faces in the image using the default HOG-based model.
    # This method is fairly accurate, but not as accurate as the CNN model and not GPU accelerated.
    # See also: find_faces_in_picture_cnn.py
    face_locations = face_recognition.face_locations(image)
      
    for face_location in face_locations:

        # Print the location of each face in this image
        top, right, bottom, left = face_location

        # You can access the actual face itself like this:
        face_image = image[top:bottom, left:right]
        pil_image = Image.fromarray(face_image)
        pil_image.show()

   In recognize.py, we can see a program that finds a match for a particular face.
   In listen0.py, we can respond to input from the user:

    # Recognizes a greeting
      
    # Get input
    words = input("Say something!\n").lower()
      
    # Respond to speech
    if "hello" in words:
        print("Hello to you too!")
    elif "how are you" in words:
        print("I am well, thanks!")
    elif "goodbye" in words:
        print("Goodbye to you too!")
    else:
        print("Huh?")

   We can recognize audio input from a microphone and respond with listen2.py:

    # Responds to a greeting
    # https://pypi.org/project/SpeechRecognition/
      
    import speech_recognition
      
    # Obtain audio from the microphone
    recognizer = speech_recognition.Recognizer()
    with speech_recognition.Microphone() as source:
        print("Say something:")
        audio = recognizer.listen(source)
      
    # Recognize speech using Google Speech Recognition
    words = recognizer.recognize_google(audio)
      
    # Respond to speech
    if "hello" in words:
        print("Hello to you too!")
    elif "how are you" in words:
        print("I am well, thanks!")
    elif "goodbye" in words:
        print("Goodbye to you too!")
    else:
        print("Huh?")

   We can even add more logic to listen for a name:

    # Responds to a name
    # https://pypi.org/project/SpeechRecognition/
      
    import re
    import speech_recognition
      
    # Obtain audio from the microphone
    recognizer = speech_recognition.Recognizer()
    with speech_recognition.Microphone() as source:
        print("Say something:")
        audio = recognizer.listen(source)
      
    # Recognize speech using Google Speech Recognition
    words = recognizer.recognize_google(audio)
      
    # Respond to speech
    matches = re.search("my name is (.*)", words)
    if matches:
        print(f"Hey, {matches[1]}.")
    else:
        print("Hey, you.")




Add to the end of the list
```
nums.append(5)
nums.insert(4, 5) (position 4 add 5)

nums[len(nums):] = [5] # attach a list the the end of another one
```
# Tuples 
are ordered, immutable sets of data; they are great for associating collections of data, sort of like a structin C, but where those values are unlikely to change.

```
presidents = [
("George Washington", 1789),
("John Adams", 1797),
("Thomas Jefferson", 1801),
("James Madison", 1809)
]

This list is iterableas well:
presidents = [
("George Washington", 1789),
("John Adams", 1797),
("Thomas Jefferson", 1801),
("James Madison", 1809)
]

#for prez, year in presidents:
print("In {1}, {0} took office".format(prez, year))
```

# Objects

First parameter is always self

Tnotion of methods, properties, and how we work with them is going to be really important to sort of synthesize.

```
class Student():
    def__init__(self, name, id):
        self.name = name
        self.id = id
    defchangeID(self, id):
        self.id = id
    defprint(self):
        print("{} –{}".format(self.name, self.id))
```
```
# file handling
  
# 1) without using with statement
file = open('file_path', 'w')
file.write('hello world !')
file.close()
  
# 2) without using with statement
file = open('file_path', 'w')
try:
    file.write('hello world')
finally:
    file.close()

 
# using with statement
with open('file_path', 'w') as file:
    file.write('hello world !')
```

### Other

A restaurant might place food orders in multiple shelves, with areas each labeled by the first letter of the customer’s name. This is an example of a dictionary, where we can map keys to values.

# Declaring lists/array
```
nums= []
nums= [1, 2, 3, 4]
nums= [x for x in range(500)]
```


 - If you have a very large data set, you might want to optimize your code to be as fast and performant as it can be, especially if you're running that code again and again. Maybe you're a company like Google. People are searching a huge database all the time. You really want to squeeze every bit of performance as you can out of the computer. 
 
- You might want to have someone smart take a language like C and write it at a very low level. It's going to be painful. They're going to have bugs. They're going to have to deal with memory management and the like. But if and when it works correctly, it's going to be much faster,

- we can cache, or save, the interpreted version of our Python program, so it runs faster after the first time. And Python is actually partially compiled too, into an intermediate step called bytecode, which is then run by the interpreter.
 
- the whole point of using newer, modern languages is to use abstractions that other people have created for you.

- When learning a new language for the first time. You're not going to have heard all of the answers before. Just apply some logic, as to, like, all right, what could explain this symptom. Start to infer how the language does or doesn't worry

