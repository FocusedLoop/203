#!/usr/bin/env python
"""\
Tutorial 3 Functions
@Author: Alan
@Date: 2024 Semester 1
"""

# Import Libraries 
import math
from typing import Callable
### Recursion 

# Question 1b
# Python program that implemnets the function.

def f(n: int) -> int:
    """
    This function takes a number n and returns the evaluated function f(n), where:
    n=0, f(n) = 1
    n=1, f(n) = 1
    n>1, f(n) = f(n-1) - f(n-2)

    :param int n: n value for computation
    :return int value: Integer value f(n)
    """
    if (n == 0):
        value = 1

    elif (n == 1):
        value = 1
    
    elif (n >1):
        value = f(n-1) - f(n-2)
    
    return value


def f(n):
    if n==0: return 1
    if n==1: return 1
    return f(n-1) - f(n-2)

f(4)


### Python and Logic

# Question 1
#  Write a Python function that takes three arguments, x, y, z and returns the value of the formula
# (x → y) ∧ z

def f(x: bool, y: bool, z: bool) -> bool:
    """
    This function takes x, y, z and computes (x → y) ∧ z as the return value.
    
    :param bool x: A truth value x
    :param bool y: A truth value y
    :param bool z: A truth value z
    :return: A boolean that represents the evaluated logic of (x → y) ∧ z

    ((not x) or y) and z 

    """
    logicValue = ((not x) or y) and z
    return logicValue

f(True, False, True)

def f(x,y):
    return (x or y)

f(False, True)

# Question 2
# Write a function in Python that takes functi(x, y) (which implements a Boolean formula in two
# variables), and prints out whether f is a tautology, contradiction, satisfiable or contingent (note
# that f may be more than one these.)

def f(x: bool,y: bool) -> bool:
    """
    This function is the desired logic function f(x,y) that implements a Boolean formula in two variables.
    Example might be (((not x) or y)) which is maths notation for ( ¬x ∨ y ).

    :param bool x: A truth value x
    :param bool y: A truth value y
    :param bool z: A truth value z
    :return: A boolean that computes your desired value.
    """    
    logicValue = (x or y)
    return logicValue


def classify(f: Callable[[bool,bool],bool]) -> None:
    """
    This function prints out if the given logic function f(x,y) is a tautology, contradiction, satisfiable or contingent.

    :param function f: A custom logic function that has two inputs (x,y) and returns a boolean value.

    :return: This function does not return anything. Instead it just prints in the console.
    """    
    # Creating flags
    tautology = True
    contradiction = True

    # Loop through all possible combinations of x and y
    for x in {True, False}:
        for y in {True, False}:
            if f(x,y):
                contradiction = False
            else:
                tautology = False

    if contradiction:
        print('contradiction')
    elif tautology:
        print('tautology')
        print('satisfiable')
    else:
        print('contingent')
        print('satisfiable')

    return None

def f(x,y):
    return (x or y)

classify(f)


# Question 3
# Write a function in Python that takes two functions, f(x, y) and g(x, y) (which both implement
# Boolean formulas in two variables) and prints out whether they are logically equivalent or not.


def testLE(f: Callable[[bool,bool],bool], g: Callable[[bool,bool],bool]) -> None:
    """
    This function takes two functions, f(x, y) and g(x, y) (which both implement Boolean formulas in two variables) and prints out whether they are logically equivalent or not.

    :param function f: A custom logic function that has two inputs (x,y) and returns a boolean value.
    :param function g: A custom logic function that has two inputs (x,y) and returns a boolean value.

    :return: This function does not return anything. Instead it just prints in the console.
    """    
    for x in {True, False}:
        for y in {True, False}:
            if f(x,y) != g(x,y):
                print('Not logically equivalent')
                return
            
    print('Logically equivalent')
    return None

def f(x,y):
    return (x or y)

def g(x,y):
    return (not((not x) and (not y)))

testLE(f,g)


