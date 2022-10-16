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
                            (?P<rest>.*)     # should be empty for an intger number
                        """, re.X),
                    q=re.compile(r"""
                            (?P<sign>[-+]?)  # optional sign
                            (?P<zeros>0*)    # optional leading zeros
                            (?P<value>\d+)   # digits
                            (?P<dot>\.?)     # optional dot
                            (?P<mantissa>\d*)  # digits
                            (?P<periodic>(\(\d+\))?)  # optional periodic part
                            (?P<rest>.*)           # should be empty for just a rational number
                        """, re.X),
                    f=re.compile(r"""
                            (?P<sign>[-+]?)  # optional sign
                            (?P<zeros>0*)    # optional leading zeros
                            (?P<value>\d*)   # digits
                            (?P<dot>\.?)     # optional dot
                            (?P<mantissa>\d*)  # digits, at least one in zeros, value, and/or mantissa
                            (?P<exp>[eE][-+]?\d+)  # optional exponent part
                            (?P<rest>.*)           # should be empty for a float number
                        """, re.X))


def main():
    """Run a test"""
    for text in "+0045", "0.(3)", ".1e2":
        for name, pattern in ReadNumber.patterns.items():
            print(f"{name=}")
            if match_object := pattern.match(text):
                print(f"For {text=}: {name} =>> {match_object=}.")
                # print(f"For {text=}: {match_object.group('sign')=}, {match_object.group('zeros')=}, "
                #       f"{match_object.group('value')=}, {match_object.group('rest')=}.")


if __name__ == "__main__":
    main()
