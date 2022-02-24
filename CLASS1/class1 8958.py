# 8958
T = int(input())

for i in range(T):
    S = list(input())
    score = 0
    sum_score = 0
    for j in range(len(S)):
        if S[j] == 'O' :
            score += 1
            sum_score += score
        else:
            score = 0

    print(sum_score)