# 1075
N = int(input())
F = int(input())

N=N-(N%100)
div = N//F
remain = N%F
result = F*(div+1)
ten = result%100

if remain == 0:
    print('00')
elif ten < 10 : 
    a=0
    print(str(a)+str(ten))
else:
    print(result%100)
