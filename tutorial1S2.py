import math

# 5. Write a short Python function that takes two numbers, a and b, and returns True when a|b.

def divides(a,b):
    return ((b % a)  == 0)

def divides(a: int, b: int):
    """
    This function tests if a divides b

    :int a: First value
    :int b: Second value
    :return: boolean to see if it divides
    """
    # Body
    result = ((b % a)  == 0)
    return result


divides(4,-12)

# 6. Write a short Python function that takes three numbers, a, b, c and returns True when a ≡ b
# (mod c).

# VS Code code snippets! 

def mod_equiv(a: int, b: int, c: int):
    """
    This function does xyz.

    :int a: First value
    :int b: Second value
    :int c: Third value
    :return: boolean to see if it modular equivalent
    """
    # Body
    return divides(c, a-b)



2 ** 15 * 2 ** 3 // 2 ** 10
import math
math.log(256//16,2)
math.log2(256//16)

# Write a short Python program that takes a number of addresses n and returns the minimum
# number of bits required to express that many unique addresses. Note that n might not be a power
# of 2. You may wish to us math.ceil().

def minimum_bits(n: int):
    """
    This function takes a number of addresses n and returns minimum number of bits.

    :param int n: Number of addresses
    :return: Integer of minimum number of bits
    """
    # Body
    return math.ceil(math.log2(n))

minimum_bits(13)
