# Packages for Data Manipulation
Now that we have a handle on the basics of Python 3.x syntax, let's start doing some data manipulation. The two most important packages we will be using are NumPy and Pandas. NumPy contains loads of useful functions and improved storage objects, like matrices (think improved lists) and functions that produce various calculations. Pandas is built on top of NumPy and allows traditional data storage, display, and tools. Like all of our code, we begin with importing the relevant packages
```python
import numpy as np
import pandas as pd
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
This is important when trying to convert data types across columns. Basically, if a column has missing values, then it must be stored as a float. This doesn't often become an issue but it is worth noting. I only have come across this issue while creating dummy variables (generate column labels based on the floats rather than the integers). We will discuss the implications of this later. 
Some of these topics might not make perfect sense yet. Review the rest of this tutorial and come back to this section, since the implications of how Python handles missing data is extremely important.

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

## Basics of Observing Data
```python
df.info()
df.head(5) #first 5 observations/rows
df.tail(10) #last 10 observations/rows
df.describe()
```
We can also call functions to produce each part of the describe function. We can also look only at selected columns. We would use the following code
```python
max(df.C)
max(df['C']) #this is equivalent to the above line, it just demonstrates another way to index data
min(df.C)
np.mean(df.C)
np.std(df.C)
np.median(df.C)
np.percentile(df.C,[25,75])
```
If you want to index multiple columns at once, you can create a list of column labels and use that to index the dataframe. See the following:
```python
df[['E','C']] #will return columns labeled E and C
```
We can also look at what data values/numerical categories and their respective counts
```python
df.E.value_counts()
```
To create a r-by-c table, we can use the following pandas function
```python
pd.crosstab(df['E'],df['D'])
```

## Basic Data Operation Procedures
### Indexing data
First, let's discuss how to index sections of data by their variable values. To select only rows where E is equal to 1. To do this, we can use the .loc function to index the data. We use it like such
```python
df.loc[df.E==1]
```
We can add multiple statements to evaulate using &(and) and |(or). For example, we can find only observations where E is equal to 1 and D is equal to 1.
```python
df.loc[((df.E==1)&(df.D==1))]
```
There are also other functions to index a dataframe (such as by row). We will let readers look up these other functions and how they index data (hint: Google "pandas loc")
### If-then Logic
Here we will discuss how to recode variables and use if-then logic operations on our dataframe. Note that we could write traditional if-then functions like discussed in part 1 of the tutorial, but these are extremely inefficient for pandas dataframe objects (long computation times). Built into pandas is a better way, so we will only be reviewing that method. I just wanted to mention that there are multiple ways to run if-then logic on a dataframe.
To start, let's divide our continuous variable (labeled 'C') into tertiles. First we need to figure out what the tertile values are. We then will set those values to be variables. We can use the following code to accomplish this
```python
lev1,lev2 = np.percentile(df.C,[1/3,2/3])
```
Now that we have our two levels, we need to use if-then logic to create a new variable we will call 'C_recode'. To do this, we use the .loc function with some additional arguments
```python
df.loc[df.C<=lev1,'C_recode'] = 0
df.loc[((df.C>lev1)&(df.C<=lev2)),'C_recode'] = 1
df.loc[df.C>lev2,'C_recode] = 2
```
Creates our new variable and assigns the corresponding values when the equation is evaluated to be True. 

## Generating Dummy Variables
Pandas also has a built-in function for creating dummy variables

## Merging dataframes
Now that we have our dummy variables generated, we need to add them back to our dataframe. We do this by merging our original dataframe with 

## Missing Data within our dataframe
Looking back at our output from df.info(), we can see that the column labeled 'M' has some missing observations within this column. Let's explore this column further
First, let's look at a feature of pd.crosstab() (remember that this generates a r-by-c table). If we use the help function and look at the document, we see that crosstab() has an option to not drop missing data (np.nan). Let's see what happens when we use this
```python
pd.crosstab(df.M,df.D,dropna=False)
```
Produces the following:
```
```
Let's check how this compares with a manual recoding of the missing variables. For this, we will use a special function called fillna(), which fills all missing values with a pre-specified value. We will fill any missing values with  99 and store it as a new dataframe labeled as dfna
```python
dfna = df.fillna(99)
pd.crosstab(dfna.M,dfna.D)
```
This result is not what is expected. This is due to the dropna=False option of pd.crosstab() not working as you would expect. As a result, when looking for missing data, it is recommended to create a copy of the pandas dataframe with the missing data filled in. This dataframe copy is only used for looking at missing data. 

## Coverting variable types

## Saving data
Now, unlike SAS, Python does not overwrite the original data when operations are conducted. The data is only stored locally till Python is closed. This is nice because we don't have to worry about accidentaly overwriting our dataset. However, it also means that we need to save a copy. Personally, I prefer to save my datafiles as CSVs. To do this, we use the following code
```python
df.to_csv('C:/file/path/to/data/new_data.csv')
```
There are a lot of other options. I recommend looking to the pandas documentation (available online) to see what other options are available.

## BONUS: Reading SAS files
There is also a package available to convert SAS7BDAT files into pandas dataframes. This is useful since it is a hassle converting SAS data files to CSV. We can convert SAS7BDAT datafiles by importing the following package and using the following code
```python
from sas7bdat import SAS7BDAT
filepath = 'C:/file/path/to/data.sas7bdat'
with SAS7BDAT(filepath) as f:
    df = f.to_data_frame()
```

# Conclusion
In this tutorial, we went over the basics of NumPy and Pandas. We discuss how to load data, perform basic observations on the data, manipulate variables, and save our data. This will prepare us for our next tutorial describing how to perform some statistical analyses and use some additional packages.
