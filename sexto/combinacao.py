d1 = {"a": 2, "b": 3, "c": 5}
d2 = {"a": 1, "b": 4, "d": 7}

def combinacao(valores):
  valores = {d1, d2}
  soma = {}

for letra, valor in valores.items():
        soma[letra] = sum(valor)

    return list(soma.items())

resultado = boletim(alunos)
