# Packages for Data Manipulation
Now that we have a handle on the basics of Python 3.x syntax, let's start doing some data manipulation. The two most important packages we will be using are NumPy and Pandas. NumPy contains loads of useful functions and improved storage objects (think improved lists). Pandas is built on top of NumPy and allows traditional data storage, display, and tools. Like all of our code, we begin with importing the relevant packages
```python
import numpy as np
import pandas as pd
```
## Loading data
Let's load the CSV file contained within the guide's documents. First we specify a variable indicating the filepath of the CSV file. This needs to be specifically changed for your computer
```python
filepath = 'C:/file/path/to/the/folder/data.csv'
```
###### Note the filepath provided is Windows specific. Mac filepaths are different
Now we can load the dataframe as a pandas dataframe object. To do this, we use a function that converts CSV files into a file recognized by pandas. We use the following code
```python
df = pd.read_csv(filepath)
```
Fantastic! Now that we have our dataframe loaded, let's take a look at some functions to give us a feel for our data. First, we can use info to give some basic summary information regarding the dataset (number of observations / columns / variable types). Next, we can use 'head' to print the first rows of observations (tail is the counterpart, printing the last rows). Lastly, we can use describe the generate basic summary measures for numeric variables
```python
df.info()
df.head(5) #first 5 observations/rows
df.tail(10) #last 10 observations/rows
df.describe()
```
We can also call functions to produce each part of the describe function. We would use the following code
```python
df.mean()




#
#
```
## Missing Data
Before we go any further, let's discuss how Python does missing data. Missing data is not inherently built into Python. Missing data is a special object available through the NumPy package. To produce a missing data object, we use the following code
```python
np.nan
```
Which is our missing data object. Now np.nan has some features that are not readily apparent. This can cause issues for beginners, so let's discuss the two biggest ones I have encountered. 
### np.nan does not equal np.nan
This is what I believe is the most confusing to NumPy newcomers, and that is that NumPy's nan is /*never*/ equal to itself. For example we run the following lines
```python
np.nan != np.nan
np.nan == np.nan
```
Both with evaluate to be False. This is counterintuitive and important to note. How we deal with this in data manipulation is later discussed, but in short, we use special functions to evaluate whether something is equal to np.nan
### Columns with np.nan must be floats
This is important when trying to convert data types across columns. Basically, if a column has missing values, then it must be stored as a float. This doesn't often become an issue but it is worth noting. I only have come across this issue while creating dummy variables (generate column labels based on the floats rather than the integers). We will discuss the implications of this later
## Missing Data within our dataframe
Looking back at our output from df.info(), we can see that the column labeled ____________________ has some missing observations within this column

