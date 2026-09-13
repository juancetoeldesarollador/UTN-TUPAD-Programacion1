# Ejercicio 1
nombre_cliente = input("Cliente: ")
while not nombre_cliente.isalpha() or nombre_cliente == "":
    print("Error: Ingrese un nombre válido (solo letras).")
    nombre_cliente = input("Cliente: ")

cant_prod_input = input("Cantidad de productos: ")
while not cant_prod_input.isdigit() or int(cant_prod_input) <= 0:
    print("Error: Ingrese una cantidad entera positiva mayor a 0.")
    cant_prod_input = input("Cantidad de productos: ")

cant_productos = int(cant_prod_input)

total_sin_desc = 0.0
total_con_desc = 0.0

for i in range(1, cant_productos + 1):
    print(f"Producto {i}")
    
    precio_input = input("Precio: ")
    while not precio_input.isdigit() or int(precio_input) <= 0:
        print("Error: Ingrese un precio válido (número entero positivo).")
        precio_input = input("Precio: ")
    precio = int(precio_input)
    
    descuento_opc = input("Descuento (S/N): ").lower()
    while descuento_opc != 's' and descuento_opc != 'n':
        print("Error: Ingrese 's' o 'n'.")
        descuento_opc = input("Descuento (S/N): ").lower()
    
    total_sin_desc += precio
    if descuento_opc == 's':
        total_con_desc += precio * 0.90
    else:
        total_con_desc += precio

ahorro_total = total_sin_desc - total_con_desc
promedio_producto = total_con_desc / cant_productos

print(f"Total sin descuentos: ${total_sin_desc:.2f}")
print(f"Total con descuentos: ${total_con_desc:.2f}")
print(f"Ahorro: ${ahorro_total:.2f}")
print(f"Promedio por producto: ${promedio_producto:.2f}")


# Ejercicio 2
USUARIO_CORRECTO = "alumno"
CLAVE_CORRECTA = "python123"

intentos = 0
acceso_concedido = False

while intentos < 3 and not acceso_concedido:
    intentos += 1
    usuario = input(f"Intento {intentos}/3 Usuario: ")
    clave = input("Clave: ")
    
    if usuario == USUARIO_CORRECTO and clave == CLAVE_CORRECTA:
        acceso_concedido = True
        print("Acceso concedido.")
    else:
        print("Error: credenciales inválidas.")

if not acceso_concedido:
    print("Cuenta bloqueada")
else:
    opcion = ""
    while opcion != "4":
        print("\n1) Estado 2) Cambiar clave 3) Mensaje 4) Salir")
        opcion = input("Opción: ")
        
        if not opcion.isdigit():
            print("Error: ingrese un número válido.")
        elif int(opcion) < 1 or int(opcion) > 4:
            print("Error: opción fuera de rango.")
        else:
            if opcion == "1":
                print("Inscripto")
            elif opcion == "2":
                nueva_clave = input("Nueva clave: ")
                if len(nueva_clave) < 6:
                    print("Error: mínimo 6 caracteres.")
                else:
                    confirmacion = input("Confirme nueva clave: ")
                    if nueva_clave == confirmacion:
                        CLAVE_CORRECTA = nueva_clave
                        print("Clave actualizada correctamente.")
                    else:
                        print("Error: Las claves no coinciden.")
            elif opcion == "3":
                print("¡El éxito es la suma de pequeños esfuerzos repetidos día tras día!")
            elif opcion == "4":
                print("Sesión finalizada.")


# Ejercicio 3
lunes1 = ""
lunes2 = ""
lunes3 = ""
lunes4 = ""

martes1 = ""
martes2 = ""
martes3 = ""

operador = input("Ingrese nombre del operador: ")
while not operador.isalpha() or operador == "":
    print("Error: Nombre inválido (solo letras).")
    operador = input("Ingrese nombre del operador: ")

opcion = ""
while opcion != "5":
    print("\n--- MENÚ DE AGENDA ---")
    print("1. Reservar turno")
    print("2. Cancelar turno")
    print("3. Ver agenda del día")
    print("4. Ver resumen general")
    print("5. Cerrar sistema")
    
    opcion = input("Opción: ")
    
    if not opcion.isdigit() or int(opcion) < 1 or int(opcion) > 5:
        print("Error: Seleccione una opción del 1 al 5.")
    else:
        if opcion == "1":
            dia = input("Elegir día (1=Lunes, 2=Martes): ")
            while dia != "1" and dia != "2":
                print("Error: Día no válido.")
                dia = input("Elegir día (1=Lunes, 2=Martes): ")
                
            paciente = input("Nombre del paciente: ")
            while not paciente.isalpha() or paciente == "":
                print("Error: Nombre inválido (solo letras).")
                paciente = input("Nombre del paciente: ")
                
            if dia == "1":
                if paciente == lunes1 or paciente == lunes2 or paciente == lunes3 or paciente == lunes4:
                    print("Error: El paciente ya tiene un turno reservado este día.")
                elif lunes1 == "":
                    lunes1 = paciente
                    print("Turno reservado con éxito en Lunes (Turno 1).")
                elif lunes2 == "":
                    lunes2 = paciente
                    print("Turno reservado con éxito en Lunes (Turno 2).")
                elif lunes3 == "":
                    lunes3 = paciente
                    print("Turno reservado con éxito en Lunes (Turno 3).")
                elif lunes4 == "":
                    lunes4 = paciente
                    print("Turno reservado con éxito en Lunes (Turno 4).")
                else:
                    print("No hay cupos disponibles para el Lunes.")
            else:
                if paciente == martes1 or paciente == martes2 or paciente == martes3:
                    print("Error: El paciente ya tiene un turno reservado este día.")
                elif martes1 == "":
                    martes1 = paciente
                    print("Turno reservado con éxito en Martes (Turno 1).")
                elif martes2 == "":
                    martes2 = paciente
                    print("Turno reservado con éxito en Martes (Turno 2).")
                elif martes3 == "":
                    martes3 = paciente
                    print("Turno reservado con éxito en Martes (Turno 3).")
                else:
                    print("No hay cupos disponibles para el Martes.")

        elif opcion == "2":
            dia = input("Elegir día a cancelar (1=Lunes, 2=Martes): ")
            while dia != "1" and dia != "2":
                print("Error: Día no válido.")
                dia = input("Elegir día a cancelar (1=Lunes, 2=Martes): ")
                
            paciente = input("Nombre del paciente a cancelar: ")
            while not paciente.isalpha() or paciente == "":
                print("Error: Nombre inválido.")
                paciente = input("Nombre del paciente a cancelar: ")
                
            cancelado = False
            if dia == "1":
                if lunes1 == paciente:
                    lunes1 = ""
                    cancelado = True
                elif lunes2 == paciente:
                    lunes2 = ""
                    cancelado = True
                elif lunes3 == paciente:
                    lunes3 = ""
                    cancelado = True
                elif lunes4 == paciente:
                    lunes4 = ""
                    cancelado = True
            else:
                if martes1 == paciente:
                    martes1 = ""
                    cancelado = True
                elif martes2 == paciente:
                    martes2 = ""
                    cancelado = True
                elif martes3 == paciente:
                    martes3 = ""
                    cancelado = True
                    
            if cancelado:
                print("Turno cancelado correctamente.")
            else:
                print("El paciente no fue encontrado en la agenda de ese día.")

        elif opcion == "3":
            dia = input("Ver agenda de qué día? (1=Lunes, 2=Martes): ")
            while dia != "1" and dia != "2":
                print("Error: Día no válido.")
                dia = input("Ver agenda de qué día? (1=Lunes, 2=Martes): ")
                
            if dia == "1":
                print("Agenda Lunes:")
                print("Turno 1:", lunes1 if lunes1 != "" else "(libre)")
                print("Turno 2:", lunes2 if lunes2 != "" else "(libre)")
                print("Turno 3:", lunes3 if lunes3 != "" else "(libre)")
                print("Turno 4:", lunes4 if lunes4 != "" else "(libre)")
            else:
                print("Agenda Martes:")
                print("Turno 1:", martes1 if martes1 != "" else "(libre)")
                print("Turno 2:", martes2 if martes2 != "" else "(libre)")
                print("Turno 3:", martes3 if martes3 != "" else "(libre)")

        elif opcion == "4":
            ocu_lunes = (1 if lunes1 != "" else 0) + (1 if lunes2 != "" else 0) + (1 if lunes3 != "" else 0) + (1 if lunes4 != "" else 0)
            disp_lunes = 4 - ocu_lunes
            
            ocu_martes = (1 if martes1 != "" else 0) + (1 if martes2 != "" else 0) + (1 if martes3 != "" else 0)
            disp_martes = 3 - ocu_martes
            
            print(f"Lunes: {ocu_lunes} ocupados, {disp_lunes} disponibles.")
            print(f"Martes: {ocu_martes} ocupados, {disp_martes} disponibles.")
            
            if ocu_lunes > ocu_martes:
                print("Día con más turnos ocupados: Lunes")
            elif ocu_martes > ocu_lunes:
                print("Día con más turnos ocupados: Martes")
            else:
                print("Empate en cantidad de turnos ocupados.")

print("Sistema cerrado por el operador", operador)


# Ejercicio 4
energia = 100
tiempo = 12
cerraduras_abiertas = 0
alarma = False
codigo_parcial = ""
forzar_seguidas = 0

agente = input("Nombre del agente: ")
while not agente.isalpha() or agente == "":
    print("Error: Ingrese un nombre válido.")
    agente = input("Nombre del agente: ")

while energia > 0 and tiempo > 0 and cerraduras_abiertas < 3 and not (alarma and tiempo <= 3):
    print(f"\n[Estado Agente {agente}] Energía: {energia} | Tiempo: {tiempo} | Cerraduras: {cerraduras_abiertas}/3 | Alarma: {alarma}")
    print("1. Forzar cerradura (-20 energía, -2 tiempo)")
    print("2. Hackear panel (-10 energía, -3 tiempo)")
    print("3. Descansar (+15 energía, -1 tiempo)")
    
    opc_input = input("Opción: ")
    while not opc_input.isdigit() or int(opc_input) < 1 or int(opc_input) > 3:
        print("Error: Selección de opción inválida (1-3).")
        opc_input = input("Opción: ")
    
    opcion = int(opc_input)
    
    if opcion == 1:
        forzar_seguidas += 1
        energia -= 20
        tiempo -= 2
        
        if forzar_seguidas == 3:
            alarma = True
            print("¡Anti-Spam! Se forzó 3 veces seguidas. La cerradura se trabó y la alarma se encendió.")
        else:
            if energia < 40:
                print("¡Riesgo de alarma por baja energía!")
                riesgo = input("Elija número (1-3): ")
                while not riesgo.isdigit() or int(riesgo) < 1 or int(riesgo) > 3:
                    print("Error: Ingrese un entero de 1 a 3.")
                    riesgo = input("Elija número (1-3): ")
                if riesgo == "3":
                    alarma = True
                    print("¡Se activó la alarma!")
            
            if not alarma:
                cerraduras_abiertas += 1
                print("¡Abriste 1 cerradura!")
                
    elif opcion == 2:
        forzar_seguidas = 0
        energia -= 10
        tiempo -= 3
        
        for paso in range(1, 5):
            codigo_parcial += "A"
            print(f"Progreso hackeo paso {paso}/4... Código parcial: {codigo_parcial}")
            
        if len(codigo_parcial) >= 8 and cerraduras_abiertas < 3:
            cerraduras_abiertas += 1
            print("¡Hackeo completado! Se abrió 1 cerradura automáticamente.")
            
    elif opcion == 3:
        forzar_seguidas = 0
        tiempo -= 1
        if alarma:
            energia += 5
            print("Descansaste con la alarma activada (+5 energía neta).")
        else:
            energia += 15
            print("Descansaste (+15 energía).")
        
        if energia > 100:
            energia = 100

if cerraduras_abiertas >= 3:
    print("\n¡VICTORIA! Lograste abrir las 3 cerraduras y escapar.")
elif alarma and tiempo <= 3:
    print("\nDERROTA: El sistema se bloqueó por la alarma activa y falta de tiempo.")
else:
    print("\nDERROTA: Te quedaste sin recursos (energía o tiempo agotados).")


# Ejercicio 5
gladiador = input("Nombre del Gladiador: ")
while not gladiador.isalpha() or gladiador == "":
    print("Error: Solo se permiten letras.")
    gladiador = input("Nombre del Gladiador: ")

vida_jugador = 100
vida_enemigo = 100
pociones = 3
ataque_pesado_base = 15
ataque_enemigo_base = 12

print("=== INICIO DEL COMBATE ===")

while vida_jugador > 0 and vida_enemigo > 0:
    print(f"\n{gladiador} (HP: {vida_jugador}) vs Enemigo (HP: {vida_enemigo}) | Pociones: {pociones}")
    print("Elige acción:")
    print("1. Ataque Pesado")
    print("2. Ráfaga Veloz")
    print("3. Curar")
    
    opc_input = input("Opción: ")
    while not opc_input.isdigit() or int(opc_input) < 1 or int(opc_input) > 3:
        print("Error: Ingrese un número válido.")
        opc_input = input("Opción: ")
        
    opcion = int(opc_input)
    
    if opcion == 1:
        if vida_enemigo < 20:
            dano_realizado = float(ataque_pesado_base * 1.5)
            print("¡Golpe Crítico!")
        else:
            dano_realizado = float(ataque_pesado_base)
        
        vida_enemigo -= int(dano_realizado)
        print(f"¡Atacaste al enemigo por {dano_realizado} puntos de daño!")
        
    elif opcion == 2:
        print(">> ¡Inicias una ráfaga de golpes!")
        for i in range(3):
            vida_enemigo -= 5
            print("> Golpe conectado por 5 de daño")
            
    elif opcion == 3:
        if pociones > 0:
            vida_jugador += 30
            pociones -= 1
            print("Te has curado 30 HP.")
        else:
            print("¡No quedan pociones!")
            
    if vida_enemigo > 0:
        vida_jugador -= ataque_enemigo_base
        print(f">> ¡El enemigo contraataca por {ataque_enemigo_base} puntos!")

print("=== FIN DEL COMBATE ===")
if vida_jugador > 0:
    print(f"¡VICTORIA! {gladiador} ha ganado la batalla.")
else:
    print("DERROTA. Has caído en combate.")