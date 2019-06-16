#!/usr/bin/env python3

"""
A python implementation of interactive sort.

The code is intentionally ~ugly~ PERLish.
"""

from itertools import permutations, count, takewhile


def interactive_sort(L):
    """
    Sort a list interactively.

    :param L: A list of items of any printable type.
    :return: A sorted copy of `L`.
    """
    while True:
        for maybe_sorted in permutations(L):
            print(f"Candidate: {maybe_sorted}.")
            if (
                next(
                    ans for ans in (
                        input("Is this sorted (y/N)? ").lower()
                        for _ in count()
                    )
                    if not ans or ans in "yn"
                ) == "y"
            ):
                return list(maybe_sorted)


if __name__ == "__main__":
    print(f"""Sorted: {', '.join(interactive_sort(list(takewhile(
        bool,
        (
            input(f'Input an element[{idx}] (leave empty to quit): ')
            for idx in count()
        )
    ))))}""")
