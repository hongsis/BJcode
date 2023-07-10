current_time = input().split()
hour = int(current_time[0])
minute = int(current_time[1])

# 요리 시간 입력 받기
cooking_time = int(input())

# 종료되는 시각 계산
hour += cooking_time // 60
minute += cooking_time % 60

# 시간과 분이 60 이상인 경우 조정
if minute >= 60:
    hour += 1
    minute -= 60
if hour >= 24:
    hour -= 24

# 종료되는 시각 출력
print(hour, minute)

    
    
    