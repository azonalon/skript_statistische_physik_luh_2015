#!/bin/python
# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
plt.style.use('bmh')
import numpy as np
import scipy as sc
import os, sys, re
os.chdir(os.path.split(sys.argv[0])[0])
plt.rc('text', usetex=True)
plt.rc('font', family='serif', size=14)

X = np.linspace(-10, 10, 1000)


def normal(x, sigma, mu):
    return 1./(2.*np.pi * sigma) * np.exp(-(x - mu)**2 / (2. * sigma**2))

plt.xticks([0], [r'$\left< X \right>$'])
# plt.yticks([])
plt.ylabel(r'$ Q_N(y) $')
plt.plot(X, normal(X, 1., 0))
plt.plot(X, normal(X, 2., 0))
plt.plot(X, normal(X, 3., 0))
plt.text(5., 0.02, r'Kleines $N$')
plt.text(0.8, 0.14, r'Gro\ss{}es $N$')
plt.savefig('./figures/first.eps', format='eps', dpi=1000)
plt.show()
