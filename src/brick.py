"""
@author: Kieu Nguyen
@date  : 2022-06-24
@desc  : https://codeforces.com/problemset/problem/1/A
"""
m, n, a = list(map(int, input().split()))

m1 = int()
m2 = int()

if (m % a) != 0:
    m1 = (m // a) + 1 
else:
    m1 = (m // a)

if (n % a) != 0:
    n1 = (n // a) + 1 
else:
    n1 = (n // a)

print(m1 * n1)
