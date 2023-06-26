import generador
import time
import os
from actores import Jugador, Enemigo, Bala
import random 
   
if __name__ == "__main__":    
    generadorDeEscenarios = generador.GeneradorDeEscenarios()
    jugador = Jugador(columna=2)
    enemigo = Enemigo(columna=5)
    balaEnemiga = Bala(enemigo.x,enemigo.y+1)
    balaJugador = Bala(jugador.x,jugador.y-1)

    while True:
        os.system("cls")
        escenario = generadorDeEscenarios.generarEscenario()
        jugador.pintar(escenario)
        enemigo.pintar(escenario)
        
        if balaEnemiga.estaEnEspera() == True:
            decision = random.choice([True,False])
            if decision == True:
                balaEnemiga.disparar(enemigo, 1)
        if balaEnemiga.estaEnEspera() == False:
            balaEnemiga.pintar(escenario)
        if balaJugador.estaEnEspera() == True:
            decision = random.choice([True,False])
            if decision == True:
                balaJugador.disparar(jugador, -1)
        if balaJugador.estaEnEspera() == False:
            balaJugador.pintar(escenario)

        # Dibujar escena 
        for fila in escenario:
            for columna in fila:
                print(columna, end="")
            print()
        # La bala enemiga esta en pocision del jugador
        # la bala jugador esta en pocision del enemigo
        # EMPATE
        if balaEnemiga.x == jugador.x and balaEnemiga.y == jugador.y and balaJugador.x == enemigo.x and balaJugador.y == enemigo.y:
            print("Fin del juego")
            input ("Has empatado")
        # La bala enemiga esta en pocision del jugador
        elif balaEnemiga.x == jugador.x and balaEnemiga.y == jugador.y:
            print("Fin del juego")
            input ("Has perdido")
            
        # La bala enemiga esta en pocision del jugador
        elif balaJugador.x == enemigo.x and balaJugador.y == enemigo.y:
            print("Fin del juego")
            input ("Has ganado")
            

        time.sleep(0.003)
        jugador.mover()
        enemigo.mover()
        balaEnemiga.mover()
        balaJugador.mover()
        