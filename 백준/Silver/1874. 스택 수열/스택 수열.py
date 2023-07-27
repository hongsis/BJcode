n=int(input())
curr=1
s=[]
a=[]
f=0

for _ in range(n):
    z=int(input())
    while curr <= z:
        s.append(curr)
        a.append('+')
        curr+=1
        
    if s[-1] == z:
        s.pop()
        a.append('-')
    else:
        print('NO')
        f=1
        break

if f==0:
    for i in a:
        print(i)