from lifestore_file import lifestore_products, lifestore_sales, lifestore_searches

administradores = [["jorge", '1234'], ["javier", '1234'], ["jose", '1234']]
usuarios = [['alberto', 'loco23']]

bienvenida = input('¡Bienvenido!\n¿Ya tiene una cuenta? (si/no): ')

# Si no, crear una cuenta
while bienvenida != 'si':
  if bienvenida == 'no': 
    print("\nPor favor, regístrese")
    user = input('\nMi usuario: ')
    #Comprobar que el usuario no esté repetido
    for usuario in usuarios:
      while user == usuario[0]:
        print('Este nombre de usuario ya existe.')
        user = input('Escriba uno nuevo: ')
    contra = input('Contraseña: ')
    # Agregar nueva cuenta admin a la lista
    usuarios.append([user, contra])
    # Refrescar la página
    print('\n ¡Hecho! La página se actualizará.')
    bienvenida = input('\n¡Bienvenido!\n¿Ya tiene una cuenta? (si/no): ')
  #Condicion: si no se escribe ni 'si' ni 'no'
  else: 
    print('\nRespuesta inválida. Responda si/no.')
    bienvenida = input('\n¡Bienvenido!\n¿Ya tiene una cuenta? (si/no): ')

# Inicio de sesión cuando se tiene una cuenta    
usuario_input = input('\nIngrese su usuario: ')
pass_input = input('Ingrese su contraseña: ')

es_admin = 0

# Comprobar que el usuario y contraseña estén correctos
for admin in administradores: 
  if admin[0] == usuario_input and admin[1] == pass_input:
    es_admin = 1
  elif (admin[0] == usuario_input and admin[1] != pass_input):
    es_admin = 2
  else:
    continue

print("\nIniciando sesión, espere...\n")

  # Inicio (o no) de sesión
if es_admin == 1:
  ## While para seguir viendo opciones, si se desea
  no_continua = 0
  print(f'¡Un gusto verlo de nuevo, {usuario_input}!')
  while no_continua != 1:
    print("\n¿Qué le gustaría ver? ( ͡° ͜ʖ ͡°)")
    print('\t1. Productos más vendidos y más rezagados'
          '\n\t2. Productos por reseña en el servicio'
          '\n\t3. Ingresos y ventas')

    # Opcion de visualización
    opcion = input('\nElija una opción: (1:3) ')

    #Introducir un while para validar la primer opción
    # Confirmar si se introduce una opcion valida
    opcion_valida = 0

    # Contar ventas de productos, devoluciones y busquedas
    # Se usa aquí porque se necesitará en las tres opciones (a,b,c)
    ventas = []
    contador_ventas = 0
    contador_busquedas = 0
    devolucion = 0

    for producto in lifestore_products:
      for venta in lifestore_sales: 
        if producto[0] == venta[1]:
          contador_ventas += 1
          if venta[4] == 1:
            devolucion += 1
      for busqueda in lifestore_searches:
        if producto[0] == busqueda[1]:
          contador_busquedas += 1
      id_producto = producto[0]
      nombre_producto = producto[1]
      precio_producto = producto[2]
      categoria_producto = producto[3]
      stock_producto = producto[4]
      ventas.append([id_producto, nombre_producto, contador_ventas, precio_producto, categoria_producto, stock_producto, devolucion, contador_busquedas])
      contador_ventas = 0 
      contador_busquedas = 0
      devolucion = 0

    ## Copiar la ventas como una nueva lista: busquedas
    busquedas = ventas[:]

    while opcion_valida != 1:
      if opcion == '1':
        opcion_valida = 1

        # Dividir productos por categorías 
        #Separar categorías
        categorias = []
        for categoria in lifestore_products:
          if categoria[3] not in categorias: 
            categorias.append(categoria[3])

        #categorías masculinas
        categorias_m = [categorias[0], categorias[3], categorias[7]]
        #categorías femeninas
        categorias_f = [categorias[1], categorias[2], categorias[4], categorias[5], categorias[6]]

        print('\nEscogió "Productos más vendidos y más rezagados".')
        print('\n¿Qué desea ver?'
              '\n\ta. Los 50 productos más vendidos.'
              '\n\tb. Los 100 productos más buscados.'
              '\n\tc. Los 50 productos menos vendidos por categoría.'
              '\n\td. Los 100 productos menos buscados por categoría.')
        
        sub_opcion = input('Elija una subopción: (a:d) ')

        # Confirmar que se introduzca una sub-opción valida
        sub_opcion_valida = 0

        while sub_opcion_valida != 1:
          if sub_opcion == 'a':
            sub_opcion_valida = 1
            
            ## Ordenar ventas de mayor a menor
            length_ventas = len(ventas) - 1
              #Bucle para las pasadas
            for i in range(0, length_ventas):
              #Bucle para las comparaciones
              for j in range(0, length_ventas):
                if ventas[j][2] < ventas[j + 1][2]:
                  temporal = ventas[j]
                  ventas[j] = ventas[j + 1]
                  ventas[j + 1] = temporal

            ### Mostrar los 50 productos más vendidos
            mas_vendidos = ventas[0:50]
            
            print('\na. Los 50 productos más vendidos son: \n')
            for producto in mas_vendidos:
                print(f'#{mas_vendidos.index(producto) + 1}: {producto[1]} (id: {producto[0]}):'
                      f'\nVentas: {producto[2]}\tStock: {producto[5]}\tCategoría: {producto[4]}.\n')
              

          elif sub_opcion == 'b':
            sub_opcion_valida = 1
            ## Ordenar busquedas de mayor a menor
            length_busquedas = len(busquedas) - 1
            #Bucle para la pasada a cada busqueda
            for i in range(0, length_busquedas):
              #Bucle para ordenar
              for j in range(0, length_busquedas):
                if busquedas[j][7] < busquedas[j + 1][7]:
                  temporal = busquedas[j]
                  busquedas[j] = busquedas[j + 1]
                  busquedas[j + 1] = temporal


            print('\nb. Los 100 productos más buscados son:\n ')
            for producto in busquedas:
              print(f'#{busquedas.index(producto) + 1}  {producto[1]} (id: {producto[0]}):'
                    f'\nBúsquedas: {producto[7]}\t Ventas: {producto[2]}\n')

          elif sub_opcion == 'c':
            sub_opcion_valida = 1
            ## Ordenar ventas de menor a mayor
            menores_ventas = ventas[:]
            length_men_ventas = len(menores_ventas) - 1
              #Bucle para las pasadas
            for i in range(0, length_men_ventas):
              #Bucle para las comparaciones
              for j in range(0, length_men_ventas):
                if menores_ventas[j][2] > menores_ventas[j + 1][2]:
                  temporal = menores_ventas[j]
                  menores_ventas[j] = menores_ventas[j + 1]
                  menores_ventas[j + 1] = temporal
            
            ## Ventas por categorias (menor a mayor)
            # Categorías de género masculino
            print('\nc. Productos menos vendidos, por categoría: ')
            i = 0
            for categoria in categorias_m: 
              print(f'\nLos {categoria} menos vendidos son: \n')
              for venta in menores_ventas: 
                if categoria == venta[4]: 
                  i += 1
                  if venta[2] > 1 or venta[2] == 0 :    
                    print(f'#{i}: {venta[1]} (id: {venta[0]}) se vendió {venta[2]} veces.\n')
                  else: 
                    print(f'#{i}: {venta[1]} (id: {venta[0]}) se vendió {venta[2]} vez.\n')
              i = 0

            # Categorías de género femenino
            for categoria in categorias_f: 
              print(f'\nLas {categoria} menos vendidas son: \n')
              for venta in menores_ventas: 
                if categoria == venta[4]: 
                  i += 1
                  if venta[2] > 1 or venta[2] == 0 :    
                    print(f'#{i}: {venta[1]} (id: {venta[0]}) se vendió {venta[2]} veces.\n')
                  else: 
                    print(f'#{i}: {venta[1]} (id: {venta[0]}) se vendió {venta[2]} vez.\n')
              i = 0

          elif sub_opcion == 'd':
            sub_opcion_valida = 1
            ## Ordenar búsquedas de menor a mayor
            menores_busquedas = busquedas[:]
            length_men_busquedas = len(menores_busquedas) - 1
            #Bucle para pasar todos los elementos
            for i in range(0, length_men_busquedas):
              #Bucle para comparar elemento por elemento
              for j in range(0, length_men_busquedas):
                if menores_busquedas[j][2] > menores_busquedas[j + 1][2]:
                  temporal = menores_busquedas[j]
                  menores_busquedas[j] = menores_busquedas[j + 1]
                  menores_busquedas[j + 1] = temporal
            
            ### Menores búsquedas por categoría: 
            print('\nd. Productos menos buscados, por categoría: ')
            #Categoría masculina
            i = 0
            for categoria in categorias_m: 
              print(f'\nLos {categoria} menos buscados son: \n')
              for busqueda in menores_busquedas: 
                if categoria == busqueda[4]: 
                  i += 1
                  if busqueda[2] > 1 or busqueda[2] == 0 :    
                    print(f'#{i}: {busqueda[1]} (id: {busqueda[0]}) se buscó {busqueda[2]} veces.\n')
                  else: 
                    print(f'#{i}: {busqueda[1]} (id: {busqueda[0]}) se buscó {busqueda[2]} vez.\n')
              i = 0

            #Búsqueda femenina
            for categoria in categorias_f: 
              print(f'\nLas {categoria} menos buscadas son: \n')
              for busqueda in menores_busquedas: 
                if categoria == busqueda[4]: 
                  i += 1
                  if busqueda[2] > 1 or busqueda[2] == 0 :    
                    print(f'#{i}: {busqueda[1]} (id: {busqueda[0]}) se buscó {busqueda[2]} veces.\n')
                  else: 
                    print(f'#{i}: {busqueda[1]} (id: {busqueda[0]}) se buscó {busqueda[2]} vez.\n')
              i = 0
          ## Si no se escoge una subopcion correcta
          else:
            print("\nSubopción incorrecta :'(")
            sub_opcion = input('Elija una subopción: (a:d) ')
      
      ### Segunda opcion
      elif opcion == '2':

      # Definir variables necesarias para las subopciones
        reseñas = []
        count_5 = 0
        count_4 = 0
        count_3 = 0
        count_2 = 0
        count_1 = 0
        puntaje = 0
        devolucion = 0 

        ### Contar numero de reseñas y Ponderar calificación
        for producto in lifestore_products: 
          for venta in lifestore_sales:
            if producto[0] == venta[1]:
              if venta[2] == 1:
                count_1 += 1
                puntaje += 1
              elif venta[2] == 2: 
                count_2 += 1
                puntaje += 2
              elif venta[2] == 3:
                count_3 += 1
                puntaje += 3
              elif venta[2] == 4:
                count_4 += 1
                puntaje += 4
              else:
                count_5 += 1
                puntaje += 5
            if producto[0] == venta[1]:
              if venta[4] == 1:
                devolucion += 1
              else:
                continue
          num_reseñas = count_1 + count_2 + count_3 + count_4 + count_5
          puntaje_ponderado = 0
          # Ponderar: sumar puntajes y dividirlos entre el total de reseñas
          if num_reseñas != 0:
            puntaje_ponderado = round(puntaje/num_reseñas, 3)
          reseñas.append([producto[0], producto[1], count_1, count_2, count_3, count_4, count_5, puntaje_ponderado, devolucion])
          count_1 = 0
          count_2 = 0
          count_3 = 0
          count_4 = 0
          count_5 = 0
          puntaje = 0
          devolucion = 0

        opcion_valida = 1
        print('\nEscogió "Productos por reseña en el servicio".')
        print('\n¿Qué desea ver?'
              '\n\ta. Los 20 productos mejor evaluados.'
              '\n\tb. Los 20 productos peor evaluados.'
              '\n\tc. Los 15 productos mejor evaluados (5 o más ventas).')

        sub_opcion = input('\nElija una subopción: (a:c) ')

        # Confirmar que se introduzca una sub-opción valida
        sub_opcion_valida = 0

        while sub_opcion_valida != 1:
        ## Subopcion 1
          if sub_opcion == 'a':
            sub_opcion_valida = 1

            ### Ordenar productos con mejor calificación
            length_reseñas = len(reseñas) -1 
            #Bucle para las pasadas
            for i in range(0, length_reseñas):
              # Bucle para ordenar por mayor puntaje
              for j in range(0, length_reseñas):
                if reseñas[j][7] < reseñas[j + 1][7]:
                  temporal = reseñas[j]
                  reseñas[j] = reseñas[j + 1]
                  reseñas[j + 1] = temporal

            # Extraer los veinte mejor calificados
            mejores_veinte = reseñas[0:20]

            # Imprimir la información
            print('Los veinte productos mejor calificados son:\n')
            for producto in mejores_veinte:
              print(f'#{mejores_veinte.index(producto) +1 } {producto[1]} (id {producto[0]}) tiene:'
                  f'\nPuntaje: {producto[7]}\t Devoluciones: {producto[8]}'
                  f'\n\t5 estrellas {producto[6]} veces.'
                      f'\n\t4 estrellas {producto[5]} veces.'
                      f'\n\t3 estrellas {producto[4]} veces.'
                      f'\n\t2 estrellas {producto[3]} veces.'
                      f'\n\t1 estrella {producto[2]} veces.\n')

          ## Subopcion 2
          elif sub_opcion == 'b':
            sub_opcion_valida = 1

            # Solo considerar productos que tengan ventas
            # Sin ventas, el puntaje será 0 y no será relevante
            # Pero un producto con pocas ventas y baja calificación sí es relevante
            con_ventas = []
            for venta in ventas:
              for reseña in reseñas:
                if venta[2] != 0: 
                  if venta[0] == reseña[0]:
                    id_producto = reseña[0]
                    nombre_producto = reseña[1]
                    count_1 = reseña[2]
                    count_2 = reseña[3]
                    count_3 = reseña[4]
                    count_4 = reseña[5]
                    count_5 = reseña[6]
                    puntaje_ponderado = reseña[7]
                    devolucion = reseña[8]
                    num_ventas = venta[2]
                    con_ventas.append([id_producto, nombre_producto, count_1, count_2, count_3, count_4, count_5, puntaje_ponderado, devolucion, num_ventas])

            ### Ordenar los productos por peor calificación

            length_con_ventas = len(con_ventas) -1 
            #Bucle para las pasadas
            for i in range(0, length_con_ventas):
              # Bucle para ordenar por peor puntaje
              for j in range(0, length_con_ventas):
                if con_ventas[j][7] > con_ventas[j + 1][7]:
                  temporal = con_ventas[j]
                  con_ventas[j] = con_ventas[j + 1]
                  con_ventas[j + 1] = temporal

            peores_veinte = con_ventas[0:20]

            # Imprimir información
            print('No se consideran los productos sin ventas.')
            print('Los productos (con ventas) peor calificados son:\n')
            for producto in peores_veinte:
              print(f'#{peores_veinte.index(producto) + 1} {producto[1]} (id {producto[0]}) tiene:'
                  f'\nVentas: {producto[9]}\t Puntaje: {producto[7]}\t Devoluciones: {producto[8]}'
                  f'\n\t5 estrellas {producto[6]} veces.'
                      f'\n\t4 estrellas {producto[5]} veces.'
                      f'\n\t3 estrellas {producto[4]} veces.'
                      f'\n\t2 estrellas {producto[3]} veces.'
                      f'\n\t1 estrella {producto[2]} veces.\n')

          ## Subopcion 3
          elif sub_opcion == 'c':
            sub_opcion_valida = 1

            ## Ordenar ventas de mayor a menor
            length_ventas = len(ventas) - 1
            #Bucle para las pasadas
            for i in range(0, length_ventas):
            #Bucle para las comparaciones
              for j in range(0, length_ventas):
                  if ventas[j][2] < ventas[j + 1][2]:
                    temporal = ventas[j]
                    ventas[j] = ventas[j + 1]
                    ventas[j + 1] = temporal

            # Se separan los 15 productos con más ventas
            # Porque sólo los 15 primeros tienes más de 5 ventas
            # Y así no sesgar el cálculo con pocas ventas pero alta calificación
            quince_mas_vendidos = ventas[0:15]          

            # Se crea nueva lista: se unen los productos más vendidos
            # Con sus reseñas, puntuación y devoluciones
            quince_con_reseña = []
            for venta in quince_mas_vendidos:
              for reseña in reseñas:
                if venta[0] == reseña[0]:
                  id_producto = reseña[0]
                  nombre_producto = reseña[1]
                  count_1 = reseña[2]
                  count_2 = reseña[3]
                  count_3 = reseña[4]
                  count_4 = reseña[5]
                  count_5 = reseña[6]
                  puntaje_ponderado = reseña[7]
                  devolucion = reseña[8]
                  num_ventas = venta[2]
                  quince_con_reseña.append([id_producto, nombre_producto, count_1, count_2, count_3, count_4, count_5, puntaje_ponderado, devolucion, num_ventas])


            ### Ordenar los quince productos por mejor calificación
            length_los_quince = len(quince_con_reseña) -1 

            #Bucle para las pasadas
            for i in range(0, length_los_quince):
              # Bucle para ordenar por mayor puntaje
              for j in range(0, length_los_quince):
                if quince_con_reseña[j][7] < quince_con_reseña[j + 1][7]:
                  temporal = quince_con_reseña[j]
                  quince_con_reseña[j] = quince_con_reseña[j + 1]
                  quince_con_reseña[j + 1] = temporal


            print('Los quince productos (con 5 o más ventas) mejor calificados son:\n')
            for producto in quince_con_reseña:
              print(f'#{quince_con_reseña.index(producto) + 1} {producto[1]} (id {producto[0]}) tiene:'
                  f'\nVentas: {producto[9]}\t Puntaje: {producto[7]}\t Devoluciones: {producto[8]}'
                  f'\n\t5 estrellas {producto[6]} veces.'
                      f'\n\t4 estrellas {producto[5]} veces.'
                      f'\n\t3 estrellas {producto[4]} veces.'
                      f'\n\t2 estrellas {producto[3]} veces.'
                      f'\n\t1 estrella {producto[2]} veces.\n')          

          else:
            print("\nSubpción incorrecta :'(")
            sub_opcion = input('Elija una subopción: (a:c) ')  

      ### Tercera opción   
      elif opcion == '3':
        opcion_valida = 1
        print('\nEscogió "Ingresos y ventas".')
        print('\n¿Qué desea ver?'
              '\n\ta. Ingresos totales.'
              '\n\tb. Ventas anuales y ventas promedio mensuales.'
              '\n\tc. Los meses con más ventas.')
        
        sub_opcion = input('\nElija una subopción: (a:c) ')

        # Confirmar que se introduzca una sub-opción valida
        sub_opcion_valida = 0

        while sub_opcion_valida != 1:
        ## Subopcion 1
          if sub_opcion == 'a':
            sub_opcion_valida = 1

            #Ingreso por producto
            ingresos_productos = []
            for producto in lifestore_products:
              for venta in ventas: 
                if producto[0] == venta[0]:
                  precio = producto[2]
                  num_ventas = venta[2]
                  devolucion = venta[6]
                  monto_devolucion = devolucion * precio
                  ingreso = (precio * num_ventas) - monto_devolucion
              ingresos_productos.append(ingreso)
              ingreso = 0 

            ingresos_total = sum(ingresos_productos)
            print('El ingreso total (ventas - devoluciones) fue de:'
                  f'\n\t{ingresos_total} pesos. ')
          
          ## Subopción 2 ""
          elif sub_opcion == 'b':
            sub_opcion_valida = 1

            # Contador de ventas 
            ventas_totales = 0

            # Bucle para pasadas
            for producto in lifestore_products:
              #Bucle para contadas
              for venta in lifestore_sales:
                if producto[0] == venta[1]:
                  ventas_totales += 1

            ventas_promedio = ventas_totales//12
          # Imprimir las ventas anuales
            print(f'\nSe realizaron {ventas_totales} ventas en todo el año.')
          # Imprimir las ventas promedio por mes
            print(f'\nSe tienen en promedio {ventas_promedio} ventas al mes.')

          ## Subopción 3 ##
          elif sub_opcion == 'c':
            sub_opcion_valida = 1

            ### Contar ventas por mes 
            #Definir variables
            ventas_mensuales = []
            venta_ene = ['Enero', 0]
            venta_feb = ['Febrero', 0]
            venta_mar = ['Marzo', 0]
            venta_abr = ['Abril', 0]
            venta_may = ['Mayo', 0]
            venta_jun = ['Junio', 0]
            venta_jul = ['Julio', 0]
            venta_ago = ['Agosto', 0]
            venta_sep = ['Septiembre', 0]
            venta_oct = ['Octubre', 0]
            venta_nov = ['Noviembre', 0]
            venta_dic = ['Diciembre', 0]

            #Comenzar a contar el total de ventas y las ventas por mes
            for producto in lifestore_products:
              for venta in lifestore_sales: 
                if producto[0] == venta[1]:
                  if '/01/' in venta[3]: 
                    venta_ene[1] += 1
                  elif '/02/' in venta[3]:
                    venta_feb[1] += 1
                  elif '/03/' in venta[3]:
                    venta_mar[1] += 1
                  elif '/04' in venta[3]:
                    venta_abr[1] += 1
                  elif '/05/' in venta[3]:
                    venta_may[1] += 1
                  elif '/06/' in venta[3]:
                    venta_jun[1] += 1
                  elif '/07/' in venta[3]:
                    venta_jul[1] += 1
                  elif '/08/' in venta[3]:
                    venta_ago[1] += 1
                  elif '/09/' in venta[3]:
                    venta_sep[1] += 1
                  elif '/10/' in venta[3]:
                    venta_oct[1] += 1
                  elif '/11/' in venta[3]:
                    venta_nov[1] += 1
                  else:
                    venta_dic[1] += 1
            ventas_mensuales.extend([venta_ene, venta_feb, venta_mar, venta_abr, venta_may, venta_jun, venta_jul, venta_ago, venta_sep, venta_oct, venta_nov, venta_dic])

            # Ordenar ventas mensuales de mayor a menor
            length_meses = len(ventas_mensuales) - 1
            #Bucle para las pasadas
            for i in range(0, length_meses):
            #Bucle para las comparaciones
              for j in range(0, length_meses):
                  if ventas_mensuales[j][1] < ventas_mensuales[j + 1][1]:
                    temporal = ventas_mensuales[j]
                    ventas_mensuales[j] = ventas_mensuales[j + 1]
                    ventas_mensuales[j + 1] = temporal

            # Imprimir, de mayor a menor, los meses con más ventas
            print('\n\nLista de meses por mayores ventas:\n ')
            for mes in ventas_mensuales:
              if mes[1] != 1:
                print(f'\t#{ventas_mensuales.index(mes) + 1} {mes[0]} tuvo: {mes[1]} ventas.')
              else: 
                print(f'\t#{ventas_mensuales.index(mes) + 1} {mes[0]} tuvo: {mes[1]} venta.')

          else:
            print("Subopción incorrecta :'(")
            sub_opcion = input('Elija una subopción: (a:c) ')
      
      else:
        print("Opción incorrecta :'(")
        opcion = input('Elija una opción: (1:3) ')

    continuar = input('\n\n¿Desea ver algo más? (si/no) ' )
    
    if continuar == 'si': 
      continue
    elif continuar == 'no':
      print('¡Gracias por su visita!\nVuelve pronto.')
      print('Cerrando sersión')
      no_continua = 1
    else: 
      print('Opción incorrecta. Intente otra vez.')
      continuar = input('¿Desea ver algo más? (si/no)')
 

# Condiciones de error al iniciar sesión. 
elif es_admin == 2:
  print("\nSu usuario y contraseña no coinciden.")
  print('Actualicé la página para iniciar sesión.')

else: 
  print(f'Lo sentimos {usuario_input}, su cuenta no tiene permisos de administrador.\n Lárguese, por favor.')

