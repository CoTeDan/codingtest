# 2884
H, M = map(int, input().split())

if 45 <= M <= 60 :
    print(H, M-45)
elif 45 > M and H == 0 :
    print("23", M+15)
elif 45 > M and H != 0 :
    print(H-1, M+15)