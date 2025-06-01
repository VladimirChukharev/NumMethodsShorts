#!/usr/bin/env python
# -*- coding: utf8 -*-

"""Classify read numbers"""
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


def natural_int(match_object: re.Match[str]) -> int:
    """Convert matched text to positive `int`"""
    assert match_object["sign"] in ("", "+") and match_object["value"][0] in "123456789"

    res: int = 0
    for digit in match_object["value"]:
        res = res * 10 + int(digit)
    return res


def nonnegative(match_object: re.Match[str]) -> int:
    """Convert matched text to 0 or positive `int`"""
    assert match_object["sign"] in ("", "+")

    res: int = 0
    for digit in match_object["value"]:
        res = res * 10 + int(digit)
    return res


def integer_int(match_object: re.Match[str]) -> int:
    """Convert matched text to `int`"""
    assert match_object["sign"] in ("", "+", "-")

    res: int = 0
    for digit in match_object["value"]:
        res = res * 10 + int(digit)
    return -res if match_object["sign"] == "-" else res


def rational_num(match_object: re.Match[str]) -> tuple[int, int]:  # FIXME
    """Convert matched text to a rational as a pair of int (second is unsigned but stored as signed)"""
    assert match_object["sign"] in ("", "+", "-")

    res: int = 0
    for digit in match_object["value"]:
        res = res * 10 + int(digit)
    return (-res, 1) if match_object["sign"] == "-" else (res, 1)


def main() -> None:
    """Run a test"""
    for text in "+0045", "-0045", "0.(3)", ".1e2", "0.1(9)", "12.", "-01.2(3)e-001", "0":
        for name, pattern in ReadNumber.patterns.items():
            match_object = pattern.match(text)
            if match_object and match_object['rest'] == '':
                print(f"For {text=}: {name} =>> {match_object.groupdict()}.")
                match name:
                    case "n":
                        print(f"{natural_int(match_object)}")
                    case "z0":
                        print(f"{nonnegative(match_object)}")
                    case "z":
                        print(f"{integer_int(match_object)}")
                    case "q":
                        print(f"{rational_num(match_object)}")
                    case _:
                        pass # raise ValueError(f"Unknown key {name=}.")


if __name__ == "__main__":
    main()
