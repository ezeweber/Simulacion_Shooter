def calculo_puntos(Jugador):    
    kills = Jugador["kills"] 
    assists = Jugador["assists"]
    deaths = int(Jugador["deaths"])
    return (kills*3) + assists - deaths


def reiniciando_variables (puntos,kills,asistencias,muertes,mvps):
    puntos = 0
    kills = 0
    asistencias = 0
    muertes = 0
    mvps = 0

def recorrer_ordenando (jugador,lista):
    for i in lista:
        # reiniciando_variables(puntos,kills,asistencias,muertes,mvps)
        actual = i
        print(actual)
        # actual.split(puntos,kills,asistencias,muertes,mvps)
        print(actual)


def ejercicio10(rounds):
    for i in rounds:
        ranking_ronda = []
        jugador = {}
        for y in range(4):
            recorrer_ordenando(jugador,ranking_ronda)
