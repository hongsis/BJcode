n=int(input())
a=[]

for i in str(n):
    a.append(int(i))
    
a.sort(reverse=True)

for j in a:
    print(j,end='')

