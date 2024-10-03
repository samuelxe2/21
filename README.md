# BlackJack Recursivo - Modelos de Programación II

Universidad Distrital Francisco José de Caldas  
Proyecto Curricular de Ingeniería de Sistemas

**Asignatura:** Modelos de Programación II  
**Profesor:** Alejandro Paolo Daza Corredor

---

## Integrantes

- Amir Zoleyt Vanegas Cárdenas - 20211020015 <br> azvanegasc@udistrital.edu.co
- Esteban Alejandro Villalba Delgadillo - 20212020064 <br> eavillalbad@udistrital.edu.co
- Samuel Antonio Sanchez Peña - 20212020151 <br> samasanchezp@udistrital.edu.co

---

## Descripción del Proyecto

Este proyecto consiste en la implementación de un juego de Blackjack utilizando exclusivamente técnicas de recursividad. En lugar de usar variables para mantener los estados, el flujo del juego y los cambios en el estado de la partida se gestionan mediante funciones que se llaman entre sí de manera recursiva. De esta manera, se evita el uso de estados mutables y se aplica una estructura puramente funcional.

El objetivo principal es simular una partida completa de Blackjack, donde el jugador puede tomar decisiones como pedir una carta, quedarse, o verificar el resultado del juego, todo en un flujo recursivo y funcional.

### Objetivos

- Implementar un juego de Blackjack utilizando únicamente funciones recursivas para manejar la lógica del juego.

- Profundizar en el entendimiento de la recursividad y la programación funcional, aplicándolos a un problema práctico.

## Características del proyecto

El juego está diseñado de manera que toda la lógica del Blackjack, desde la repartición de cartas hasta la evaluación de la mano del jugador, es gestionada sin ninguna variable externa. El flujo del programa depende completamente de las funciones que se llaman entre sí, garantizando un modelo puramente funcional y recursivo.

El jugador puede tomar decisiones como:

- Cuánto apostar.
- Pedir cartas adicionales (Hit) o quedarse (Stand).
- Dividir su mano (Split).
- Verificar el resultado final de su mano en comparación con la del dealer.

*Recursión Pura: La lógica de juego, incluyendo la decisión del jugador, está estructurada completamente mediante funciones recursivas.
Funciones como estructura: No hay variables o bucles, lo que refuerza el uso de la programación funcional y el manejo de la memoria a través de la recursividad.*

*blackjack.py esta ubicado el codigo final pero sin particiones*

![Diagrama de Secuencia](https://github.com/samuelxe2/21/blob/master/diagramas/diagrama21.png)
### Instrucciones de ejecución

Para ejecutar el proyecto, primero debe verificar que tenga instalando Python en su sistema Operativo; preferiblemente una versión 3.10 o mayor.

Estas son las siguientes instrucciones para ejecutar el proyecto:

1. **Clonar el repositorio:**
```bash
   git clone https://https://github.com/samuelxe2/21
```

2. **Navega al directorio del repositorio clonado:**
```bash
   cd 21
```

3. **Ejecutar el main:**
```bash
   python main.py
```

---