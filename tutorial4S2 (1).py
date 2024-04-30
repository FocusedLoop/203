#!/usr/bin/env python
"""
Tutorial 4 Functions
@Author: Alan
@Date: 2024 Semester 1
"""

# Import Libraries 
import math

# (a) Write a Python expression for the set of all divisors of 12.

# Method 0 - Using hardcoding ... NOT GREAT

# Method 1 - Using For Loop

# Method 2 - Intermediate

# Method 3 - Using Set Comprehension



# (b) Write a Python expression for the set of positive divisors of 72 that are not squares.

# Method 1 - Using For Loop

# Method 2 - Intermediate

# Method 3 - Using Set Comprehension



# c) Write a Python expression for the set of positive integers less than 65 that are multiples of 5 or 7.

# Method 1 - Using For Loop

# Method 2 - Intermediate

# Method 3 - Using Set Comprehension



# d) Suppose that variables S, T, U are sets. Write a Python expression for the things that S has in common with T but not with U.

def setCommonsAndDifference(S: set, T: set, U: set) -> set:
    """
    This function takes sets S, T, U and returns things that S has in common with T but not with U.
    
    :param set S: A set S
    :param set T: A set T
    :param set U: A set U
    :return: A set of that S is common with T but not U
    """

    return None


# (e) Define a function that takes a number x and returns a set containing all non-negative integers
# less than 100 that are divisible by x

def integersLessThanHundred(x: int) -> set:
    """
    This function takes a number x and returns a set containing all non-negative integers less than 100 that are divisible by x
    
    :param int x: An integer x
    :return: A set of non negative integers divisble by x
    """

    return None


# (f) Define a function that implements complements by taking a set S and a universe U and returning the complement of S in U

def complement(S: set,U: set) -> set:
    """
    This function takes set S and a universe U and returning the complement of S in U.
    
    :param Set S: A Set S
    :param Set U: A set U
    :return: Completent of S from U (set)
    """
    return None
