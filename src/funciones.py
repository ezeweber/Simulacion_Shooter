def agregar_campos (rondas):
    for ronda in rondas:
        for nick, stats in ronda.items():
            stats["puntos"] = 0
            stats["mvp"] = 0
    return rondas

def calculo_puntos(Jugador):    
    kills = Jugador["kills"] 
    assists = Jugador["assists"]
    deaths = int(Jugador["deaths"])
    return (kills*3) + assists - deaths

def mvp_puntos (ronda):
    puntuacion_max = -1
    for nick, stats in ronda.items():
        puntos = calculo_puntos(stats)
        stats["puntos"] += puntos
        if puntos > puntuacion_max:
            puntuacion_max = puntos
            mvp_ronda = nick
    if mvp_ronda:
        ronda[mvp_ronda]["mvp"] += 1
    return ronda

def procesar_datos(rondas):
    ranking = {}
    for i, ronda in enumerate(rondas,start=1):
        for nick, stats in ronda.items():
            if nick not in ranking:
                ranking[nick] = {"kills": 0, "assists": 0, "deaths": 0, "puntos": 0, "mvp": 0}
            ranking[nick]["kills"] += stats["kills"]
            ranking[nick]["assists"] += stats["assists"]
            ranking[nick]["deaths"] += int(stats["deaths"])
            ranking[nick]["puntos"] += stats["puntos"]
            ranking[nick]["mvp"] += stats["mvp"]
        # ranking_lista = list(ranking.items())
        # print(ranking_lista)
        # ranking_lista.sort(reverse=True, key=[stats]["puntos"])
        # ranking = dict(ranking_lista)
        ranking = dict(sorted(ranking.items(), key=lambda item: item[1]["puntos"], reverse=True))
        imprimir_rondas(ranking, i,rondas)
    return ranking

def simulacion_rondas(rondas):
    for ronda in rondas:
        mvp_puntos(ronda) # calcula y almacena el puntaje en los campos nuevos para luego
    procesar_datos(rondas) # procesar los datos y hacer la simulacion de la partida

def imprimir_rondas(ranking, ronda_act, rondas):
    print(f"Ranking ronda {ronda_act}:\n") if ronda_act < len(rondas) else print("Ranking final:\n")
    print(f"{'Jugador':<12} {'Kills':>7} {'Asistencias':>12} {'Muertes':>9} {'MVPs':>6} {'Puntos':>8}")
    print('-' * 60)
    for nick, stats in ranking.items():
        print(f"{nick:<12} {stats['kills']:>7} {stats['assists']:>12} {stats['deaths']:>9} {stats['mvp']:>6} {stats['puntos']:>8}")
    print("-" * 60)