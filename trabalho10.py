def two_sum(numeros, alvo):
    # mapeia cada valor ao seu índice em `numeros`  
    mapa = {}  

    for i, valor_atual in enumerate(numeros):
        mapa[valor_atual] = i
    
    for i, valor_atual in enumerate(numeros):
        numero_desejado = alvo - valor_atual
        if numero_desejado in mapa:
            return [i, mapa[numero_desejado]]

    return []       

if __name__ == "__main__":
    numeros = [2, 7, 11, 15]
    alvo = 9
    resultado = two_sum(numeros, alvo)
    print(resultado)