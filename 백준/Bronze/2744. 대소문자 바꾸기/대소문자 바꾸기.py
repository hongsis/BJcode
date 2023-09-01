import sys
input = sys.stdin.readline

a=input().rstrip()

for i in a:
    if i.islower()==True:
        print(i.upper(),end='')
    else:
        print(i.lower(),end='')

