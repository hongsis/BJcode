def fac(n):
    if n>1:
        return n*fac(n-1)
    else:
        return 1
n=int(input())
print(fac(n))

