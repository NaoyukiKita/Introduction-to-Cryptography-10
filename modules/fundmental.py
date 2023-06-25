#!/usr/bin/env python
# coding: utf-8

# In[1]:


from numpy import sqrt


# In[2]:


def gcd(x, y):
    if y == 0: return x
    return gcd(y, x % y)

def phi(n):
    for ele in range(2, int(sqrt(n)) + 1):
        if n % ele != 0: continue
        break
    return (ele - 1) * (n // ele - 1)

def eratos(n):
    l = list(range(2, n+1))

    for p in range(2, n+1):
        l = [i for i in l if i == p or i % p != 0]

    return l

def factorize(n):
    p_list = []
    ep_list = []
    current = n
    for p in range(2, n):
        if current == 1: break
        if current % p: continue

        ep = 0
        while current % p == 0:
            current = current // p
            ep += 1
        
        p_list.append(p)
        ep_list.append(ep)

    if current != 1:
        p_list.append(current)
        ep_list.append(1)
    
    return p_list, ep_list

def divisors(n):
    ans = []
    for i in range(1, n + 1):
        if i * i > n: break
        if n % i: continue
        ans.append(i)
        if n // i != i: ans.append(n // i)

    ans.sort()
    return ans

def primitive_roots(mod):
    ds = divisors(mod - 1)

    ans = []
    for g in range(mod):
        if gcd(g, mod) != 1: continue
        primitive = True
        for p in ds:
            if p == mod - 1: continue
            if pow(g, p, mod) != 1: continue
            primitive = False
            break

        if primitive: ans.append(g)
    
    return ans


# In[3]:


if 'get_ipython' in globals():
    import subprocess
    subprocess.run(['jupyter', 'nbconvert', '--to', 'python', '*.ipynb'])

