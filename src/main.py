import funciones

rounds = [
 {
 'Shadow': {'kills': 2, 'assists': 1, 'deaths': True},
 'Blaze': {'kills': 1, 'assists': 0, 'deaths': False},
 'Viper': {'kills': 1, 'assists': 2, 'deaths': True},
 'Frost': {'kills': 0, 'assists': 1, 'deaths': False},
 'Reaper': {'kills': 1, 'assists': 1, 'deaths': False}
 },
 {
 'Shadow': {'kills': 0, 'assists': 2, 'deaths': False},
 'Blaze': {'kills': 2, 'assists': 0, 'deaths': True},
 'Viper': {'kills': 1, 'assists': 1, 'deaths': False},
 'Frost': {'kills': 2, 'assists': 1, 'deaths': True},
 'Reaper': {'kills': 0, 'assists': 1, 'deaths': False}
 },
 {
 'Shadow': {'kills': 1, 'assists': 0, 'deaths': False},
 'Blaze': {'kills': 2, 'assists': 2, 'deaths': True},
 'Viper': {'kills': 1, 'assists': 1, 'deaths': True},
 'Frost': {'kills': 0, 'assists': 1, 'deaths': False},
 'Reaper': {'kills': 1, 'assists': 1, 'deaths': False}
 },
 {
 'Shadow': {'kills': 2, 'assists': 1, 'deaths': False},
 'Blaze': {'kills': 1, 'assists': 0, 'deaths': True},
 'Viper': {'kills': 0, 'assists': 2, 'deaths': False},
 'Frost': {'kills': 1, 'assists': 1, 'deaths': True},
 'Reaper': {'kills': 1, 'assists': 1, 'deaths': False}
 },
 {
 'Shadow': {'kills': 1, 'assists': 2, 'deaths': True},
 'Blaze': {'kills': 0, 'assists': 1, 'deaths': False},
 'Viper': {'kills': 2, 'assists': 0, 'deaths': True},
 'Frost': {'kills': 1, 'assists': 1, 'deaths': False},
 'Reaper': {'kills': 1, 'assists': 1, 'deaths': True}
 }
 ]

rondas = rounds.copy()
mvps = {}

def mvp (ronda):
    puntuacion_max = -1
    for nick, stats in ronda.items():
        puntos = funciones.calculo_puntos(stats)
        if puntos > puntuacion_max:
            puntuacion_max = puntos
            mvp = nick
    if mvp in mvps:
        mvps[mvp] += 1 
    else:
        mvps[mvp] = 1
    return mvps

def simulacion_rondas(rondas):
    for i in rondas:
        mvps = mvp(i)
    for i in mvps:
        print(i)

print(simulacion_rondas(rondas))

# def mvp2 (ronda):
#     puntuacion_max = -1
#     for nick, stats in ronda.items():
#         stats["puntos"] = calculo_puntos(stats)
#     # 2️⃣ Ordenar el diccionario de la ronda según los puntos (de mayor a menor)
#     ronda_ordenada = dict(sorted(ronda.items(), key=lambda item: item[1]["puntos"], reverse=True))
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