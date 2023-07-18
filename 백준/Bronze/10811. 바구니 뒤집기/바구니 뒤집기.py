N, M =map(int,input().split())
b=[i for i in range(1,N+1)]
for _ in range(M):
    i, j = map(int,input().split())
    l=b[i-1:j]
    l.reverse()
    b[i-1:j]=l
for n in range(N):
    print(b[n],end=' ')