N=int(input())
A=[]
for _ in range(N):
    s=int(input())
    A.append(s)
A.sort()
for i in range(len(A)):
    print(A[i])