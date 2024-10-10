import math  # Importa el módulo math para usar valores como infinito (inf) en el algoritmo Minimax

# Definir los jugadores
HUMANO = -1  # El jugador humano se representa con -1
COMPUTADORA = 1  # La computadora se representa con 1

# Crear el tablero vacío, representado por una matriz de 3x3 donde los ceros indican casillas vacías
tablero = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]
]

# Función para verificar si un jugador ha ganado
def ganador(tablero, jugador):
    # Define todas las combinaciones posibles para ganar (filas, columnas y diagonales)
    win_state = [
        [tablero[0][0], tablero[0][1], tablero[0][2]],  # Primera fila
        [tablero[1][0], tablero[1][1], tablero[1][2]],  # Segunda fila
        [tablero[2][0], tablero[2][1], tablero[2][2]],  # Tercera fila
        [tablero[0][0], tablero[1][0], tablero[2][0]],  # Primera columna
        [tablero[0][1], tablero[1][1], tablero[2][1]],  # Segunda columna
        [tablero[0][2], tablero[1][2], tablero[2][2]],  # Tercera columna
        [tablero[0][0], tablero[1][1], tablero[2][2]],  # Diagonal principal
        [tablero[2][0], tablero[1][1], tablero[0][2]],  # Diagonal secundaria
    ]
    # Si el jugador tiene tres en línea en cualquiera de las combinaciones, retorna True
    return [jugador, jugador, jugador] in win_state

# Función para verificar si todas las casillas están ocupadas (tablero lleno)
def tablero_lleno(tablero):
    # Recorre cada fila del tablero
    for fila in tablero:
        # Si encuentra un 0, significa que hay una casilla vacía, por lo tanto el tablero no está lleno
        if 0 in fila:
            return False
    return True  # Si no encuentra ceros, el tablero está lleno

# Función para evaluar el estado actual del tablero
def evaluar(tablero):
    if ganador(tablero, COMPUTADORA):
        return 1  # Retorna 1 si la computadora gana
    elif ganador(tablero, HUMANO):
        return -1  # Retorna -1 si el humano gana
    else:
        return 0  # Retorna 0 si no hay ganador aún

# Algoritmo Minimax para encontrar el mejor movimiento posible
def minimax(tablero, profundidad, jugador):
    # Verifica si hay un ganador
    if ganador(tablero, COMPUTADORA):
        return 1  # Retorna 1 si la computadora ha ganado
    if ganador(tablero, HUMANO):
        return -1  # Retorna -1 si el humano ha ganado
    if tablero_lleno(tablero):
        return 0  # Retorna 0 si el tablero está lleno y no hay ganador (empate)

    # Si es el turno de la computadora (jugador = 1), busca maximizar el puntaje
    if jugador == COMPUTADORA:
        mejor = -math.inf  # Inicializa el mejor puntaje como menos infinito
        # Recorre el tablero en busca de posibles movimientos
        for i in range(3):
            for j in range(3):
                if tablero[i][j] == 0:  # Si la casilla está vacía
                    tablero[i][j] = COMPUTADORA  # Simula el movimiento de la computadora
                    mejor = max(mejor, minimax(tablero, profundidad + 1, HUMANO))  # Llama recursivamente a minimax
                    tablero[i][j] = 0  # Deshace el movimiento (backtracking)
        return mejor
    # Si es el turno del humano (jugador = -1), busca minimizar el puntaje
    else:
        peor = math.inf  # Inicializa el peor puntaje como infinito
        for i in range(3):
            for j in range(3):
                if tablero[i][j] == 0:  # Si la casilla está vacía
                    tablero[i][j] = HUMANO  # Simula el movimiento del humano
                    peor = min(peor, minimax(tablero, profundidad + 1, COMPUTADORA))  # Llama recursivamente a minimax
                    tablero[i][j] = 0  # Deshace el movimiento (backtracking)
        return peor

# Función que determina el mejor movimiento de la computadora usando Minimax
def movimiento_computadora(tablero):
    mejor_movimiento = None
    mejor_valor = -math.inf  # Inicializa el mejor valor como menos infinito
    # Recorre todas las casillas del tablero
    for i in range(3):
        for j in range(3):
            if tablero[i][j] == 0:  # Si la casilla está vacía
                tablero[i][j] = COMPUTADORA  # Simula el movimiento de la computadora
                valor = minimax(tablero, 0, HUMANO)  # Evalúa el valor de este movimiento
                tablero[i][j] = 0  # Deshace el movimiento
                if valor > mejor_valor:  # Si el valor es mejor que el mejor valor actual
                    mejor_valor = valor  # Actualiza el mejor valor
                    mejor_movimiento = (i, j)  # Guarda el mejor movimiento
    return mejor_movimiento  # Retorna el mejor movimiento

# Función para imprimir el estado actual del tablero
def imprimir_tablero(tablero):
    for fila in tablero:
        print(fila)  # Imprime cada fila del tablero

# Función principal que simula el juego
def juego():
    while True:
        imprimir_tablero(tablero)  # Imprime el tablero en cada turno
        if tablero_lleno(tablero):  # Si el tablero está lleno, es un empate
            print("Empate!")
            break

        # Movimiento del humano
        fila = int(input("Introduce la fila (0, 1, 2): "))  # Solicita la fila del movimiento
        col = int(input("Introduce la columna (0, 1, 2): "))  # Solicita la columna del movimiento
        if tablero[fila][col] == 0:  # Verifica si la casilla está vacía
            tablero[fila][col] = HUMANO  # Asigna el movimiento del humano
        else:
            print("Movimiento no válido, intenta de nuevo.")  # Si la casilla está ocupada, pide otra entrada
            continue

        if ganador(tablero, HUMANO):  # Verifica si el humano ha ganado
            imprimir_tablero(tablero)
            print("¡Has ganado!")
            break

        # Movimiento de la computadora
        movimiento = movimiento_computadora(tablero)  # Calcula el mejor movimiento de la computadora
        tablero[movimiento[0]][movimiento[1]] = COMPUTADORA  # Realiza el movimiento

        if ganador(tablero, COMPUTADORA):  # Verifica si la computadora ha ganado
            imprimir_tablero(tablero)
            print("La computadora ha ganado.")
            break

# Iniciar el juego
juego()  # Llama a la función principal para comenzar el juego
