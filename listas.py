# Criar uma lista a partir da outra com somente os numeros pares
# lista original
lista_completa = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# lista so com os numeros pares
lista_pares = [x for x in lista_completa if x % 2 == 0]

print(lista_pares)

# Criar uma lista a partir da outra com palavras terminadas em a
# lista orginal
nomes = ['joao', 'felipe', 'marcos', 'renan', 'carla', 'ana']

# lista com os nomes terminados em a
nomes_final_a = [x for x in nomes if x[-1] == 'a']

print(nomes_final_a)
