def reverse_str(s):
    """Return reverse of input str (s)"""
    return s[::-1]


def is_Palindrome(s):
    """Boolean method to check whether  given string is a palindrome"""
    rev = reverse_str(s)
    return s == rev


def factorial(n):
    """Calculates factorial iteratively."""
    if not (isinstance(n, int) and n >= 0):
        raise ValueError("'n' must be a non-negative integer.")
    if n == 0:
        return 1
    result = 1
    for i in range(2, n+1):
        result *= i
    return result
