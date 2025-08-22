operacion = input(f'''{'':*^90}
*{'Ingrese la operación a realizar:':^88}*
{'':*^90}
*{'1. Suma':^88}*
*{'2. Resta':^88}*
*{'3. Producto':^88}*
*{'4. División':^88}*
{'':*^90}
''')
print(f'{'':*^90}')
if operacion != '1' and operacion != '2' and operacion != '3' and operacion != '4': # Verificar si el valor dado no es ninguno de los códigos disponibles. 
    print(f'ERROR: ingrese un número valido (1, 2, 3, 4), valor ingresado actualmente: {operacion}')
else:
    n1 = input('Ingrese el primer número: ')
    n2 = input('Ingrese el segundo número: ')
    print(f'{'':*^90}')
    try: # Verificación si n1 y n2 son enteros.
        temp = int(n1) + int(n2)
    except:
        print(f'''ERROR: Ingrese un número real, valores ingresados actualmente:
        {n1}, {n2}''')
    # Tranformamos a número las cadenas n1 y n2.
    else:
        a=float(n1) 
        b=float(n2)
        match operacion: # Aplicación de la operación correspondiente según el código dado por el usuario.
            case '1':
                operacion = 'Suma'
                print(f'Se realizo la operación {operacion.lower()}: {a} + {b} = {a+b:.2f}')
            case '2':
                operacion = 'Resta'
                print(f'Se realizo la operación {operacion.lower()}: {a} - {b} = {a-b:.2f}')
            case '3':
                operacion = 'Producto'
                print(f'Se realizo la operación {operacion.lower()}: {a} * {b} = {a*b:.2f}')
            case '4':
                operacion = 'División'
                if b == 0:
                    print('ERROR: Ingrese un denominador distinto de cero')
                else:
                    print(f'Se realizo la operación {operacion.lower()}: {a} / {b} = {a/b:.2f}')


