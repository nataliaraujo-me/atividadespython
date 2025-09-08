#livros = ["Nós - Tamara Klink", "Garotas em Chamas - C. J. Tudor", "As Crônicas Marcianas - Ray Bradbury"]

#1
#print([livros])

#2
#print(f"[{livros[0]}, {livros[2]}]")

#3
#for i in range (2):
#    livro = str(input("Digite qual livro quer adicionar: "))
#    livros.append(livro)
#print([livros])

#4
#livros.insert(1, "Duna - Frank Hebert")
#print([livros])

#5
#if "Silêncio dos Inocentes" in livros:
#    livros.remove("Silêncio dos Inocentes")
#    print("Livro removido com sucesso!")
#else:
#    print("Livro não encontrado.")

#6
#numeros = [1, 2, 3, 2, 4, 2, 5]

#quantidade = numeros.count(2)
#print(f"O número {2} aparece {quantidade} vezes na lista.")

#7
#for i in range (len(livros)):
#    print(f"O livro {livros[i]} é interessante.")

#8
#idades = [12, 18, 25, 14, 30]

#for idade in (idades):
#    if idade >= 18:
#        print(f"{idade} faz parte das maiores idades.")

#9
#valores = [10, 20, 30, 40]

#for valor in (valores):
#    soma=(sum(valores))

#print(f"A soma de todos os itens da lista é {soma}")
    
#10

#notas=[]

#for i in range (2):
#    aluno_notas=[]
#    for n in range (3):
#        nota=float(input(f"Digite a nota {n+1} do aluno {i+1}: "))
#        aluno_notas.append(nota)
#        notas.append(aluno_notas)
        
#print(f"Notas: {nota}")

#for i, aluno_notas in enumerate(notas):
#    media = sum(aluno_notas)/len(aluno_notas)
#    print(f"A média do aluno {i+1} é: {media}")

#11
#tabuleiro = [["[]"for _ in range(8)] for _ in range(8)]

#pecas = ["tor", "cav", "bis", "rei", "rai", "bis", "cav", "tor"]

#tabuleiro[0] = pecas
#tabuleiro[1] = ["pea" for _ in range(8)]

#tabuleiro[6] = ["pea" for _ in range(8)]
#tabuleiro[7] = pecas

#for linha in tabuleiro:

#    print(linha)
