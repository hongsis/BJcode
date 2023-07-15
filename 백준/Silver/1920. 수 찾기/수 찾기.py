N=int(input())
A = list(map(int, input().split()))
A.sort()

M=int(input())
m=list(map(int, input().split()))

for num in m:
    L=0
    U=len(A)-1

    
    while L <= U:
        mid=(L+U)//2
        if num == A[mid]:
            print(1)
            break
        elif num < A[mid]:
            U= mid-1
        else:
            L= mid+1
   
    if L > U:
        print(0)
    