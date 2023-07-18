s=[]
for _ in range(10):
    A=int(input())
    s.append(A%42)

rest=set(s)
print(len(rest))