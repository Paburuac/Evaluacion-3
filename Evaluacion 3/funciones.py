def menu():
    print("OPCIONES DE MENU")
    print("1. Registrar puntajes torneo")
    print("2. Listar todos los puntajes")
    print("3. Imprimir por tipo")
    print("4. Salir del programa")

def registrar_puntajes():
        diccionario=[]
        id_jugador=input("Ingrese su ID de jugador: ")
        nombre=input("Ingrese el nombre del jugador: ")
        apellido=input("Ingrese el apellido del jugador: ")
        juego=input("Ingrese el juego en que esta participando: ")
        try:
            puntaje=int(input("Ingrese el puntaje que usted obtuvo en su respectivo juego: "))
        except:
            print("Debe ingresar un puntaje con numeros")
            puntaje=int(input("Ingrese el puntaje que usted obtuvo en su respectivo juego: "))
        tipo=input("Ingrese su tipo de jugador (Principiante, Avanzado, Experto): ").lower()
        Datos_jugador={
            "ID Jugador":id_jugador,
            "Nombre":nombre,
            "Apellido":apellido,
            "Juego":juego,
            "Puntaje":puntaje,
            "Tipo":tipo,
        }
        diccionario.append([Datos_jugador])
        print("Jugador registrado", diccionario)
    
def listar_puntajes():
    diccionario=[]
    print("Lista de jugadores")
    for id_jugador in diccionario:
        return(f"El ID del jugador es: {id_jugador},")
    for nombre in diccionario:
        return(f"El nombre del jugador es: {nombre},")
    for apellido in diccionario:
        return(f"El apellido del jugador es: {apellido},")
    for juego in diccionario:
        return(f"El juego del jugador es: {juego},")
    for puntaje in diccionario:
        return(f"El puntaje del jugador es: {puntaje},")
    for tipo in diccionario:
        return(f"El tipo del jugador es: {tipo},")

def imprimir_por_tipo():
    diccionario=[]
    archivo_salida=f"hoja_de_ruta_.txt"
    with open(archivo_salida,"w") as archivo:
        archivo.write(f"Se ha agregado {diccionario} a la hoja de ruta")
        print(f"Hoja de ruta ha sido guardada en {archivo_salida}")