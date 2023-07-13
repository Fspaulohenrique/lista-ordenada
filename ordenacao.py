import time

# Função para ordenar a lista utilizando o algoritmo de insertion sort
def insertion_sort(lista, ordem):
    # Loop para percorrer toda a lista
    for i in range(1, len(lista)):
        # Armazena o valor do elemento atual
        atual = lista[i]
        j = i - 1
        # Move os elementos maiores do que o elemento atual uma posição para a frente
        while j >= 0 and ((ordem == "crescente" and atual < lista[j]) or (ordem == "decrescente" and atual > lista[j])):
            lista[j + 1] = lista[j]
            j -= 1
        # Insere o elemento atual na posição correta
        lista[j + 1] = atual
    # Retorna a lista ordenada
    return lista

# Função para imprimir a lista original e a lista ordenada
def imprimir_listas(lista_entrada, lista_ordenada):
    print("Lista original, não ordenada: ", lista_entrada)
    print("Lista ordenada: ", lista_ordenada)

# Mensagem de boas-vindas ao programa
print("Bem-vindo ao programa de ordenação de listas!")
print("Por favor, siga as instruções para obter uma lista ordenada.")

# Loop para obter a lista de entrada do usuário
while True:
    lista_numeros = input("Insira a lista de números separados por vírgula ou espaço: ")
    # Verifica se a lista contém apenas números
    try:
        lista_numeros = [int(num) for num in lista_numeros.replace(",", " ").split()]
        break
    except ValueError:
        print("A lista deve conter apenas números separados por vírgula ou espaço.")

# Loop para obter a ordem de ordenação do usuário
while True:
    opcao = input("Deseja ordenar em ordem crescente ou decrescente? (c/d): ")
    if opcao.lower() == "c":
        lista_ordenada = insertion_sort(lista_numeros, ordem="crescente")
        break
    elif opcao.lower() == "d":
        lista_ordenada = insertion_sort(lista_numeros, ordem="decrescente")
        break
    else:
        print("Opção inválida. Insira 'c' ou 'd'.")

# Imprime as listas original e ordenada
imprimir_listas(lista_numeros, lista_ordenada)

# Calcula o tempo de execução do algoritmo de ordenação
inicio = time.time()
insertion_sort(lista_numeros, ordem="crescente")
fim = time.time()

# Imprime o tempo de execução do algoritmo de ordenação
print(f"Tempo de execução do algoritmo: {fim - inicio:.5f} segundos.")

# Mensagem de despedida
print("Obrigado por usar o programa de ordenação de listas. Até a próxima!")

