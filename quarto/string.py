#contagem de palavras 

tipos_frutas = "banana maçã banana morango maçã uva jambo maçã carambola uva jambo"

def fruteira(tipos_frutas):
    frutas = tipos_frutas.split()

    contagem = {}

    for fruta in set(frutas):
        contagem[fruta] = frutas.count(fruta)
    
    return contagem

resultado = fruteira(tipos_frutas)

print(resultado)
print('-' * 50)