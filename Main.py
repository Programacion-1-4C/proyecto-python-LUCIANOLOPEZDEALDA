from Funciones import director_tecnico
from Funciones import jugador

lista_equipos = []
jugador_fichado = []

print('Hola bienvenido/a Futbol Manager!')
print('Elige que quieres ser:')
while True:
    print(
        '1. Director Tecnico\n'
        '2. Jugador'
        )
    eleccion = int(input('>>> '))

    if eleccion == 1:
        director_tecnico()

    elif eleccion == 2:
        jugador()