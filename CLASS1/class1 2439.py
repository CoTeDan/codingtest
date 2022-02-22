# 2439
import sys
N = int(sys.stdin.readline()) # 입력받기

for i in range(1,N+1):
    print(' '*(N-i),end='') # 띄어쓰기를 N-i만큼 출력한 뒤
    print('*'*i)            # 별을 i 만큼 출력