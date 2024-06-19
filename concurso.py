A = []
while True:
    N, K = map(int, input("").split(' '))
    if(1 <= K <= N <= 500):
        break

while True:

    A[0:(N-1)] = map(int, input("").split(' '))
    if(1 <= max(A) <= 100):
        break
SortedA = sorted(A, reverse=True)


def CountIfBiggerOrThan(matriz, value):
    count = 0
    for i in matriz:
        if i >= value:
            count += 1
    return count


if(K == 1):
    print(max(A))
else:
    for i in SortedA:
        if(CountIfBiggerOrThan(SortedA, i) >= K):
            print(i)
            break