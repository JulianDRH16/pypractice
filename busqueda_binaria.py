objetivo = int(input('Escoge un número: '))
epsilon = 0.001
bajo = 0.0
alto = max(1.0, objetivo)
repuesta = (alto + bajo) / 2
while abs(repuesta**2 - objetivo) >= epsilon:
    print(f'bajo= {bajo}, alto = {alto} respuesta = {repuesta}')
    if repuesta**2 < objetivo:
        bajo = repuesta
    else:
        alto = repuesta

    repuesta = (alto + bajo) / 2

print(f'La raiz cuadrada de {objetivo} es {repuesta}')