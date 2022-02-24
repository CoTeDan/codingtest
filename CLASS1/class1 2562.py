# 2562 *
A = []
for i in range(9): # 9번 입력 받고 A리스트에 추가
    a = int(input())
    A.append(a)

print(max(A), A.index(max(A))+1) # A리스트 최대값과 인덱스 출력