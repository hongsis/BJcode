m=[]
for _ in range(5):
    A=int(input())
    m.append(A)
m.sort()
print(int(sum(m)/len(m)),m[2],sep='\n')