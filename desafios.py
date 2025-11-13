# Arquivo: desafios.py
# Projeto: Mini To-Do List
# Objetivo: completar as funções para que o sistema funcione corretamente
# Dica: use apenas listas, loops e condicionais!


# Lista principal de tarefas
tarefas = []


# Desafio 01: Adicionar uma nova tarefa
def adicionar_tarefa(titulo):
    """
    Adiciona uma nova tarefa à lista.
    Dica: use append() para inserir o título na lista 'tarefas'.
    """
    tarefas.append(titulo)
    print(f"✅ Tarefa '{titulo}' adicionada com sucesso!")


# Desafio 02: Listar todas as tarefas
def listar_tarefas():
    """
    Exibe todas as tarefas da lista numeradas.
    Dica: use um for com enumerate() para mostrar o índice e o nome.
    """
    if not tarefas:
        print("📭 Nenhuma tarefa cadastrada.")
    else:
        print("\n📋 Lista de tarefas:")
        for i, tarefa in enumerate(tarefas):
            print(f"{i} - {tarefa}")


# Desafio 03: Marcar uma tarefa como concluída
def concluir_tarefa(indice):
    """
    Marca uma tarefa como concluída.
    Dica: você pode alterar o texto da tarefa adicionando um 'ok' no final.
    Exemplo: 'Estudar Git' → 'Estudar Git - ok'
    """
    if 0 <= indice < len(tarefas):
        if "- ok" not in tarefas[indice]:
            tarefas[indice] = tarefas[indice] + " - ok"
            print(f" Tarefa '{tarefas[indice]}' marcada como concluída!")
        else:
            print(" Essa tarefa já foi concluída.")
    else:
        print(" Índice inválido.")


# Desafio 04: Remover uma tarefa
def remover_tarefa(indice):
    """
    Remove uma tarefa pelo índice.
    Dica: use pop() para remover da lista.
    """
    if 0 <= indice < len(tarefas):
        removida = tarefas.pop(indice)
        print(f" Tarefa '{removida}' removida com sucesso!")
    else:
        print(" Índice inválido.")


# Desafio 05: Buscar tarefa pelo nome
def buscar_tarefa(nome):
    """
    Busca uma tarefa pelo nome e retorna se ela existe ou não.
    Dica: use um loop para percorrer a lista e comparar strings.
    """
    encontrada = False
    for tarefa in tarefas:
        if nome.lower() in tarefa.lower():
            print(f"🔎 Encontrada: {tarefa}")
            encontrada = True
    if not encontrada:
        print("🚫 Nenhuma tarefa encontrada com esse nome.")


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
            print(" Encerrando o programa...")
            break
        else:
            print(" Opção inválida! Tente novamente.")


# menu()  # Descomente para testar
