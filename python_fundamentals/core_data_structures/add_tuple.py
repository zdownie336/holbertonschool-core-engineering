#!/usr/bin/env python3
def add_tuple(tuple_a=(), tuple_b=()):
    if len(tuple_a) == 1:
        ta0 = tuple_a[0]
        ta1 = 0
    elif len(tuple_a) == 0:
        ta0 = 0
        ta1 = 0
    else:
        ta0 = tuple_a[0]
        ta1 = tuple_a[1]

    if len(tuple_b) == 1:
        tb0 = tuple_b[0]
        tb1 = 0
    elif len(tuple_b) == 0:
        tb0 = 0
        tb1 = 0
    else:
        tb0 = tuple_b[0]
        tb1 = tuple_b[1]

    return (ta0 + tb0, ta1 + tb1)
