#!/usr/bin/env python
"""\
Tutorial 2 Functions
@Author: Alan
@Date: 2024 Semester 1
"""

# Import Libraries 
import math

### Bits

x = "string"
y = 2

1+2

# Question 1
# How many bits are required if you need 18 unique bit strings? Write a short Python function
# that does this calculation for any number of bit strings.

def numAddress(numStrings: int) -> int:
    """
    This function takes a number of addresses n and returns minimum number of bits.
    
    :param int numStrings: Number of addresses
    :return: Integer of minimum number of bits
    """
    bits = math.ceil(math.log2(numStrings))
    return bits

numAddress( 16 )

### Character and Text Representation

# References: https://docs.python.org/3/library/functions.html#ord
# References: https://docs.python.org/3/library/functions.html#bin
# References: https://docs.python.org/3/library/functions.html#hex

bin(ord('C'))

0b101 + 0b011

hex(0b11001011)


bin(0xAE)
