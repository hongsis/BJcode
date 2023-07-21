N=int(input())
A=[]
import sys
for _ in range(N):
    s=int(sys.stdin.readline())
    A.append(s)
A.sort()
for i in range(len(A)):
    print(A[i])