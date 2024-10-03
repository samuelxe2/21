#Este es la primera version del 21 que se realizo aun tenia estados 
#que sirvio como base logica para la implementacion completa de la recursividad

import random

def carta (valor, palo):
    return (valor, palo)

def inicializar_baraja():
    return [carta(v,p) for v in ['As',2,3,4,5,6,7,8,9,10,10,10,10] for p in ['D','C','T','P']]

def barajar(baraja):
    return random.sample(baraja, len(baraja))

def repartir_mano(baraja):
    return (baraja[0], baraja[1]), baraja[2:]

def calcular_puntuacion(mano):
    total = 0
    num_as = 0

    for carta in mano:
        valor, palo = carta
        if valor == 'As':
            total += 1
            num_as += 1
        else:
            total += valor
    
    while total <= 11 and num_as > 0:
        total += 10
        num_as -= 1
        
    return total

def turno_jugador(baraja, mano_jugador):
    if calcular_puntuacion(mano_jugador) >= 21:
        return mano_jugador, baraja
    decision = input(f"Tu mano: {mano_jugador} - Puntuación: {calcular_puntuacion(mano_jugador)}. ¿Quieres otra carta? (s/n): ")
    if decision == 's':
        nueva_mano_jugador = mano_jugador + (baraja[0],)
        return turno_jugador(baraja[1:], nueva_mano_jugador)
    else:
        return mano_jugador, baraja

def turno_dealer(baraja, mano_dealer):
    if calcular_puntuacion(mano_dealer) < 17:
        nueva_mano_dealer = mano_dealer + (baraja[0],)
        return turno_dealer(baraja[1:], nueva_mano_dealer)
    else:
        return mano_dealer, baraja

def determinar_ganador(mano_jugador, mano_dealer):
    puntuacion_jugador = calcular_puntuacion(mano_jugador)
    puntuacion_dealer = calcular_puntuacion(mano_dealer)
    if puntuacion_jugador > 21:
        return "Gana el Dealer"
    elif puntuacion_dealer > 21 or puntuacion_jugador > puntuacion_dealer:
        return "Gana el Jugador"
    elif puntuacion_jugador == puntuacion_dealer:
        return "Empate"
    else:
        return "Gana el Dealer"

def juego():
    baraja = barajar(inicializar_baraja())
    mano_jugador, baraja = repartir_mano(baraja)
    mano_dealer, baraja = repartir_mano(baraja)

    mano_jugador, baraja = turno_jugador(baraja, mano_jugador)
    if calcular_puntuacion(mano_jugador) <= 21:
        mano_dealer, baraja = turno_dealer(baraja, mano_dealer)

    print(f"Mano del jugador: {mano_jugador} - Puntuación: {calcular_puntuacion(mano_jugador)}")
    print(f"Mano del Dealer: {mano_dealer} - Puntuación: {calcular_puntuacion(mano_dealer)}")
    print(determinar_ganador(mano_jugador, mano_dealer))

if __name__ == "__main__":
    juego()
