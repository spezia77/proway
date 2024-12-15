def verificar_ano():
    ano = int(input("Digite o ano: "))

    if (ano % 4 == 0 and ano %100 !=0) or (ano % 400 == 0):
        print(f"o ano {ano} é bissexto")
    else:
        print(f"O ano {ano} não é bissexto")


def calculadora_juros():
    principal = int(input("Digite quanto deseja financiar: "))
    taxaJuros = float(input(f"Digite a taxa de juros: ")) / 100
    tempo = int(input("Digite em quanto tempo deseja parcelar(Digite a quantiade de meses ex: 24): "))

    juros = principal * taxaJuros * tempo
    montanteTotal = principal + juros

    print(f"O montante total será de: R${montanteTotal:.2f}")



romano = 'MMCIV'
def converter_romano_para_inteiro(romano):
    valores = {'I':1,
              'V':5,
              'X':10,
              'L':50,
              'C':100,
              'D':500,
              'M':1000}
    total = 0
    anterior = 0
    for simbolo in romano:
        valor = valores[simbolo]
        if valor < anterior:
            total -= valor
        else:
            total += valor
        anterior = valor
    return total

#print(converter_romano_para_inteiro(romano))


def verificar_primo(n):
    if n <= 1:
        return False
   
    for i in range(2, n):
        if n % i == 0:
            return False 
    return True  

numero = 4
if verificar_primo(numero):
    print(f"{numero} é primo.")
else:
    print(f"{numero} não é primo.")


