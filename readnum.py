#!/usr/bin/env python
# -*- coding: utf8 -*-

"""Classify read numbers"""
from math import gcd
import re


class ReadNumber:
    """Read a number from a text string and classify what classes it belongs to by the value and representation.
    For example, "+45" by both criteria can belong to Q (rationals), Z (integers), Z0 (non-negative integers),
    and N (naturals), while "+45.0(00)" and "4.5e+01" by representation belong only to Q, having the same value.
    """

    patterns = dict(n=re.compile(r"""
                            (?P<sign>[+]?)       # optional plus sign
                            (?P<zeros>0*)        # optional leading zeros
                            (?P<value>[1-9]\d*)  # at least 1 non-zero digit and any digits
                            (?P<rest>.*)         # should be empty for just a natural number
                        """, re.X),
                    z0=re.compile(r"""
                            (?P<sign>[+]?)  # optional sign
                            (?P<zeros>0*)    # optional leading zeros
                            (?P<value>\d+)   # at least 1 digit
                            (?P<rest>.*)     # should be empty for a non-negative integer number
                        """, re.X),
                    z=re.compile(r"""
                            (?P<sign>[-+]?)  # optional sign
                            (?P<zeros>0*)    # optional leading zeros
                            (?P<value>\d+)   # at least 1 digit
                            (?P<rest>.*)     # should be empty for an integer number
                        """, re.X),
                    q=re.compile(r"""
                            (?P<sign>[-+]?)  # optional sign
                            (?P<zeros>0*)    # optional leading zeros
                            (?P<value>\d+)   # digits
                            (?P<dot>\.?)     # optional dot
                            (?P<mantissa>\d*)  # digits
                            (?P<periodic>(?P<left>\()\d+(?P<right>\)))?  # optional periodic part
                            (?P<rest>.*)           # should be empty for just a rational number
                        """, re.X),
                    f=re.compile(r"""
                            (?P<sign>[-+]?)  # optional sign
                            (?P<zeros>0*)    # optional leading zeros
                            (?P<value>\d*)   # digits
                            (?P<dot>\.?)     # optional dot
                            (?P<mantissa>\d*)  # digits, at least one in zeros, value, and/or mantissa
                            (?P<exp>([eE][-+]?\d+)?)  # optional exponent part
                            (?P<rest>.*)     # should be empty for a float number
                        """, re.X),
                    g=re.compile(r"""
                            (?P<sign>[-+]?)  # optional sign
                            (?P<zeros>0*)    # optional leading zeros
                            (?P<value>\d*)   # digits
                            (?P<dot>\.?)     # optional dot
                            (?P<mantissa>\d*)  # digits, at least one in zeros, value, and/or mantissa
                            (?P<periodic>(?P<left>\()\d+(?P<right>\)))?  # optional periodic part
                            (?P<exp>([eE][-+]?\d+)?)  # optional exponent part
                            (?P<rest>.*)
                        """, re.X))
    indexes = ("sign", "zeros", "value", "dot", "mantissa", "periodic", "left", "right", "exp", "rest")


def char2int(character: str) -> int:
    """Convert a digit to an integer"""
    assert len(character) == 1
    match character:
        case "0":
            return 0
        case "0":
            return 0
        case "1":
            return 1
        case "2":
            return 2
        case "3":
            return 3
        case "4":
            return 4
        case "5":
            return 5
        case "6":
            return 6
        case "7":
            return 7
        case "8":
            return 8
        case "9":
            return 9
        case _:
            raise ValueError(f"Unexpected {character=}.")


def str2natural(string: str) -> int:
    """Convert a string of digits to a positive `int`"""
    assert all((character in "0123456789" for character in string))

    res: int = 0
    for digit in string:
        res = res * 10 + char2int(digit)
    return res


def natural_int(match_object: re.Match[str]) -> int:
    """Convert matched text to positive `int`"""
    assert match_object["sign"] in ("", "+") and match_object["value"][0] in "123456789"
    return str2natural(match_object["value"])


def nonnegative(match_object: re.Match[str]) -> int:
    """Convert matched text to 0 or positive `int`"""
    assert match_object["sign"] in ("", "+")
    return str2natural(match_object["value"])


def integer_int(match_object: re.Match[str]) -> int:
    """Convert matched text to `int`"""
    assert match_object["sign"] in ("", "+", "-")
    return -str2natural(match_object["value"]) if match_object["sign"] == "-" else str2natural(match_object["value"])


def rational_num(match_object: re.Match[str]) -> tuple[int, int]:
    """Convert matched text to a rational as a pair of int (second is unsigned but stored as signed)"""
    assert match_object["sign"] in ("", "+", "-")

    numerator: int = 0
    denominator: int = 1
    entire: int = str2natural(match_object["value"])
    m_length: int = 0
    if match_object["mantissa"] and (m_length := len(match_object["mantissa"])) > 0:
        numerator = str2natural(match_object["mantissa"])
        denominator = pow(10, m_length)
    p_num: int = 0    # numerator for periodic part
    p_denom: int = 1  # denominator for periodic part
    if match_object["periodic"] and (p_length := len(match_object["periodic"])) > 0:
        assert p_length > 2
        p_length -= 2
        p_num = str2natural(match_object["periodic"][1:-1])  # trim '(' and ')'
        p_denom = (pow(10, p_length) - 1) * pow(10, m_length)
    # print(f"{numerator=}, {denominator=}, {numerator/denominator=}; {p_num=}, {p_denom=}, {p_num/p_denom=}.")
    divisor: int = 1
    p_fact: int = p_denom
    factor: int = denominator
    if (divisor := gcd(denominator, p_denom)) > 1:
        factor //= divisor
        p_fact //= divisor
    numerator = numerator * p_fact + p_num * factor
    denominator *= p_fact
    numerator += entire * denominator
    if (divisor := gcd(denominator, numerator)) > 1:
        denominator //= divisor
        numerator //= divisor
    return (-numerator, denominator) if match_object["sign"] == "-" else (numerator, denominator)


def main() -> None:
    """Run a test"""
    for text in "+0045", "-0045", "0.(3)", ".1e2", "0.1(9)", "12.", "-01.2(3)e-001", "0", "0.4", "-02.7(63)":
        for name, pattern in ReadNumber.patterns.items():
            match_object = pattern.match(text)
            if match_object and match_object['rest'] == '':
                print(f"For {text=}: {name} =>> {match_object.groupdict()}.")
                match name:
                    case "n":
                        print(f"n:  {natural_int(match_object)}")
                    case "z0":
                        print(f"z0: {nonnegative(match_object)}")
                    case "z":
                        print(f"z:  {integer_int(match_object)}")
                    case "q":
                        nu, de = rational_num(match_object)
                        print(f"q:  {nu}, {de}; {nu/de = }")
                    case _:
                        pass # raise ValueError(f"Unknown key {name=}.")


if __name__ == "__main__":
    main()
