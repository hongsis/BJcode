import sys

n=int(input())
for _ in range(n):
    s = []
    a = sys.stdin.readline()
    for i in a:
        if i=='(':
            s.append(a)
        elif i==')':
            if s :
                s.pop()
            else:
                print('NO')
                break
    else:
        if len(s) ==0:
            print('YES')
        else:
            print('NO')

    
        
        
        
        