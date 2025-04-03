def calculo_puntos(Jugador):    
    kills = Jugador["kills"] 
    assists = Jugador["assists"]
    deaths = int(Jugador["deaths"])
    return (kills*3) + assists - deaths

def procesar_ronda (ronda):
    puntuacion_max = -1
    for nick, stats in ronda.items():
        puntos = calculo_puntos(stats)
        stats["puntos"] += puntos
        if puntos > puntuacion_max:
            puntuacion_max = puntos
            mvp_ronda = nick
    if mvp_ronda:
        ronda[mvp_ronda]["mvp"] += 1
    print (mvp_ronda)
    return ronda

def agregar_campos (rondas):
    for ronda in rondas:
        for nick, stats in ronda.items():
            stats["puntos"] = 0
            stats["mvp"] = 0
    return rondas

# def sumatoria_datos(rondas):
#     resultado_final = {}
#     for ronda in rondas:
#         for nick, stats in ronda.items():
#             if nick not in resultado_final:
#                 resultado_final[nick] = {
#                     "kills": 0,
#                     "assists": 0,
#                     "deaths": 0,
#                     "puntos": 0,
#                     "mvp": 0
#                 }