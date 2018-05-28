# -*- coding: utf-8 -*-

"""

This module contain the gcd function and gcd_stein function that uses to get
Greatest Common Divisor.
"""


def gcd(num1: int, num2: int) -> int:
    if num2 == 0:
        return num1
    else:
        return gcd(num2, num1 % num2)


def gcd_stein(num1: int, num2: int) -> int:
    if num1 < num2:
        num1, num2 = num2, num1

    if num2 == 0:
        return num1

    if num1 % 2 == 0 and num2 % 2 == 0:
        return 2 * gcd_stein(num1 // 2, num2 // 2)

    if num1 % 2 == 0:
        return gcd_stein(num1 // 2, num2)

    if num2 % 2 == 0:
        return gcd_stein(num1, num2 // 2)

    return gcd_stein((num1 + num2) // 2, (num1 - num2) // 2)
