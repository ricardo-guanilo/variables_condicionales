
try:
    edad = input('Ingrese su edad: ')
    pais = input('''Ingrese su país de residencia:
    1. Perú
    2. Colombia
    3. Argentina
    4. Corea del Sur
    5. Japón
    ''')
    pais=int(pais) #Verificar si el código es entero para saltar error de ser necesario
except:
    print(f'''ERROR: Ingrese un código de país adecuado
    Codigos permitidos: 1,2,3,4,5
    Código actual: {pais}''')
else:
    match pais:
        case 1:
            nombre_pais = 'Perú'
            if(int(edad)>=17):
                print('Usted puede votar')
            else:
                print(f'Usted no puede votar, la edad mínima para votar en {nombre_pais} es 17, su edad es {edad}')
        case 2:
            nombre_pais = 'Colombia'
            if(int(edad)>=18):
                print('Usted puede votar')
            else:
                print(f'Usted no puede votar, la edad mínima para votar en {nombre_pais} es 18, su edad es {edad}')            
        case 3:
            nombre_pais = 'Argentina'
            if(int(edad)>=16):
                print('Usted puede votar')
            else:
                print(f'Usted no puede votar, la edad mínima para votar en {nombre_pais} es 16, su edad es {edad}')
        case 4:
            nombre_pais = 'Corea del Sur'
            if(int(edad)>=19):
                print('Usted puede votar')
            else:
                print(f'Usted no puede votar, la edad mínima para votar en {nombre_pais} es 19, su edad es {edad}')
        case 5:
            nombre_pais = 'Japón'
            if(int(edad)>=18):
                print('Usted puede votar')
            else:
                print(f'Usted no puede votar, la edad mínima para votar en {nombre_pais} es 18, su edad es {edad}')
        case _:
                print(f'''ERROR: Ingrese un código de país adecuado
    Codigos permitidos: 1,2,3,4,5
    Código actual {pais}''') 
                          
