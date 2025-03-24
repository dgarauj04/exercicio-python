print("-"*50)

lista_nome = [("Douglas", 18), ("Samuel", 22), ("Karine", 22), ("João", 25), ("Joy", 20), ("Kleber", 28), ("Carol", 26)]

def ordenar_lista(lista_nome):
    lista_ordenada = sorted(lista_nome, key=lambda x: x[1])
    return lista_ordenada

print(ordenar_lista(lista_nome))

print("-"*50)
