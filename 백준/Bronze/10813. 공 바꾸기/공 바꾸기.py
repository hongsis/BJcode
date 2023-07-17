N, M=map(int,input().split())
bsk=list(range(1,N+1))
temp=0

for _ in range(M):
    i, j=map(int,input().split())
    temp=bsk[i-1]
    bsk[i-1]=bsk[j-1]
    bsk[j-1]=temp
for n in range(N):
    print(bsk[n],end=' ')