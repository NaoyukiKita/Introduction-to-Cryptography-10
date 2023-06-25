#!/usr/bin/env python
# coding: utf-8

# In[1]:


from numpy import sqrt, ceil, log
import random

from fundmental import gcd


# In[2]:


def Pollard(alpha, base, mod, max_len=None):
    n = mod - 1

    G = list(range(1, mod))
    G1 = G[:mod // 3]
    G2 = G[mod // 3 : (mod // 3) * 2]
    G3 = G[(mod // 3) * 2:]
    # max_iter is based on birthday paradox
    max_iter = int(ceil((1 + sqrt(1 + 8 * n * log(2))) / 2))

    while True:
        x = random.choice(G)
        y = 0
        beta = pow(base, x, mod)

        x_list = [x]
        y_list = [y]
        beta_list = [beta]
        indices = [0]

        found = False
        for j in range(1, max_iter + 1):
            # update
            if beta in G1:
                x = (x + 1) % n
                y = y
                beta = (base * beta) % mod
            elif beta in G2:
                x = (2 * x) % n
                y = (2 * y) % n
                beta = (beta ** 2) % mod
            elif beta in G3:
                x = x
                y = (y + 1) % n
                beta = (alpha * beta) % mod
            
            # find
            if beta in beta_list:
                index = beta_list.index(beta)
                found = True
                break
            
            # delete
            if j % 2 == 0:
                index = indices.index(j // 2)
                _ = x_list.pop(index)
                _ = y_list.pop(index)
                _ = beta_list.pop(index)

            # store
            x_list.append(x)
            y_list.append(y)
            beta_list.append(beta)
            indices.append(j)

            # check the constraint
            if max_len is not None and len(beta_list) > max_len: break
        
        if not found: continue

        x_dif = x_list[index] - x
        y_dif = y - y_list[index]

        g = gcd(gcd(x_dif, y_dif), n)
        c1 = y_dif // g
        c2 = x_dif // g
        mod_prime = n // g

        z_list = []
        for _ in range(mod_prime):
            if c2 % c1 == 0: z_list.append(c2 // c1)
            c2 += mod_prime

        solved = False
        for z in z_list:
            current_x = z
            for k in range(g):
                if pow(base, current_x, mod) == alpha:
                    solved = True
                    break
                current_x += mod_prime
            if solved: break
        
        if solved: return current_x


# In[3]:


if 'get_ipython' in globals():
    import subprocess
    subprocess.run(['jupyter', 'nbconvert', '--to', 'python', '*.ipynb'])

