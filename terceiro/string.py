#contagem de palavras 

ferramentas = ['Java', 'Python', 'Java', 'SQL', 'Java', 'JavaScript', 'Ruby', 'SQL', 'Python']

def programacao(ferramentas):
    contagem = {}  

    for ferramenta in set(ferramentas):  
        contagem[ferramenta] = ferramentas.count(ferramenta) 

    return contagem

resultado = programacao(ferramentas)

print(resultado)
print('-' * 50)
