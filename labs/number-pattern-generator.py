def number_pattern(n):
    # Controllo che il tipo sia intero (escludendo i booleani, che in Python sono sottoclasse di int)
    if not isinstance(n, int) or isinstance(n, bool):
        return "Argument must be an integer value."
    
    # Controllo che l'intero sia maggiore di 0
    if n < 1:
        return "Argument must be an integer greater than 0."
    
    result = ""
    # Ciclo for da 1 a n inclusi
    for i in range(1, n + 1):
        if result == "":
            result = str(i)
        else:
            result += " " + str(i)
            
    return result