import os

def contar_vogais_consoantes(texto):
    os.system('cls')
    vogais = "aeiouAEIOU"
    vogais_count = 0
    consoantes_count = 0

    for caractere in texto:
        if caractere.isalpha(): #isalpha verifica se todos os caracteres de ums string são letras, retorna true se só tiver letras, se tiver espaço ou numeros retorna false
            if caractere in vogais:
                vogais_count += 1
            else:
                consoantes_count += 1
                
    print("O texto: "+ texto +". Tem...")
    print(f"Vogais: {vogais_count}")
    print(f"Consoantes: {consoantes_count}")

texto = input("Digite um texto: ")
contar_vogais_consoantes(texto)