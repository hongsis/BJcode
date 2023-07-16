N, X=map(int,input().split())
A = list(map(int,input().split()))
B=[]
for i in range(N):
    if X > A[i]:
        print(A[i],end=" ")