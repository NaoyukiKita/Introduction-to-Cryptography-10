#!/usr/bin/env python
# coding: utf-8

# In[1]:


from numpy import sqrt, ceil


# In[2]:


def BabyGiant(alpha, base, mod):
    gamma = base
    n = mod

    m = int(ceil(sqrt(n)))

    # baby step
    B = []
    solved = False
    for r in range(0, m):
        first = (alpha * pow(gamma, -r, n)) % n
        second = r
        B.append((first, second))

        if first != 1: continue
        x = r
        solved = True

    # giant step
    if not solved:
        delta = pow(gamma, m, n)
        max_q = 1000000

        current = delta
        for q in range(1, max_q+1):
            for r in range(0, m):
                if B[r][0] != current: continue
                x = q * m + r
                solved = True
            
            if solved: break
            current = (current * delta) % n
    
    return x


# In[3]:


if 'get_ipython' in globals():
    import subprocess
    subprocess.run(['jupyter', 'nbconvert', '--to', 'python', '*.ipynb'])

