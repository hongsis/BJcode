n = int(input()) #전형적인 그리디 알고리즘 문제

for _ in range(n):
	money = int(input())
	for i in [25, 10, 5, 1]:
		print(money//i, end=' ')
		money = money%i
    
    
    
    