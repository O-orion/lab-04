# Arquivo: desafios.py
# Projeto: Mini To-Do List
# Objetivo: completar as funções para que o sistema funcione corretamente
# Dica: use apenas listas, loops e condicionais!

# Lista principal de tarefas
tarefas = []


# Desafio 01: Adicionar uma nova tarefa
def adicionar_tarefa(titulo):
   def adicionar_tarefa(titulo):
    tarefas.append(titulo)
    print(f"Tarefa adicionada: {titulo}")



# Desafio 02: Listar todas as tarefas
def listar_tarefas():
    if not tarefas:
        print("Nenhuma tarefa cadastrada.")
    else:
        for i, t in enumerate(tarefas, start=1):
            print(f"{i} - {t}")



# Desafio 03: Marcar uma tarefa como concluída
def concluir_tarefa(indice):
    if 0 <= indice - 1 < len(tarefas):
        tarefas[indice - 1] += " - ok"
        print("Tarefa marcada como concluída!")
    else:
        print("Índice inválido!")



# Desafio 04: Remover uma tarefa
def remover_tarefa(indice):
    """
    Remove uma tarefa pelo índice.
    Dica: use pop() para remover da lista.
    """
    # TODO: implementar lógica de remoção
    pass


# Desafio 05: Buscar tarefa pelo nome
def buscar_tarefa(nome):
    """
    Busca uma tarefa pelo nome e retorna se ela existe ou não.
    Dica: use um loop para percorrer a lista e comparar strings.
    """
    # TODO: implementar lógica de busca
    pass


# Desafio 06: Menu interativo (opcional)
def menu():
    """
    Exibe um menu simples para testar o programa.
    Dica: use um while True e input() para ler opções do usuário.
    """
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
            indice = int(input("Número da tarefa: "))
            concluir_tarefa(indice)
        elif opcao == "4":
            indice = int(input("Número da tarefa: "))
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
