def pb(n):
    if n==0:
        return 0
    elif n==1 or n==2:
        return 1
    else:
        return pb(n-1)+pb(n-2)

n=int(input())
print(pb(n))

    

