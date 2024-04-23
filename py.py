notas = []

contador = 1

while contador <= 5:
    codigo_aluno = input("RM: ")
    nota = float(input("Nota: "))
    resultado = [codigo_aluno, nota]
    notas.append(resultado)

    contador = contador+1

print ("quant notas", len(notas))
#usa o terminal com: python nomedoarquivo.py