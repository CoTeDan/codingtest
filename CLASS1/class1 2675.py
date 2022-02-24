# 2675
T = int(input()) # 테스트 케이스 개수

for i in range(T) : # T번 테스트
    R, S = input().split() 
    R = int(R) 
    S = list(S) 
    for i in range(len(S)): # 리스트S 길이 만큼 반복
        print(S[i]*R, end = '') # 문자열S 를 횟수R 만큼 반복하여 출력하는 코드
        if i == (len(S)-1) :
            print('')

