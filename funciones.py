import random


def crear_equipo():
    nombre_equipo = input('Nombra a tu equipo: ')
    print('El nombre de tu equipo es:', nombre_equipo)


def comprar_vender_jugador():
    nombre_dt = input('Escribe tu nombre de director tecnico: ')
    print('Hola {} , tienes $120 millones de dolares para crear tu equipo .' \
          "podes comprar 11 jugadores ".format(nombre_dt))

    cartera = 120
    jugadores = {'hart': 20, 'curtois': 18, 'navas': 20, 'bravo': 15, 'cech': 15, 'de gea': 20, 'ramos': 40,
                 'pique': 30, 'ronaldo': 50,
                 'messi': 50, 'suarez': 45, 'neymar': 48, 'bale': 45, 'hazard': 42, 'aguero': 40, 'smith': 2,
                 'johhny': 4, 'sunny': 8, 'patrick': 5,
                 'debian': 3, 'shaggy': 4.5, 'randy': 3, 'karim': 6, 'samuel': 2, 'billy': 4, "aaron": 5}
    equipo = []

    for key, precio in jugadores.items():
        print("Nombre: {} precio: {} Millones de dolares".format(key, precio))

    while len(equipo) < 11:
        comprar_jugador = input('Nombre del jugador a comprar: ')
        if comprar_jugador in equipo:
            print(comprar_jugador + " ya esta en tu equipo")
            continue
        if comprar_jugador not in jugadores:
            print('Este jugador no se puede comprar, chequea la lista de nuevo')
            continue
        print("Jugador: {} Precio: {} Millones de dolares; {}'s Cartera: {} Millon de dolares".format(comprar_jugador,
                                                                                                      jugadores[
                                                                                                          comprar_jugador],
                                                                                                      nombre_dt,
                                                                                                      cartera))
        respuesta_final = input('Estas seguro de hacer esta compra? (si o no) , no puedes volver atras; ')
        if respuesta_final.lower() != "si":
            continue
        if cartera - jugadores[comprar_jugador] <= 0:
            print("insuficiente saldo")
            respuesta_vender = input('Necesitas vender un jugador , escribe el nombre del jugador a vender')
            if respuesta_vender not in equipo:
                continue
            print("{} ,  Precio: {} Millones de dolares.Sold ".format(respuesta_vender, jugadores[comprar_jugador]))
            equipo.remove(respuesta_vender)
            cartera += jugadores[respuesta_vender]
            print("{} este es tu nuevo dinero".format(cartera))
            print("Tienes {} jugadores en tu equipo".format(str(len(equipo))))
            continue
        cartera -= jugadores[comprar_jugador]
        equipo.append(comprar_jugador)
        print("Tienes {} jugadores en tu equipo".format(str(len(equipo))))

    print("\n".join(equipo))
    print('Este es tu nuevo equipo!')


def formacion_equipo():
    formaciones = {'4-4-2': 0, '4-3-1-2': 1, '4-3-3': 2, '4-2-3-1': 3, '3-5-2': 4, '3-4-3': 5, '5-4-1': 6,
                   '5-3-2': 7}
    equipo = []

    for key, numero in formaciones.items():
        print("Nombre de la formacion: {}, numero: {}".format(key, numero))

    while len(equipo) < 1:
        formacion = input('Nombre de la formacion: ')
        if formacion in equipo:
            print(formacion + " ya la tiene el equipo")
            continue
        if formacion not in formaciones:
            print('Esta formacion no existe, chequea la lista de nuevo')
            continue
        respuesta_final = input('Estas seguro de elegir esta formacion? (si o no): ')
        if respuesta_final.lower() != "si":
            continue
        equipo.append(formacion)
        print("Tu formacion es", formacion)


def jugar_partido():
    elige = ["Ganaste", "Perdiste"]
    aleatorio = random.choice(elige)
    print(aleatorio)
    if aleatorio == "Ganaste":
        print("+3pts")
    elif aleatorio == "Perdiste":
        print("-3pts")


def ver_estadisticas(estadisticas, estadistica="All"):
    print("Tus estadisticas son: ")
    if estadistica == "All":
        for est, val in estadisticas.items():
            print(est, ": ", val)
    else:
        print(estadistica, ": ", estadisticas[estadistica])


def entrenar(estadisticas, estadistica="All"):
    if estadistica == "All":
        for est in estadisticas.keys():
            estadisticas[est] = random.randint(0, 99)
    else:
        estadisticas[estadistica] = random.randint(0, 99)
    ver_estadisticas(estadisticas)


def fichar_por_equipo():
    equipos = {"Boca": 0, "Riber": 1, "Chacarita": 2, "Talleres": 3, "Belgrano": 4}
    for key, numeros in equipos.items():
        print("Nombre: {} numero: {} ".format(key, numeros))
    equipo = []
    while len(equipo) < 1:
        equipo_f = input('Nombre del equipo a cambiar: ')
        if equipo_f not in equipos:
            print('Este equipo no existe, chequea la lista de nuevo')
            continue
        respuesta_final = input('Estas seguro de elegir este equipo? (si o no): ')
        if respuesta_final.lower() != "si":
            continue
        equipo.append(equipo)
        print("Tu equipo nuevo es", equipo_f)


def equipo_aleatorio():
    equipos = ["Boca", "Riber", "Chacarita", "Talleres", "Belgrano", ]
    equipo = random.choice(equipos)
    print("Tu equipo es", equipo)
