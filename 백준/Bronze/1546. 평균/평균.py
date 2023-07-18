N=int(input())
s=list(map(int,input().split()))
M=max(s)
C=[]
for i in range(N):
    A=s[i]/M*100
    C.append(A)
print(sum(C)/len(C))