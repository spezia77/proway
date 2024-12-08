import os
import random

def gerar_numero_aleatorio():
    return random.randint(1,10)


def adivinhar_numero():
    os.system('cls')
    numero_gerado = gerar_numero_aleatorio()

    while True:
        try:
            numero = int(input("Adivinha um número entre 1 e 50: "))
            
            if numero == numero_gerado:
                print("Acertou, parabéns!")
                break
            else:
                os.system('cls')
                print("Número errado, tente novamente")
                
        except ValueError:
            print("Insira um número válido")


adivinhar_numero()