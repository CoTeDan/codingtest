# 1546
N = int(input()) # 과목 수 N
score = list(map(int, input().split())) # 점수 리스트 만들기
M = max(score) # 점수 중 최댓값 M

for i in range(N):
    score[i] = (score[i]/M)*100

result = sum(score)/N
print(result)
