"""
Lista de estruturas sequenciais|Conversores de temperatura:
"""
#Fahrenheit para Celsius:
def converte(f):
    c=(f-32)/1.8
    c=float(c)
    c=round(c,1)
    print(f'{f}° F são {c}° C')
converte(float(input('Digite o valor em graus Fahrenheit\n')))

"""
De forma reduzida:
"""

#Celsius para Fahrenheit:
def converte(c):
  print(f'{c}° C são {float((c*(9/5))+32):.1f}° F')
converte(float(input('Digite o valor em graus Celsius\n')))