# 10871
N, X = map(int, input().split()) # 입력받기
A = list(map(int, input().split())) 

for i in range(len(A)):
    if A[i]<X : # X보다 A[i]값이 작으면 출력
        print(A[i], end=' ')
    else :  # 그 외에는 뛰어넘기
        continue
