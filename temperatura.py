try:
    print(f"{'':*^90}")
    temp_inicial = input("Ingrese la temperatura: ")
    print(f"{'':*^90}")
    origen = input(f'''Ingrese la escala de Origen:
    1. Celcius (°C)
    2. Farenheit (°F)
    3. Kelvin (°K)
    ''')
    print(f"{'':*^90}")
    destino = input('''Ingrese la escala de Origen:
    1. Celcius (°C)
    2. Farenheit (°F)
    3. Kelvin (°K)
    ''')
    print(f"{'':*^90}")
    # Transformación de cadena a número para saltar errores de tipo de dato
    temp_inicial = float(temp_inicial)
    origen = int(origen)
    destino = int(destino)
except:
    print(f'''ERROR: indique valores adecuados.
Temperatura (número real): {temp_inicial}
Origen (1,2,3): {origen}
Destino (1,2,3): {destino}''')
else:
    if origen in range(1,4) and destino in range(1,4):
        match origen:
            case 1:
                inicio = '°C'
                match destino:
                    case 1:
                        fin, temp_final = '°C',temp_inicial 
                    case 2:
                        fin, temp_final = '°F', (temp_inicial * 1.8) + 32
                    case 3:
                        fin, temp_final = '°K', (temp_inicial + 273.15)
            case 2:
                inicio = '°F'
                match destino:
                    case 1:
                        fin, temp_final = '°C', (temp_inicial - 32) / 1.8
                    case 2:
                        fin, temp_final = '°F', temp_inicial
                    case 3:
                        fin, temp_final = '°K', ((temp_inicial - 32) / 1.8) + 273.15
            case 3:
                inicio = '°K'
                match destino:
                    case 1:
                        fin, temp_final = '°C', (temp_inicial - 273.15)
                    case 2:
                        fin, temp_final = '°F', ((temp_inicial - 273.15) * 1.8) + 32
                    case 3:
                        fin, temp_final = '°K', temp_inicial
            case _:
                print(f'Ingrese un valor adecuado de origen (1,2,3), valor actual: {origen}')

        print(f''' Conversión realizada de {temp_inicial}{inicio} a {temp_final}{fin}
{'':*^90}''')
    elif origen in range(1,4):
        print(f'Ingrese un valor adecuado de destino (1,2,3), valor actual: {destino}')
    elif destino in range(1,4):
        print(f'Ingrese un valor adecuado de origen (1,2,3), valor actual: {origen}')
    else:
        print(f'''Ingrese valores adecuados para origen y destino (1,2,3), valores actuales:
Origen: {origen}
Destino: {destino}''')
