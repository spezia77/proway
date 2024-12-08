import os

def calcular_imc():
    os.system("cls")
    peso = float(input("Digite seu peso: ")) 
    os.system("cls")
    altura = float(input("Digite sua altura: "))

    if peso == 0:
        print("O peso não pode ser igual a 0")
    elif altura == 0:
        print("A altura não pode ser igual a 0")
    # elif peso == 0 and altura == 0:
    #     print("Peso e altura não podem ser iguais a 0")
    
    
    os.system("cls")

    imc = peso / (altura * altura)

    texto = "O resultado do IMC foi: " + str(f"{imc:.2f}") + ", e sua classificação é:"

    if imc == 0:
        print("Você inseriu a altura ou o peso incorretamente \nLembre-se que nenhum deles pode ser igual a 0")
    elif imc < 18.5:
        print(texto, "'Magreza'")
    elif imc >= 18.5 and imc <= 24.9:
        print(texto, "'Peso normal'")
    elif imc >= 25 and imc <= 29.9:
        print(texto, "'Sobrepeso'")
    elif imc >= 30 and imc <= 34.9:
        print(texto, "'Obesidade GRAU I'")
    elif imc >= 35 and imc <= 39.9:
        print(texto, "'Obesidade GRAU II'")
    elif imc >= 40: 
        print(texto, "'Obesidade GRAU III'")


if __name__ == '__main__':
    calcular_imc()