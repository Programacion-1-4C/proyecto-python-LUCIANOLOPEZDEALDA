def crear_equipo(lista_equipos = []):
    equipo = input('Que nombre le pones a tu equipo: ')
    lista_equipos.append(equipo)
    print(lista_equipos)


def fichar_jugador(jugador_fichado = []):
    jugadores = ["Messi", "CR7", "Neymar", "Pogba", "Dybala", "Halland", "Mbappe", "Pele", "Maradona", "Foden", "Kun"]
    print("Que jugador quieres fichar?")
    print(jugadores)
    nombre_jugador = input("Ingresa el nombre del jugador a fichar: ")
    indice = jugadores.index(nombre_jugador)
    jugadores.pop(indice)
    print(jugadores)
    jugador_fichado.append(nombre_jugador)
    print(jugador_fichado)



def director_tecnico():
    while True:
        print(
            '1. Crear equipo\n'
            '2. Fichar jugador\n'
            '3. Vender jugador\n'
            '4. Formacion del equipo\n'
            '5. Jugar partido\n'
            '6. Salir'
        )
        eleccion = int(input('>>> '))

        if eleccion == 1:
            crear_equipo()

        elif eleccion == 2:
            fichar_jugador()

        elif eleccion == 3:
            pass


def jugador():
    while True:
        print(
            '1. Ver estadisticas\n'
            '2. Entrenar\n'
            '3. Fichar por otro equipo\n'
            '4. Salir'
        )
        eleccion = int(input('>>> '))