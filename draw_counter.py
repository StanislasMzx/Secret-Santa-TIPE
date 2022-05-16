#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created in 2022

@author: Stanislas MEZUREUX
Copyright (c) 2021 Stanislas MEZUREUX. All rights reserved.
"""

from itertools import permutations


"""
Presumed formula : (nb_people_in_one_team !)^(nb_teams)
"""


def check_draw(D, L, p, n):
    for e in D:
        if e[1] not in L[((e[0]-1)//p + 1)%n]:
            return False
    return True


def gen_draws(p, n):
    M = [i for i in range(1, n*p+1)]
    P = list(permutations(M))
    R = [[]]*len(P)
    for i, e in enumerate(P):
        D = [()]*(n*p)
        for j in range(len(e)):
            D[j] = (j, e[j])
        R[i] = D
    return R


def count(p, n):
    L = [[p*i+j+1 for j in range(p)] for i in range(n)]
    R = gen_draws(p, n)
    res = 0
    for e in R:
        if check_draw(e, L, p, n):
            res += 1
    return res


# print(count(4, 1))