r1 = float(input('Primero segmento do triangulo'))
r2 = float(input('segunto segmento do triangulo'))
r3 = float(input('Terceiro segmento do triangulo'))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmentos acima podem formar um triangulo!',end='')
    if r1 == r2 == r3:
        print('Equilatero')
    elif r1 != r2 != r3 != r1:
        print('Escaleno')
    else:
        print('Isoceles')
else:
    print('Os segmentos nao podem formar um triangulo')
