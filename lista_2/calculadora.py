import os

def calculadora():
    operacao = input("Deseja usar qual operação?\n1 - SOMA\n2 - SUBTRAÇÃO\n3 - DIVISÃO \n4 - MULTIPLICAÇÃO\n ")
    os.system("cls")
    n1 = int(input("Digite o primeiro número: "))
    n2 = int(input("Digite o segundo número: "))

    soma = n1 + n2
    subtracao = n1 - n2
    divisao = n1 / n2
    multiplicacao = n1 * n2
    
    try:
        if operacao == '3' and n2 == '0':
            print("Não é possível dividir por 0")
        elif operacao == '1':
            print("O resultado da conta é: ",soma)
        elif operacao == '2':
            print("O resultado da conta é: ",subtracao)
        elif operacao == '3':
            print("O resultado da conta é: ",divisao)
        elif operacao == '4':
            print("O resultado da conta é: ",multiplicacao)
    except ValueError:
        print("Não é possível dividir por 0")


calculadora()