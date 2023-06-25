#!/usr/bin/env python
# coding: utf-8

# In[4]:


from numpy import sqrt, ceil, log
from sympy.ntheory.modular import crt
import random

from fundmental import primitive_roots
from babyGiant import BabyGiant


# In[5]:


def IndexCalculus(alpha, base, mod, factor_base):
    if base not in primitive_roots(mod):
        print(f'base {base} must be a primitive root mod {mod}.')
        return
    
    # inner function
    def B_smooth(b, factor_base):
        for factor in factor_base:
            while b % factor == 0: b = b // factor
        
        return b == 1
    
    xq_list = []
    for q in factor_base:
        xq = BabyGiant(alpha=q, base=base, mod=mod)
        xq_list.append(xq)
    
    y_list = []
    eq_matrix = []
    for y in range(1, mod):
        b = (alpha * pow(base, y, mod)) % mod
        if not B_smooth(b, factor_base): continue
        
        eq_list = []
        for factor in factor_base:
            eq = 0
            while b % factor == 0:
                b = b // factor
                eq = eq + 1
            eq_list.append(eq)
        y_list.append(y)
        eq_matrix.append(eq_list)

    x_list = []
    for i in range(len(y_list)):
        s = sum([xq * eq for xq, eq in zip(xq_list, eq_matrix[i])])
        x = (s - y_list[i]) % (mod - 1)

        x_list.append(x)
    
    return list(set(x_list))


# In[6]:


if 'get_ipython' in globals():
    import subprocess
    subprocess.run(['jupyter', 'nbconvert', '--to', 'python', '*.ipynb'])

