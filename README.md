# Python-for-Epidemiologists
[![Join the chat at https://gitter.im/zEpid/community](https://badges.gitter.im/zEpid/community.svg)](https://gitter.im/zEpid/community?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge)
[![DOI](https://www.zenodo.org/badge/113911867.svg)](https://www.zenodo.org/badge/latestdoi/113911867)

This repository is an introduction to epidemiology analyses in Python. Additionally, the tutorials for my library 
*zEpid* are hosted here. For more information on *zEpid*, see [GitHub](https://github.com/pzivich/zEpid) or 
[ReadTheDocs](https://zepid.readthedocs.io/en/latest/). 

The directory of this guide is
1) Python Basics
2) Basics of pandas (data management library)
3) Epidemiology analyses in Python
   1) Basics
   2) Missing data
   3) Causal inference
      1) Time-fixed treatments
      2) Time-varying treatments
   4) Sensitivity analyses 

## Required packages for tutorial
To complete the tutorial, user must have the following packages installed: `numpy`, `pandas`, `zepid`, `matplotlib`, 
`statsmodels`, `lifelines`, and `sklearn`

## IDE (Integrated Development Environment)
No IDE is required to complete the tutorial. All files are available in `ipynb` also known as jupyter notebooks. Code 
can be either downloaded or copied from the notebooks. 

Here are some IDEs I have used in the past (and what I believe to be their advantages and disadvantages

**Rodeo**

This is the IDE I used for a long time. It is set up like RStudio

Advantages: 

Basically RStudio but for Python, decent interface, easy to run line-by-line, easy to visualize plots (although it 
encourage bad habits)

Disadvantages:

Does not have all the features of RStudio (will delete changes if closed without saving), sucks up a lot of memory, 
sometimes the auto-complete would stop working if I hit more than 300+ lines of code, the environment tab is not 
great (don't expect it to open anything like RStudio)

*Aside*: their website has great tutorials how to run some basic stuff in Python if you are new to analysis in Python
https://rodeo.yhat.com/

**jupyter notebooks**

Designed to be like a lab notebook, or like R markdown. Supports a pseudo-line-by-line concept 
Good for writing, since it allows for MarkDown. While I know a lot of people like jupyter, I only really use it for 
examples of code, not my personal programming. I never liked how it had to open via a Web Browser. I would rather have 
it be separate program. However, all guides were made using this IDE

**PyCharm**

This is the IDE I currently use

Advantages:

Easily set up virtual environments, interacts natively with Git, supports different file formats with plug-ins 
(e.g. .md), enforces certain coding conventions, better debug code features, organization of files under the project 
tab are convenient

Disadvantages:

Not great for running line-by-line code (it can do it, just not as elegantly), little more hardcore (I wouldn't really 
consider it a beginner's IDE. It requires some knowledge of set-up of Python)

**IDLE**

Ships with the basic Python 3.x installation. It is very basic and does not support line-by-line. Wouldn't recommend 
unless you are just starting with Python and don't want to commit to an IDE yet

**Spyder**

Ships with `conda`. Not bad but I didn't use it that much (I couldn't get the hang of it). Similarly it is an RStudio 
copy. Can't say too much since I haven't used it extensively

# Basic Introduction to Python
If you have never used Python before, I have created some introductory materials to Python and the data management 
library I use, `pandas`. These are basic guides, but they also point to other resources. Please **READ ALL OF THE BELOW 
BEFORE PROCEEDING**.

## Installing Python
To install, Python 3.x, we can download it directly from: https://www.python.org/downloads/ <br /> <br />
The installer provides an option to add Python3 to PATH, it is **highly recommended** you do this, since it allows you 
to avoid having to do it manually

Open Command Prompt / Terminal. When opened, type `python` and this should open Python in the same window. From here, 
you can quit by typing 'quit()' or closing the window. If this does NOT work, make sure your environmental variable 
was created properly

## Installing Python Packages
Packages are what stores Python functions that we will use. These packages are contributed by various members of the 
community (including me)) and there is a wide array. To be able to download packages, we need to make sure we have an 
environmental variable created for python. We will discuss how to install packages

Python 3.x conveniently comes with a package manager. Basically it stores all the packages and we can use it to 
download new ones or update already downloaded ones.

To download a new package: Open Command Prompt/Terminal and use the following code (we will be installing pandas)

```
pip install pandas
```

To update a Python package, type the following command into Command Prompt. For example, we will update our pandas package
```
pip install pandas --upgrade
```

That concludes the basics. Please review parts 1 and 2 of the tutorials next
