# 10816 *시간초과 코드 주의
import sys
from collections import Counter # Counter 사용
N = int(sys.stdin.readline())
N2 = list(map(int, sys.stdin.readline().split()))
    
M = int(sys.stdin.readline())
M2 = list(map(int, sys.stdin.readline().split()))

N2 = Counter(N2)

for i in M2:
    print(N2[i])