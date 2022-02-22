# 2920
a = list(map(int, input().split())) # 입력받기
count1 = 0 # 값 초기화
count2 = 0
count3 = 0
for i in range(8):      # count 세는 반복문
    if a[i] == (i+1) :
        count1 += 1
    elif a[i] == (8-i) :
        count2 += 1
    else :
        break
if count1 == 8 :        # count 값에 따른 출력문
    print("ascending")
elif count2 == 8 :
    print("descending")
else:
    print("mixed")        