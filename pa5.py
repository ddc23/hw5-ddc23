"""
This module contains functions to calculate the greatest common divisor, 
remove opposite pairs from paths, and find roots using bisection.
"""

def gcd(a, b):
    """
    Compute the greatest common divisor of two numbers using the Euclidean algorithm.
    
    :param a: First integer
    :param b: Second integer
    :return: The greatest common divisor of a and b
    """
    while b != 0:
        a, b = b, a % b
    return a

def remove_pairs(path):
    """
    Remove directly opposite adjacent pairs from a path string.
    
    :param path: A string representing the path with directions
    :return: A string with opposite adjacent pairs removed
    """
    opposite = {'N': 'S', 'S': 'N', 'E': 'W', 'W': 'E'}
    if len(path) < 2:
        return path
    
    first, second = path[0], path[1]
    
    if second == opposite.get(first, ''):
        return remove_pairs(path[2:])
    return first + remove_pairs(path[1:])

def bisection_root(f, a, b, tol=1e-6):
    """
    Find the root of a function within an interval [a, b] using the bisection method.
    
    :param f: A function for which the root is to be found
    :param a: Lower bound of the interval
    :param b: Upper bound of the interval
    :param tol: Tolerance for stopping the search
    :return: A float representing the approximate root
    """
    if f(a) * f(b) >= 0:
        raise ValueError("The function does not change signs within the given interval.")

    while abs(b - a) > tol:
        c = (a + b) / 2
        if f(c) == 0 or abs(f(c)) < tol:
            return c
        if f(a) * f(c) < 0:
            b = c
        else:
            a = c

    return (a + b) / 2

