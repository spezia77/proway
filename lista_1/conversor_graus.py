import os

def conversor():

    os.system("cls")

    print("C = Celsius\nF = Fahrenheit")
    origem = str(input("Informe a unidade térmica de origem: ")).lower()
    os.system("cls")
    graus = float(input("Informe o valor: "))

    os.system("cls")

    celsius_fahrenheit = (graus * 1.8) + 32
    fahrenheit_celsius = (graus - 32) / 1.8

    if origem == 'c':
        print(graus,"Celsius em Fahrenheit são:",celsius_fahrenheit)
    elif origem == 'f':
        print(graus,"Fahrenheit em Celsius são:",fahrenheit_celsius)


if __name__ == '__main__':
    conversor()
    