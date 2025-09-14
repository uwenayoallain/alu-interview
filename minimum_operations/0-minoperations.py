#!/usr/bin/python3
"""Minimum Operations
======================

Provides a single function, ``minOperations(n)``, that computes the
fewest number of copy/paste operations needed to obtain exactly ``n``
characters 'H', starting from a single 'H', when only two operations
are allowed: Copy All and Paste.

The optimal strategy is equivalent to factoring ``n`` and summing its
prime factors: whenever ``n`` is divisible by a number ``d``, performing
``Copy All`` once and then ``Paste`` ``d-1`` times effectively multiplies
the current count by ``d``, costing ``d`` operations. Repeating this for
each factor yields the minimal total.
"""


def minOperations(n):
    """Return the minimal number of operations to reach ``n`` 'H's.

    The function returns 0 if ``n`` is less than 2 since it's either
    already at the target (1) or impossible (non-positive).

    Args:
        n (int): Target number of 'H' characters.

    Returns:
        int: Fewest number of operations, or 0 if impossible.
    """
    if n <= 1:
        return 0

    ops = 0
    divisor = 2

    while n > 1:
        if n % divisor == 0:
            ops += divisor
            n //= divisor
        else:
            divisor += 1

    return ops
