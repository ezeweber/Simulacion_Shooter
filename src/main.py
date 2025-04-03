import funciones


def ejercicio10(rounds):
    for i in rounds:
        ranking_ronda = []
        jugador = {}
        for y in range(4):
            recorrer_ordenando(jugador,ranking_ronda)

def calculo_puntos(Jugador):    
    kills = Jugador["kills"] 
    assists = Jugador["assists"]
    deaths = int(Jugador["deaths"])
    return (kills*3) + assists - deaths
    
def mvp (ronda):
    puntuacion_max = -1
    for nick, stats in ronda.items():
        puntos = calculo_puntos(stats)
        if puntos > puntuacion_max:
            puntuacion_max = puntos
            mvp = nick
    if mvp in mvps:
        mvps[mvp] += 1 
    else:
        mvps[mvp] = 1
    return mvp

def mvp2 (ronda):
    puntuacion_max = -1
    for nick, stats in ronda.items():
        stats["puntos"] = calculo_puntos(stats)
    # 2️⃣ Ordenar el diccionario de la ronda según los puntos (de mayor a menor)
    ronda_ordenada = dict(sorted(ronda.items(), key=lambda item: item[1]["puntos"], reverse=True))
    



# def score (ronda):
#     puntuaciones = []
#     puntuacion_max = -1
#     for nick, stats in ronda.items():
#         if calculo_puntos(stats) > puntuacion_max:
#             score_ordenado[1] = ronda.items
#         else:      
# for i in rounds:
#     # tomo el diccionario de la primer ronda
#     print (mvp(i))
#     # imprimir en orden de puntos, ronda a ronda el score
#     score(i)
# for i in rondas: