from funciones import crear_equipo
from funciones import comprar_vender_jugador
from funciones import formacion_equipo
from funciones import jugar_partido
from funciones import ver_estadisticas
from funciones import entrenar
from funciones import fichar_por_equipo
from funciones import equipo_aleatorio
lista_equipos = []
jugador_fichado = []
estadisticas = {
    "Fuerza": 0,
    "Aceleracion": 0,
    "Resistencia": 0,
    "Equilibrio": 0,
    "Velocidad": 0,
    "Salto": 0,
}

print('Hola bienvenido/a Futbol Manager!')
print('Elige que quieres ser:')
while True:
    print(
        '1. Director Tecnico\n'
        '2. Jugador'
        )
    eleccion = int(input('>>> '))

    if eleccion == 1:
        while True:
            print(
                '1. Crear equipo\n'
                '2. Comprar/vender jugador\n'
                '3. Formacion del equipo\n'
                '4. Jugar partido\n'
                '5. Salir'
            )
            eleccion = int(input('>>> '))

            if eleccion == 1:
                crear_equipo()

            elif eleccion == 2:
                comprar_vender_jugador()

            elif eleccion == 3:
                formacion_equipo()

            elif eleccion == 4:
                jugar_partido()

            elif eleccion == 5:
                break

    elif eleccion == 2:
        equipo_aleatorio()
        while True:
            print(
                '1. Ver estadisticas\n'
                '2. Entrenar\n'
                '3. Fichar por otro equipo\n'
                '4. Salir'
            )
            eleccion = int(input('>>> '))

            if eleccion == 1:
                ver_estadisticas(estadisticas)

            elif eleccion == 2:
                entrenar(estadisticas)

            elif eleccion == 3:
                fichar_por_equipo()

            elif eleccion == 4:
                break