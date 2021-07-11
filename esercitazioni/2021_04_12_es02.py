#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul  8 15:33:55 2021

@author: alessandro
"""

import numpy as np
import numpy.linalg as npl


def matrice(a): return np.array([1, -1, 2, -1, 6, 1, 2, 1, a]).reshape((3, 3))


AS = [matrice(a) for a in range(6, 11)]

# a)
normeinf = [npl.norm(A, np.inf) for A in AS]
print(normeinf)

# b)
massimo = max(normeinf)
indice = 6 + normeinf.index(massimo)
print(f"Norma massima = {massimo} in indice {indice}")

# c)
normeuno = [npl.norm(A, 1) for A in AS]
print(normeuno)
minimo = min(normeuno)
indice = 6 + normeuno.index(minimo)
print(f"Norma minima = {minimo} in indice {indice}")

# ---------------
