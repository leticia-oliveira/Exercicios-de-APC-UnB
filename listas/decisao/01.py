"""
Lista de estruturas de decisão|Áreas de figuras geométricas
"""
def area(f, x, y): #Em que f é uma forma geométrica e x e y são suas medidas de base ou raio e altura, respectivamente.
    area=x*y
    if f=='retangulo' or f=='r' or f=='q' or f=='quadrado' or f=='retângulo':
        if f=='q' or f=='quadrado':
            f='quadrado'
        else:
            f='retângulo'
    elif f=='circulo' or f=='c' or f=='círculo':
        area=int(3*x**2)
        f='círculo'
    elif f=='triangulo' or f=='t' or f=='triângulo':
        area=area/2
        f='triângulo'
    else:
        area="naosei"
        print('Não sei calcular isso... ˚( ´•︵•` )·˚')
    if area!="naosei":
        print(f'O {f} tem {area} de área')
area(input('Qual forma geométrica você quer medir?\n'), int(input('Qual a medida da base (ou raio, em caso de círculo)?\n')), int(input('Qual a altura?\n')))