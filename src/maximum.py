

a, b, c = list(map(int, input().split()))

maxi = a

if maxi < b:
    maxi = b
if maxi < c:
    maxi = c

print(maxi)

"""
max = a

if max < b -> max = b
if max < c -> max = c

print (max)

"""