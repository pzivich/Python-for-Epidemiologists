# Python Basics
Note that in Python everything after # in Python is designated as a comment
```python
print('Hello World') #Everything afterwards is considered a comment
```

## Object Types
Now that you have Python installed and chosen your IDE, let's discuss the basic object types in Python. There are a plethora of object types in Python. We will discuss the basic object types here.
### Basic Data Types
Below are some of the most common data types that you will see in Python. These are the fundamental building blocks of every higher level item. Note that print() is a basic function that prints the results & type() is a basic function that determines the type of object that is designated
1) Integer (numbers with no decimals)
```python
x = 2
print(type(x))
```
The above print() statement should produce the following output
```
<class 'int'>
```
We can transform other object types into integers by using the following built-in function
```python
int(1.9)
```

2) Float (numbers with decimals)
```python
y = 0.3
print(type(y))
```
The above print() statement should produce the following output
```
<class 'float'>
```
Similarly, we can transform other object types into integers by using the following built-in function
```python
float(4)
```

3) Boolean (True / False objects)
```python
q = True
print(type(q))
```
The above print() statement should produce the following output
```
<class 'bool'>
```
Again, we can transform other object types into Boolean objects
```python
bool(1) #Note that 1 is True while 0 is False
```

4) String (character/sentence format)
```python
z = 'two'
print(type(z))
```
The above print() statement should produce the following output
```
<class 'str'>
```
##### NOTE: this is only a super brief outline on string objects. There is a lot more about how Python interacts and uses string objects. Similar this guide is primarily on data analysis (excluding text analysis), we will not discuss strings much further. For more information regarding string objects in Python, visit https://docs.python.org/3/library/stdtypes.html#str

### Basic Container Types
Now that we have our basic data object types, let's store multiple objects together (in containers). There are multiple types of containers in Python. We will go over a few basic built-in ones here.
1) List
List is a basic container that a series of items. Note that the items contained in a list can be different basic object types. To demonstrate
```python
l = ['first',1,1,2,3,4,5,8,8,'last'] #list()
print(type(l))
print(l)
```
Now that we have a list object, let's pull out a single item from our list. To pull the first object,
```python
print(l[0])
```
Note: Python starts the indexing with 0, rather than 1. So, 0 gets the first object, 1 gets the second, and so on. This is **vitally important** to remember. The nice feature of this index ordering is that is is super easy to index the last object. To get the last object in the list, we simply do
```python
print(l[-1])
```
To add an item to our list, we use the following built-in function
```python
l.append('add to list')
```
Which appends the specified item to the end of the list
Let's imagine that instead of the second item in our list being an integer, we wanted to change it to a string object that says 'second'. We can use the following statement to edit items in our list
```python
l[1] = 'second'
```

2) Set
Set is similar to list, but the set only contains unique items. To see this we can convert our list into a set
```python
s = set(l)
print(s)
```
From the output, we can see that our new object only contains unique instances of each item. No longer are there repeated numbers
```
{'second', 2, 3, 4, 1, 5, 8, 'last', 'first'}
```

3) Tuple
Tuple are also similar to a list, but tuples are immutable. Basically, this means once an items is within a tuple, it cannot be changed
```python
t = (1,23,45,678) #tuple()
print(t)
```
So unlike our list, the number contained in our tuple are permanently affixed to be those values. Tuples are useful if you want to create a list but you don't want it to be accidentaly changed. To add an item to our tuple, we use a slightly different bit of code
```python
t += (1024,)
```

4) Dictionary
Last of the container objects we will discuss. Dictionary is slightly different from the prior containers because it contains two items technically. Dictionaries contain a key and a value. Each unique key corresponds to a value. So instead of index by an items position in a list, we can index by the keys in a dictionary
```python
d = {'0':0,'1':1,'2':2}
```
Each key-value pair is indicated by a colon. The item to the left of the colon is the key, and the value is to the right
To add a new item to our dictionary 
```python
d['Three'] = 3
```
Now we have a key (named 'Three') referring to an integer of 3
We can access the dictionary keys and values by using the following statements, respectively
```python
print(d.keys())
print(d.values())
```
##### Note: Python 3.x refers to dictionary items in a different way when compared to Python 2.x
##### Note: that values can be any type of basic object, or even container objects

From these humble objects, we can build a variety of things. For example, we could create a list of dictionaries that has values of sets of tuples

## Mathematical Functions
Now that we know our basic objects and container objects, let's start doing some basic math
For basic mathematical manipulations, we can use the following
```python
print(5+8) #addition
print(5-8) #subtraction
print(5*8) #multiplication
print(5/8) #division
print(5**8) #exponential
print(5//8) #returns only integer for division
print(5%8) #outputs remainder from division
```
To do more complicated mathematical functions, like exponentiating, we need to import the math package. The math package comes with base Python. To access the math package, we use the following code
```python
import math
```
Now we can call the math package and use some of its specified functions for calculations of interest
```python
print(math.sqrt(x)) #square root
print(math.log(x)) #natural log 
print(math.exp(x)) #exponentiate
print(math.factorial(x)) #factorial
```
Note that this is just a basic showcase of some common mathematical functions in the math package. This is not an exhaustive list

## String Functions
I know I said we were mostly skipping over string objects, but I just wanted to mention a few items about them here
### Special String Sequences
### Mathematical Functions on strings

## Loops, if-then, functions
Now that we have some basics, let's build on what we have learned. First we will discuss for loops. For loops is a process that is repeated until the end of an object is reached. Let's look at the following example
```python
```
