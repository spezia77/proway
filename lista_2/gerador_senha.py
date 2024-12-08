import random
import string


def gerar_caracteres(tamanho):
    return ''.join(random.choices(string.ascii_letters, string.digits, string.punctuation, k=tamanho))


def gerar_senha():
    tamanho = int(input("Digite quantos caracteres você quer na senha: "))
    
    senha_criada = gerar_caracteres(tamanho)
    
    print("A sua senha aleatória é:", senha_criada)

gerar_senha()