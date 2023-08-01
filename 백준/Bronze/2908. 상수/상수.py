i, j =map(int,input().split())
ii=int(str(i)[::-1])
jj=int(str(j)[::-1])

if ii>jj:
    print(ii)
else:
    print(jj)