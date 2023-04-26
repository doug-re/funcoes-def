from bib.mat import *

while True:
    numero_exercicio = int(input("informe o numero do exercicio: "))
    if numero_exercicio == 1:
        exercicio1()
    elif numero_exercicio == 2:
        exercicio2()
    elif numero_exercicio == 3:
        exercicio3()
    elif numero_exercicio == 4:
        exercicio4()
    elif numero_exercicio == 5:
        exercicio5()
    elif numero_exercicio == 6:
        exercicio6()
    elif numero_exercicio == 7:
        exercicio7()
    else:
        print("numero solicitado incorreto, por favor verifique e tente novamente: ")
        