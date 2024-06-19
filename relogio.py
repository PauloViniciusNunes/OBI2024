while True:
    H = int(input(''))
    M = int(input(''))
    S = int(input(''))
    T = int(input(''))

    if ((0<=H <=23) and (0 <= M <= 59) and (0 <= S <= 59) and (1 <= T <= 10**9)):
        break

S += T

if(S>59):
    M += S // 60
    S = S % 60
if(M>59):
    H += M // 60
    M = M % 60
if(H>23):
    H = H % 24

print(H)
print(M)
print(S)
