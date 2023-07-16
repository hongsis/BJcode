n_list=[]
for i in range(9):
    n_list.append(int(input()))
nmax=max(n_list)
idx=n_list.index(nmax)
print(nmax)
print(idx+1)