import os
import random
import string

# gerar palavras aleatorias com a biblioteca string
def gerar_palavras_aleatorias(tamanho=8):
    return ''.join(random.choices(string.ascii_lowercase, k=tamanho)) #ascii gera todos os caracteres do alfabeto
    #                                                                 __lowercase em minuscuo,   
    #                                                                  o k=tamanho define o tamanho das palavras, nesse caso 8

def gerar_arquivo(nome_arquivo, pasta):
    os.makedirs(pasta, exist_ok=True)  #cria a pasta 'arquivo_para_ler'

    #caminho do arquivo
    caminho_arquivo = os.path.join(pasta, nome_arquivo)

    #funçao acima armazenada em uma variavel, onde vai gerar de 1 a 50 palavras dentro do arquivo
    texto = [gerar_palavras_aleatorias() for _ in range(random.randint(1, 50))]

    #converte a lsita de palavras em uma string separadas por um espaco ' '
    texto_completo = ' '.join(texto)

    #cria o arquivo e escreve as palavaras nele
    with open(caminho_arquivo, 'w') as f: # w = write
        f.write(texto_completo)  # escreve as palavras ja transformadas em string

    print(f"Arquivo '{nome_arquivo}' gerado com sucesso em '{pasta}'.")

#definindo o nome do arquivo e o nome da pasta
nome_arquivo = "arquivo_aleatorio.txt"
pasta = "arquivo_para_ler"


def contar_palavras():
    #caminho do arquivo
    caminho = os.path.join(pasta, nome_arquivo)
    
    # abre o arquivo e le o que tem dentro
    with open(caminho, 'r') as f: # 'r' vem de read
        texto = f.read()  #le o conteudo do arquivo

    #conta as palavras dentro do arquivo
    palavras = texto.split()  # .split divide as palavras do texto separando por espaço
    quantidade_palavras = len(palavras)  #conta o numero de palavras dentro do arquivo
    
    print(f"O arquivo contém {quantidade_palavras} palavras.")

# chama a função que gera o arquivo
gerar_arquivo(nome_arquivo, pasta)

# chama a função que conta as palavras
contar_palavras()