#!/usr/bin/env python
"""
Tutorial 6 Functions
@Author: Alan
@Date: 2024 Semester 1
"""

# Import Libraries 
import math
from typing import Callable


# 4. In Python, we might encode a relation over a set A as a Python set containing Python tuples, each
# of which is length 2 where the both elements are in A. For example, a relation might look like:
# R = { (1, 3), (2, 1), (3, 4) }
# Write a short Python function that takes a relation as above and returns the set A that R is over.
# Note that relations do not have to refer to every element of the set that they are over, (i.e. they
# do not need to have some (a, b) or (b, a) for every a ∈ A) so the set you return will just be the set
# of elements that R refers to.

def underlyingSet(R: set) -> set:
    """
    This function takes a relation R and returns the set A that R is over.

    :param set S: A set S
    :param predicate p: A function of p representing a predicate with input x (bool) and output boolean
    :return: A boolean that represents the evaluated logic of ∀x ∈ S p(x)
    """
    return None

# 5. Write a Python function which, given a relation in the format described in the previous question,
# and returns a pair (a, b) where a is True if the relation is symmetric and False otherwise, and b is
# True if the relation is anti-symmetric and False otherwise.

def antisymmetric(R: set) -> (bool,bool):
    """
    This function takes a relation R and returns a pair (a, b) where a is True if the relation is symmetric and False otherwise, and b is True if the relation is anti-symmetric and False otherwise.

    :param set R: A relation R
    :return: A pair (a, b) where a is True if the relation is symmetric and False otherwise, and b is True if the relation is anti-symmetric and False otherwise.
    """
    return None


# 6. Write a Python function which, given a relation in the format used in the previous questions,
# returns True if the relation is transitive, otherwise False.

def transitive(R: set) -> bool:
    """
    This function takes a relation R and returns True if the relation is transitive, otherwise False.

    :param set R: A relation R
    :return: A boolean that represents the evaluated logic of whether the relation is transitive
    """
    return None

# 2. Write a Python function which, given a relation in the format used in the previous section, a set
# A, a set B returns (a, b) where a is True if the relation is a function from A to B, otherwise False,
# and b is True if the relation is a function from A to B and has an inverse, otherwise False.

def checkFunction(R,a):
    return len({b for (a2,b) in R if a2 == a})

def isfunction(R: set, A: set,B set) -> (bool,bool):
    """
    This function takes a relation R, a set A, and a set B and returns (a, b) where a is True if the relation is a function from A to B, otherwise False, and b is True if the relation is a function from A to B and has an inverse, otherwise False.

    :param set R: A relation R
    :param set A: A set A
    :param set B: A set B
    :return: A pair (a, b) where a is True if the relation is a function from A to B, otherwise False, and b is True if the relation is a function from A to B and has an inverse, otherwise False.

    """

    return None

# 2. Write a collection of functions that implement a mini student database. The functions are:
# (a) createD() Return an empty database
# (b) addStudent(D, student): Add a student to the database
# (c) studentName(D, number): retrieve the students first and last name from the database by
# student number
# D is some data structure (you get to decide what it should be) representing the database. student
# is a data structure representing an individual student, and should include student number, first
# name and last name.
# To keep things simple, your functions are allowed to have undefined behaviour when given inappropriate inputs. You can assume, for example, that a student number querried will always be in
# the database, student numbers are unique, etc..

def createD():
    """
    This function returns an empty database

    :return: An empty database
    
    """

def addStudent(D: dict, student: dict):
    """
    This function adds a student to the database

    :param dict D: A database D
    :param dict student: A student to be added to the database
    :return: None
    
    """

def studentName(D: dict, number: int):
    """
    This function retrieves the students first and last name from the database by student number

    :param dict D: A database D
    :param int number: A student number
    :return: The students first and last name
    
    """
