try:
    precio = input('Ingrese el precio final del producto: ')
    precio = float(precio) # Verificación de tipo de dato de precio, salta error de ser necesario
    tarjeta = input('¿Tiene tarjeta de fidelidad? (Y/N): ').upper() # Permite ingreso de mayúsculas o minúsculas
    print(f'{'':*^90}')
except:
    print(f"ERROR: ingrese un numero real en su precio, precio ingresado: {precio}")
else:
    if (tarjeta != 'Y') and (tarjeta !='N'): # Verificar si se ingresó un valor distinto a Y o N
        print(f'ERROR: Por favor ingrese \"Y\" o \"N\", valor ingresado: {tarjeta}')
    else: # Aplicación de descuento acorde al rango del precio final del producto
        print(f'Precio incial: ${precio:.2f}')
        if precio > 100000: 
            descuento = 0.15
            precio_fin = precio * (1-descuento)
            print(f'Precio con descuento del {descuento*100}%: {precio_fin:.2f}.')
        elif precio >= 50000:
            descuento = 0.1
            precio_fin = precio * (1-descuento)
            print(f'Precio con descuento del {descuento*100}%: {precio_fin:.2f}.')    
        elif precio >= 10000:
            descuento = 0.05
            precio_fin = precio * (1-descuento)
            print(f'Precio con descuento del {descuento*100}%: {precio_fin:.2f}.')
        else:
            print('No se aplicó descuento por precio.')
            precio_fin = precio
        match tarjeta: # Verificación si el cliente posee o no tarjeta de fidelidad.
            case 'Y':
                descuento_tarjeta = 0.05
                precio_fin = precio_fin * (1-descuento_tarjeta)
                print(f'Precio con descuento adicional de {descuento_tarjeta*100}% por tarjeta: {precio_fin:.2f}.')
                print(f'\nSu precio final es: ${precio_fin:.2f}.')
            case 'N':
                print('No se aplicó descuento por tarjeta.')
                print(f'Su precio final es: ${precio_fin:.2f}.')
print(f'{'':*^90}')