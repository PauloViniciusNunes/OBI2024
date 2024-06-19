while True:
    E = int(input(""))
    D = int(input(""))

    if((0 <= E <= 5) and (0 <= D <= 5) and (E != D)):
        break

if( E > D ):
    print(E + D)
else:
    print(2*(D - E))