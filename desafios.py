# Arquivo: desafios.py
# Projeto: Mini To-Do List
# Objetivo: completar as funções para que o sistema funcione corretamente
# Dica: use apenas listas, loops e condicionais!

# Lista principal de tarefas
tarefas = []


# Desafio 01: Adicionar uma nova tarefa
def adicionar_tarefa(titulo):
    if titulo:
        tarefas.append(titulo)
        print(f"Tarefa '{titulo}' adicionada com sucesso!")
    else:
        print("Erro: O título não pode ser vazio.")


# Desafio 02: Listar todas as tarefas
def listar_tarefas():
    print("\n--- LISTA DE TAREFAS ---")
    if not tarefas:
        print("Nenhuma tarefa cadastrada.")
        return

    for indice, titulo in enumerate(tarefas, start=1):
        print(f"{indice}. {titulo}")


# Desafio 03: Marcar uma tarefa como concluída
def concluir_tarefa(indice):
    try:        
        indice_real = indice - 1
        
        if 0 <= indice_real < len(tarefas):
            if " - ok" not in tarefas[indice_real]:
                tarefas[indice_real] += " - ok"
                print(f"Tarefa {indice} marcada como concluída!")
            else:
                print(f"Tarefa {indice} já estava concluída.")
        else:
            print(f"Erro: Tarefa {indice} não encontrada.")
    except Exception as e:
        print(f"Erro ao concluir tarefa: {e}")


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
