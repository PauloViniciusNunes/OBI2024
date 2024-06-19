#Variáveis do problema
A = []
A_new = []
NullM = []
v = 0 #Número de celulas vivas
s = ''
while True:
    N, Q = map(int, input("input 0: ").split(' '))

    if((1<= N <=50) and (1 <= Q <= 100)):
        break


for k in range(0, N):
    a_input = str(input("input 1: "))
    A.append(a_input)

for repeticoes in range(0, Q):
    #MATRIZ
    for index_rows, rows in enumerate(A):
        for index_char, char in enumerate(rows):
            #SUB-MATRIZ
            for sub_rows in range(index_rows - 1, index_rows + 2):
                for sub_char in range(index_char - 1, index_char + 2):
                    try:
                        if((sub_rows != index_rows) and (sub_char != index_char)):
                            if(A[sub_rows][sub_char] == "1"):
                                v += 1

                    except:
                        v += 0
            
            if(char == "0" and v == 3):
                s += "1"
            elif(char == "0" and v != 3):
                s += "0"
            elif(char == "1" and (v == 3 or v == 2)):
                s += "1"
            elif(char == "1" and v < 2):
                s += "0"
            elif(char == "1" and v > 3):
                s += "0"
            v = 0
        A_new.append(s)
        s = ''
    
    A = A_new
    A_new = NullM

for elements in A:
    print(elements)
