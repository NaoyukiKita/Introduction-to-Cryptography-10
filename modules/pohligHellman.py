#!/usr/bin/env python
# coding: utf-8

# In[1]:


from sympy.ntheory.modular import crt

from fundmental import factorize
from babyGiant import BabyGiant


# In[2]:


def PohligHellman(alpha, base, mod):
    n = mod - 1

    p_list, ep_list = factorize(n)

    order_list = [p ** ep for p, ep in zip(p_list, ep_list)]
    np_list = [n // order for order in order_list]
    gammap_list = [pow(base, np, mod) for np in np_list]
    alphap_list = [pow(alpha, np, mod) for np in np_list]
    xp_list = [BabyGiant(alphap, gammap, mod) \
               for alphap, gammap, order in zip(alphap_list, gammap_list, order_list)]

    x = crt(order_list, xp_list)[0]

    return x


# In[3]:


if 'get_ipython' in globals():
    import subprocess
    subprocess.run(['jupyter', 'nbconvert', '--to', 'python', '*.ipynb'])

