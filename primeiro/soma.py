#soma dos numeros pares
print("-"*50)
def calcular_pares(lista):
    resultado = 0
    for numero in lista:
        if numero %2 == 0:
            resultado += numero
    
    return resultado

lista = [2, 4, 10, 3, 9, 7, 15, 22]
print('A soma dos pares é:', calcular_pares(lista))

print("-"*50)