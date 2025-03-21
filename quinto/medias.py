#medias de notas

alunos = {
  "Wesley": [8, 7, 9],
  "Vinicius JR": [10, 7, 7], 
  "Mikaela": [6, 7, 5], 
  "Sarah": [10, 9, 8], 
  "Gerson": [5, 9, 7] 
}

def boletim(alunos):
    media = {}

    for nome, notas in alunos.items():
        media[nome] = sum(notas) / len(notas)

    return list(media.items())

resultado = boletim(alunos)

print(resultado)
print("-" * 50)