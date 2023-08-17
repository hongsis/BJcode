z=[]
length=[]
for _ in range(5):
    a=input()
    z.append(a)
    length.append(len(a))
    
rst=''
for i in range(max(length)):
    for j in range(5):
        if i < length[j]:
            rst+=z[j][i]
            
print(rst)
        
    