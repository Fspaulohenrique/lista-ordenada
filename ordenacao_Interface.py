import tkinter as tk
import time

def insertion_sort(lista, ordem):
    for i in range(1, len(lista)):
        atual = lista[i]
        j = i - 1
        while j >= 0 and ((ordem == "crescente" and atual < lista[j]) or (ordem == "decrescente" and atual > lista[j])):
            lista[j + 1] = lista[j]
            j -= 1
        lista[j + 1] = atual
    return lista

def ordenar():
    entrada = entrada_lista.get()
    ordem = var_ordem.get()
    try:
        lista_numeros = [int(num) for num in entrada.replace(",", " ").split()]
        lista_ordenada = insertion_sort(lista_numeros.copy(), ordem=ordem)
        texto_saida.config(state='normal')
        texto_saida.delete('1.0', tk.END)
        texto_saida.insert('1.0', f"Lista original: {lista_numeros}\nLista ordenada: {lista_ordenada}")
        texto_saida.config(state='disabled')
        tempo_execucao.config(text=f"Tempo de execução do algoritmo: {tempo_insertion_sort(lista_numeros, ordem):.5f} segundos.")
    except ValueError:
        texto_saida.config(state='normal')
        texto_saida.delete('1.0', tk.END)
        texto_saida.insert('1.0', "A lista deve conter apenas números separados por vírgula ou espaço.")
        texto_saida.config(state='disabled')

def tempo_insertion_sort(lista, ordem):
    inicio = time.time()
    insertion_sort(lista, ordem)
    fim = time.time()
    return fim - inicio

janela = tk.Tk()
janela.title("Ordenação de Listas")

# Frame para entrada da lista
frame_entrada = tk.Frame(janela)
frame_entrada.pack(padx=10, pady=10)

label_entrada = tk.Label(frame_entrada, text="Insira a lista de números:")
label_entrada.pack(side=tk.LEFT)

entrada_lista = tk.Entry(frame_entrada)
entrada_lista.pack(side=tk.LEFT)

# Frame para escolha da ordem de ordenação
frame_ordem = tk.Frame(janela)
frame_ordem.pack(padx=10, pady=10)

label_ordem = tk.Label(frame_ordem, text="Ordem de ordenação:")
label_ordem.pack(side=tk.LEFT)

var_ordem = tk.StringVar(value="crescente")

radio_crescente = tk.Radiobutton(frame_ordem, text="Crescente", variable=var_ordem, value="crescente")
radio_crescente.pack(side=tk.LEFT)

radio_decrescente = tk.Radiobutton(frame_ordem, text="Decrescente", variable=var_ordem, value="decrescente")
radio_decrescente.pack(side=tk.LEFT)

# Botão de ordenação
botao_ordenar = tk.Button(janela, text="Ordenar", command=ordenar)
botao_ordenar.pack(padx=10, pady=10)

# Texto de saída
texto_saida = tk.Text(janela, height=5, width=40, state='disabled')
texto_saida.pack(padx=10, pady=10)

# Tempo de execução do algoritmo
tempo_execucao = tk.Label(janela, text="")
tempo_execucao.pack(padx=10, pady=10)

janela.mainloop()
