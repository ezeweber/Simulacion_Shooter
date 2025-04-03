def calculo_puntos(Jugador):
    kills = "kills"
    for i in kills:
        kills=i
    assists = "assists"
    for i in assists:
        assists = i
    deaths = "deaths"
    for i in deaths:
        deaths = i
    return kills + assists + deaths

def mvp (ronda):
    puntuacion = 0
    for nick in ronda:
        if calculo_puntos(ronda[nick]) > puntuacion:
            mvp = nick
        




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