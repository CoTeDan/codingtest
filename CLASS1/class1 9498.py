# 9498
import sys
score = int(sys.stdin.readline()) # 점수입력

if 90<= score <= 100 :  # 90~100 -> A
    print('A')
elif 80 <= score < 90 : # 80~90 -> B
    print('B')
elif 70 <= score < 80 : # 70~80 -> C
    print('C')
elif 60 <= score < 70 : # 60~70 -> D
    print('D')
else :                  # 나머지 점수 -> F
    print('F')