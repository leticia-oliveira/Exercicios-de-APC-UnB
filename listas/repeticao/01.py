"""
Lista de estruturas de repetição|Verificador de anos bissextos
"""
def anobissexto(ano):
    try:
        float(ano)  
    except ValueError:
        print("Não é um ano") 
    else:
        if int(ano) % 400 == 0:
            b="é"
        elif int(ano) % 100 == 0:
            b="não é"
        elif int(ano) % 4 == 0:
            b="é"
        else:
            b="não é"
        print(f'{ano} {b} ano bissexto')
anobissexto(input('Digite um ano\n'))