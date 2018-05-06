#########################################################################################
# Section 1: Python Basics
#
# Created by: Paul Zivich                                       Last edit: May 6, 2018
#########################################################################################

#Comments
print('Hello World') #Everything afterwards is considered a comment

#Object types
    #Basic Data Types
x = 2 #integer
print(type(x))
int(1.9)

y = 0.3 #float
print(type(y))
float(4)

q = True #Boolean
print(type(q))
bool(1) #Note that 1 is True while 0 is False

z = 'two' #string
print(type(z))

    #Basic Container Types
l = ['first',1,1,2,3,4,5,8,8,'last'] #lists
print(type(l))
print(l)
print(l[0])
print(l[-1])
l.append('add to list')
print(l)
l[1] = 'second'
print(l)

s = set(l) #sets
print(s)

t = (1,23,45,678) #tuples
print(t)
t += (1024,)
print(t)

d = {'0':0,'1':1,'2':2} #dictionary
d['Three'] = 3
print(d)
print(d.keys())
print(d.values())

#Mathematical functions
print(5+8) #addition
print(5-8) #subtraction
print(5*8) #multiplication
print(5/8) #division
print(5**8) #exponential
print(5//8) #returns only integer for division
print(5%8) #outputs remainder from division

import math
print(math.sqrt(x)) #square root
print(math.log(x)) #natural log 
print(math.exp(x)) #exponentiate
print(math.factorial(x)) #factorial

#String functions
print('\tHello'+'\nworld!')
print('Nine'+' = '+str(9)) #add to a string
print('repeat '*5)

#Loops, if-then, functions
for i in range(5): #for loop
    print(i)


i = 0
while i < 5: #while loop
    print(i)
    i += 1


i = 4
if i == 5: #if, then statements
    print('The current number is five')
    print('Hello')
elif i == 4:
    print('The current number is four')
else:
    pass #ignores this line 


def risk_ratio(a,b,c,d,risk=True): #user-defined function
    '''This function calculates the Risk Ratio. The inputs are 
    the numbers from a 2x2 table'''
    rr = (a/(a+b)) / (c/(c+d))
    if risk == True:
        print('The risk ratio is:')
        return rr
    else:
        print('not a RR')


risk_ratio(15,24,52,64)
risk_ratio(15,24,52,64,risk=False)

def count_to_x(x): #loops, if-then, and defined functions all together
    '''This functions counts to x. It only accepts non-negative, integers.
    
    Inputs:
    x - number to count to'''
    if ((x < 0) | (type(x) != int)): #Note that | means 'or' and & means 'and'
        print('x must be a positive integer')
    else:
        for i in range(x):
            print(i)


count_to_x(5)
count_to_x(-5)

#Python Packages Introduction
import zepid as ze 

help(ze.calc.rr)
ze.calc.rr(15,24,52,64)