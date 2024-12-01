import random
import csv

itens = ['banana', 'maca', 'pera', 'carne', 'ovo', 'cerveja', 'vinho', 'arroz',
         'feijao', 'batata', 'uva', 'farinha', 'agua', 'queijo', 'presunto', ]

def gerar_lista_compras():
    # seleciona 5 itens aleatórios da lista
    compra = random.sample(itens, 5)

    # cria o arquivo 
    nome_arquivo = "lista_compras.csv"

    #cria o arquivo em modo write 'w',prepara ele para ser escrito,caso ja exista um
    #ele é sobrescrito -- newline está corrigindo as linhas do arquivo
    #
    with open(nome_arquivo, mode='w', newline='') as arquivo_csv:
        escritor_csv = csv.writer(arquivo_csv)
    
        # escreve cada linha do arquivo
        for item in compra:
            escritor_csv.writerow([item])

    print(f"Arquivo '{nome_arquivo}' criado com sucesso.")


gerar_lista_compras()


