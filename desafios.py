# Arquivo: desafios.py
# Projeto: Mini To-Do List
# Objetivo: completar as funções para que o sistema funcione corretamente
# Dica: use apenas listas, loops e condicionais

# Lista principal de tarefas

tarefas = []

# Desafio 01: Adicionar uma nova tarefa


def adicionar_tarefa(titulo):
    tarefas.append(titulo)


# Desafio 02: Listar todas as tarefas
def listar_tarefas():
    for i, tarefa in enumerate(tarefas):
        print(f"{i + 1} - {tarefa}")


# Desafio 03: Marcar uma tarefa como concluída
def concluir_tarefa(indice):
    def concluir_tarefa(indice):
    if 0 <= indice < len(tarefas):
        tarefas[indice] = tarefas[indice] + " - ok"


# Desafio 04: Remover uma tarefa
def remover_tarefa(indice):
    if 0 <= indice < len(tarefas):
        tarefas.pop(indice)


# Desafio 05: Buscar tarefa pelo nome
def buscar_tarefa(nome):
    for tarefa in tarefas:
        if nome.lower() in tarefa.lower():
            print(f"Tarefa encontrada: {tarefa}")
            return
    print("Tarefa não encontrada.")


# Desafio 06: Menu interativo (opcional)
def menu():
    while True:
        print("\n--- MENU TO-DO ---")
        print("1 - Adicionar tarefa")
        print("2 - Listar tarefas")
        print("3 - Concluir tarefa")
        print("4 - Remover tarefa")
        print("5 - Buscar tarefa")
        print("0 - Sair")

        opcao = input("Escolha: ")

        if opcao == "1":
            titulo = input("Título da tarefa: ")
            adicionar_tarefa(titulo)
        elif opcao == "2":
            listar_tarefas()
        elif opcao == "3":
            indice = int(input("Número da tarefa: ")) - 1
            concluir_tarefa(indice)
        elif opcao == "4":
            indice = int(input("Número da tarefa: ")) - 1
            remover_tarefa(indice)
        elif opcao == "5":
            nome = input("Nome da tarefa: ")
            buscar_tarefa(nome)
        elif opcao == "0":
            print("Encerrando o programa...")
            break
        else:
            print("Opção inválida! Tente novamente.")


# Dica Final:
# Quando terminar todos os desafios:
# 1️ Teste todas as funções usando o menu()
# 2️ Faça commit das alterações, para cada commit crie uma tag.
# 3️ Crie a tag final: tag: desafios-completos-v1.0

# menu()  # Descomente para testar
