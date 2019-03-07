
#Proyecto dados José Alberto Martín Marí e Inés Golpe Martínez

#Funciones

def imprimir_dado(tirardado):
    if tirardado == 6:
        print("""

     |||||||||
     ||     ||
     ||     ||
     ||     ||
     ||     ||
     |||||||||""")

    elif tirardado == 5:

        print("""
     ||    //
     ||   //
     ||  //
     ||  \`
     ||   \`
     ||    \`""")

    elif tirardado == 4:

        print("""
     |||||||||
     ||     ||
     ||     ||
     ||   \` |
     ||    \`
     |||||||\` """)

    elif tirardado == 3:

        print("""

     ||||||||||
         |||
         |||
     ||  |||
     ||  |||
     |||||||""")

    elif tirardado == 2:
        print("""

     |||    |||
         ||
     |||    |||
         ||
     |||    ||| """)

    elif tirardado == 1:
        print("""

     |||    |||

     ||| || |||

     |||    ||| """)

def tirardado(numerodados,contadortirada):
    for i in range(numerodados):
        dado=random.randint(1,6)
        imprimir_dado(dado)
        dados.append(dado)
    return contadortirada+1

def seleccionardados(palo):
    for i in dados:
        if i==palo:
            puntuacion.append(i)

def tirada_ronda2(palo, jugador):
    contadortirada=0
    contadortirada=tirardado(5,contadortirada)
    while contadortirada<3:
        tirada=input("Vuelve a tirar los dados ")
        if dados.count(palo+1)==5:
            contadortirada=tirardado(5,contadortirada)
        else:
            contadortirada=tirardado(5-dados.count(palo+1), contadortirada)
    seleccionardados(palo+1)
    puntuar=puntuacion[:]
    totalporjugador[jugador].append(puntuar)
    del dados[:]
    del puntuacion[:]
        
def segundaronda():
    print ("""
        ===========================================
        |         EMPIEZA LA SEGUNDA RONDA        |
        |   VAIS A JUGAR UNA RONDA POR CADA PALO  |
        |                 ¡SUERTE!                |
        =========================================== """)

    for i in range(len(palos)):
        print ("Ahora juegas a %s, suerte! "%palos[i])
        for j in range(numerojugador):
            tirada=input("Le toca al jugador %s pulsa intro para tirar los dados "%jugadores[j])
            tirada_ronda2(i, j)

def totalizar_puntuacion(total):
    for i in range(len(total)):                             #i es el jugador
        puntuacionporjugador = 0
        for k in range(len(totalporjugador[i])):            #k son las rondas
            for j in range(len(totalporjugador[i][k])):     #j es la ronda concreta
                puntuacionporjugador+=totalporjugador[i][k][j]
        print ("""
            =============================================================
            |JUGADOR: %s                            PUNTUACIÓN : %d  |
            =============================================================""" %(jugadores[i],puntuacionporjugador))
      

#Listas y tuplas
jugadores=[]
dados=[]
totalizacion=[]
puntuacion=[]
totalporjugador=[]
palos=("Negras", "Rojas", "Jotas", "Reinas", "Reyes", "Ases")
letrasdados=("N","R","J","Q","K","As")

#Programa
import random
import msvcrt


print ("""
    =======================================================
    |      BIENVENIDO AL JUEGO DE LOS DADOS DE PÓKER      |
    =======================================================""")


numerojugador=int(input("¿Cuántos jugadores vais a ser? "))

for i in range(numerojugador):
    nombre=input("Dime tu nombre: ")
    jugadores.append(nombre)
    totalporjugador.append(i)
    totalporjugador[i] = []

for i in range(numerojugador):
    tirada=input("Le toca al jugador %s pulsa intro para tirar los dados " %jugadores[i])
    contadortirada=0
    contadortirada=tirardado(5,contadortirada)
    palo=input("¿A qué palo quieres jugar? ")
    palo=palo.capitalize()   #Por si se introduce el palo en minúscula (o con la primera letra en minúscula, en el caso del As)
    for j in range(len(letrasdados)):
        if palo==letrasdados[j]:
            palo=j+1
    while contadortirada<3:
        tirada=input("Vuelve a tirar los dados ")
        if dados.count(palo)==5:
            contadortirada=tirardado(5,contadortirada)
        else:
            contadortirada=tirardado(5-dados.count(palo), contadortirada)     
    seleccionardados(palo)
    puntuar=puntuacion[:]
    totalporjugador[i].append(puntuar)
    del dados[:]
    del puntuacion[:]


segundaronda()

totalizar_puntuacion(totalporjugador)

msvcrt.getch()           
       
                  
       
            
       
       
       
    
       
    



