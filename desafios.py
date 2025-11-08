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
    titulo = titulo.strip()
    if not titulo:
        print("Título vazio. A tarefa não foi adicionada.")
        return
    tarefas.append(titulo)
    print(f"Tarefa '{titulo}' adicionada.")


# Desafio 02: Listar todas as tarefas
def listar_tarefas():
    """
    Exibe todas as tarefas da lista numeradas.
    Dica: use um for com enumerate() para mostrar o índice e o nome.
    """
    if not tarefas:
        print("Nenhuma tarefa cadastrada.")
        return
    for indice, titulo in enumerate(tarefas, start=1):
        print(f"{indice} - {titulo}")


# Desafio 03: Marcar uma tarefa como concluída
def concluir_tarefa(indice):
    """
    Marca uma tarefa como concluída.
    Dica: você pode alterar o texto da tarefa adicionando um 'ok' no início.
    Exemplo: 'Estudar Git' → 'Estudar Git - ok'
    """
    if not tarefas:
        print("Nenhuma tarefa cadastrada.")
        return

    try:
        idx = int(indice) - 1
    except (ValueError, TypeError):
        print("Índice inválido.")
        return

    if idx < 0 or idx >= len(tarefas):
        print("Índice fora do intervalo.")
        return

    if tarefas[idx].endswith(" - ok"):
        print(f"Tarefa '{tarefas[idx]}' já está concluída.")
        return

    tarefas[idx] = f"{tarefas[idx]} - ok"
    print(f"Tarefa '{tarefas[idx]}' concluída.")


# Desafio 04: Remover uma tarefa
def remover_tarefa(indice):
    """
    Remove uma tarefa pelo índice.
    Dica: use pop() para remover da lista.
    """
    if not tarefas:
        print("Nenhuma tarefa cadastrada.")
        return

    try:
        idx = int(indice) - 1
    except (ValueError, TypeError):
        print("Índice inválido.")
        return

    if idx < 0 or idx >= len(tarefas):
        print("Índice fora do intervalo.")
        return

    tarefa = tarefas.pop(idx)
    print(f"Tarefa '{tarefa}' removida.")


# Desafio 05: Buscar tarefa pelo nome
def buscar_tarefa(nome):
    """
    Busca uma tarefa pelo nome e retorna se ela existe ou não.
    Dica: use um loop para percorrer a lista e comparar strings.
    """
    nome = (nome or "").strip()
    if not tarefas:
        print("Nenhuma tarefa cadastrada.")
        return False

    if not nome:
        print("Nome vazio. Informe um texto para buscar.")
        return False

    encontrados = []
    for indice, titulo in enumerate(tarefas, start=1):
        if nome.lower() in titulo.lower():
            encontrados.append((indice, titulo))

    if not encontrados:
        print(f"Nenhuma tarefa encontrada com '{nome}'.")
        return False

    for indice, titulo in encontrados:
        print(f"{indice} - {titulo}")
    return True


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
