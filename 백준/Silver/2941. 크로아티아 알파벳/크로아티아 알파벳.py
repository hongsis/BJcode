li=['c=','c-','dz=','d-','lj','nj','s=','z=']

t=input()

for i in li:
    t=t.replace(i,'*')# input 변수와 동일한 이름의 변수
print(len(t))



