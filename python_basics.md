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
###### NOTE: this is only a super brief outline on string objects. There is a lot more about how Python interacts and uses string objects. Similar this guide is primarily on data analysis (excluding text analysis), we will not discuss strings much further. For more information regarding string objects in Python, visit https://docs.python.org/3/library/stdtypes.html#str

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
###### Note: Python 3.x refers to dictionary items in a different way when compared to Python 2.x
###### Note: that values can be any type of basic object, or even container objects

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
There are special "escape" characters that Python uses to do different text editing functions. We will talk about two of them here. First there is tab (designated by \t) and enter/new line (designated \n). This allows tabs and new lines to be created when printing strings. We can see what happens when we run the following line
```python
print('\tHello'+'\nworld!')
```
### Mathematical Functions on strings
We can also perform some basic mathematical functions on strings, using the symbols from earlier. First we can 'add' or concatenate string objects together using the plus sign. Note that this only works when all objects are string objects
```python
print('Nine'+' = '+str(9)) #add to a string
```
We can also use multiplication to repeat a string multiple times
```python
print('repeat '*5)
```
Again, these are just the bare minimum regarding string functionality. If you want to learn more, I suggest looking at the online documentation for Python or looking through StackOverflow

## Loops, if-then, functions
Now that we have some basics, let's build on what we have learned. 
### Loops
First we will discuss for loops. For loops is a process that is repeated until the end of an object is reached. Let's look at the following example
```python
for i in range(5):
    print(i)
 

```
This for loop will print the current loop number until the end is reached. Remember that Python begins indexing with zero. As a result, our loop will count from 0 to 4, rather than 1 to 5. Also note that Python loops are "smart" in that they will add an iteration once the end of the loop statement is reached. This means we don't have to create a counter

Now let's discuss the syntax of a loop a little more. First you will see we begin our for loop with a 'for' statment. In this statement, we specify the variable that will serve as the current count. In this example, we are using 'i' as the variable name. Next we use the Python key-word 'in' do designate that where 'i' comes from. Next is the built-in function 'range()'. Range outputs the range between number specified. When only one number is included, it counts from zero to that number, not inclusive. Finally, we end our loop with a colon.
The next line, which is nested within the loop, is indicated as part of the loop by an indent. Note that the indent **must** be 4 spaces. The default on most computer text editors is 8 spaces. This is why I recommend using an IDE built for Python, since most default to this spacing. Once we have all the statements written inside our loop, we close the loop by putting two blank lines are the loop
For loops are not the only option, there are others. Let's just look at another quick example. Below is a 'while' loop. It repeats the process until the while criteria is met
```python
i = 0
while i < 5:
    print(i)
    i += 1
```
To make sure we do not get stuck in an infinite loop, this time we added the statement 'i += 1'. This statement adds 1 to the current count after each loop through the while statement. The statement 'i += 1' is equivalent to 'i = i + 1', but the first is just a shorthand option available in Python. It is also supported for other basic mathematical operations

### If-then
If-thensare logical statements where an action is taken only if certain criteria are met. If-then statements have a similar syntax structure to loops. Let's look at the following example
```python
i = 4
if i == 5:
    print('The current number is five')
    print('Hello')
elif i == 4:
    print('The current number is four')
else:
    pass #ignores this line 
```
###### Note that to assess whether two items are equal, we use a **double** equal sign '==' 
In this example there are the 3 key-words for if-then statements. First, there is the intitial 'if' which is evaluated. This statement ends with a colon. All lines indented below this line will be executed when the if statement is True. 
Following the 'if' statement is an else if statement indicated by the Python key-word 'elif'. This statement is **only** checked when the prior 'if' statement is false. Depending on the complexity of the if-then statements and how many items have to be assessed, elif can increase efficiency rather than just have all if statements.
The last part of the if-then grouping is an 'else' statement. This statement only occurs if all the previous statements are evaluated to be False. Note that in our example, we use a Python key-word 'pass'. This indicates that Python should just skip or pass over this if-then statement if evaluated to be True. 

### Functions
Users can define functions for themselves. This makes a calculation easier to repeat for a number of variables. Let's take a sample user-defined function to calculate the Risk Ratio
```python
def risk_ratio(a,b,c,d):
    '''This function calculates the Risk Ratio. The inputs are 
    the numbers from a 2x2 table'''
    rr = (a/(a+b)) / (c/(c+d))
    print('The risk ratio is:')
    print(rr)


```
The first line 


### Altogether

## Python Packages Introduction
Now, it would be a lot of effort to write functions to do everything. For example, with the prior function, it doesn't calculate the variance, so we don't have confidence intervals. Now, we could write calculations into the function but this will quickly become tedious and exceedingly complicated for some functions. Luckily, there is a plethora of packages available that do a wide variety of calculations. We will now use a package I have been writing to help us with some calculations
###### Note: Packages need to be installed with 'pip' or some package manager before they can be used. Please see the introduction page for how to install packages with pip. 
Once we have the package installed with pip, we can open with 
```python
import zepid as ze 
```
Note that we use the 'as' statement. This allows us to shorten to name we use to call the package and the functions contained within it. Instead of writing 'zepid' each time we want to use a package function, we can now only write 'ze'
Now we can use the summary calculation function available in zepid to calculate our risk ratio and corresponding confidence intervals. First we call the package up by the abbreviated name, followed by a period. Following the period, we use the following items to specify the specific function we want to use 'RelRisk', which is contained in the 'summary' class
```python
ze.summary.RelRisk()
```
Which should output
```

```
There is a large variety of freely available packages. In the next sections, we will discuss some of the most common packages used for data management and data analysis. Additionally, most packages have extensive online documentation detailing all the functions available

# Summary
So in this part of the tutorial we have went over some of the basic functionality of Python. This section is just meant to be an introduction to the very basics of Python. There is a lot more to learn, but this serves as a good introduction to the elements important for data analysis. In the next sections, we will cover more of data analysis specifics
