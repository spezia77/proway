import os
import random

#lista de extensoes
extensoes = ['.txt', '.pdf', '.docx', '.csv']

#criar arquivo aleatorio
def criar_arquivo_aleatorio(pasta, nome_arquivo=f"arquivo_{random.randint(1, 99)}"):

    #cria a pasta
    txt = "arquivos/pasta_txt"
    pdf = "arquivos/pasta_pdf"
    docx = "arquivos/pasta_docx"
    csv = "arquivos/pasta_csv"
    pasta = "arquivos"
    os.makedirs(pasta, exist_ok=True)
    os.makedirs(txt, exist_ok=True)
    os.makedirs(pdf, exist_ok=True)
    os.makedirs(docx, exist_ok=True)
    os.makedirs(csv, exist_ok=True)
    
    extensao = random.choice(extensoes)

    if extensao == '.txt':
        caminho_arquivo = os.path.join(txt, nome_arquivo + extensao)
    
        #cria o arquivo
        with open(caminho_arquivo, 'w') as f:
            f.write("ARQUIVO TXT")  #escrita dentro do arquivo
    
        print(f"Arquivo criado: {caminho_arquivo}")
        return caminho_arquivo
    
    elif extensao == '.pdf':
        caminho_arquivo = os.path.join(pdf, nome_arquivo + extensao)
    
        #cria o arquivo
        with open(caminho_arquivo, 'w') as f:
            f.write("ARQUIVO PDF")  #escrita dentro do arquivo
    
        print(f"Arquivo criado: {caminho_arquivo}")
        return caminho_arquivo
    
    elif extensao == '.docx':
        caminho_arquivo = os.path.join(docx, nome_arquivo + extensao)
    
        #cria o arquivo
        with open(caminho_arquivo, 'w') as f:
            f.write("ARQUIVO DOCX")  #escrita dentro do arquivo
    
        print(f"Arquivo criado: {caminho_arquivo}")
        return caminho_arquivo
    
    elif extensao == '.csv':
        caminho_arquivo = os.path.join(csv, nome_arquivo + extensao)
    
        #cria o arquivo
        with open(caminho_arquivo, 'w') as f:
            f.write("ARQUIVO CSV")  #escrita dentro do arquivo
    
        print(f"Arquivo criado: {caminho_arquivo}")
        return caminho_arquivo

diretorio = "."
criar_arquivo_aleatorio(diretorio)


