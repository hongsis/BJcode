s=[]
import sys
c=int(sys.stdin.readline())
for _ in range(c):
    i =list(map(int,sys.stdin.readline().split()))
    if i[0] ==1 :
        s.append(i[1])
    elif i[0] ==2:
        if len(s) !=0:
            print(s[-1])
            s.pop()
        else:
            print(-1)
    elif i[0]==3:
        print(len(s))
    elif i[0] ==4:
        if len(s) !=0:
            print(0)
        else:
            print(1)
    elif i[0] ==5:
        if len(s) !=0:
            print(s[-1])
        else:
            print(-1)    
        




