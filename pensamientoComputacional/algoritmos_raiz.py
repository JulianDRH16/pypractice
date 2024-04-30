def selecciona_opciones():
    print(f"Seleccione el algoritmo que desea usar: \n 1.Enumeracion Exaustiva \n 2.Aproximación \n 3.Busqueda Binaria")
    opcion = int(input(f'Escriba la opcion que desee:'))
    numero = int(input(f'Escriba el número que desea utilizar con el algoritmo: '))

    if opcion == 1:
        print("1.Enumeración Exaustiva")
        ##numero = int(input(f'Escriba el número que desea utilizar con el algoritmo de enumeración: '))
        enumeracion(numero)
    elif opcion == 2:
        print("2.Aproximación")
        ##numero = int(input(f'Escriba el número que desea utilizar con el algoritmo de aproximación: '))
        aproximacion(numero)
    elif opcion == 3:
        print("Busqueda binaria")
        ##numero = int(input(f'Escriba el número que desea utilizar con el algoritmo de Busqueda binaria: '))
        busqueda_binaria(numero)
    else:
        print(":"*8, "Seleccione unicamente las opciones 1, 2 o 3", ":"*8)
        selecciona_opciones()

def enumeracion(objetivo):
    respuesta = 0
    while respuesta**2 < objetivo:
        print(respuesta)
        respuesta += 1
    if respuesta**2 == objetivo:
        print(f'La raiz cuadrada de {objetivo} es {respuesta}')
    else:
        print(f'{objetivo} no tiene raiz cudrada exacta')         

def aproximacion(objetivo):
    epsilon = 0.001
    paso = epsilon**2
    respuesta = 0.0
    
    while abs(respuesta**2 - objetivo) >= epsilon and respuesta <= objetivo:
        print(abs(respuesta**2 - objetivo), respuesta)
        respuesta += paso
        
    if abs(respuesta**2 - objetivo) >= epsilon:
        print(f'No se encuntró la raiz cuadrada de {objetivo}')
    else:
        print(f'La raiz cuadrada de {objetivo} es {respuesta}')

def busqueda_binaria(objetivo):
    epsilon = 0.01
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

selecciona_opciones()