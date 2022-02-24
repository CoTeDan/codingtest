# 2475
a = list(map(int, input().split())) # 입력
sum = 0     
for i in range(len(a)): 
    sum = sum + (a[i]**2) # sum 계산

result = sum%10 # sum을 10으로 나눈 나머지 result
print(result)