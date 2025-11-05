# Lista principal de tarefas
tarefas = []

# Desafio 01: Adicionar uma nova tarefa
def adicionar_tarefa(titulo):
    """
    Adiciona uma nova tarefa à lista.
    Dica: use append() para inserir o título na lista 'tarefas'.
    """
    tarefas.append(titulo)
    print(f"Tarefa '{titulo}' adicionada com sucesso!")

# Desafio 02: Listar todas as tarefas
def listar_tarefas():
    """
    Exibe todas as tarefas da lista numeradas.
    Dica: use um for com enumerate() para mostrar o índice e o nome.
    """
    if not tarefas:
        print("Nenhuma tarefa cadastrada.")
        return

    for i, tarefa in enumerate(tarefas):
        print(f"{i + 1}. {tarefa}")

# Desafio 03: Marcar uma tarefa como concluída
def concluir_tarefa(indice):
    """
    Marca uma tarefa como concluída.
    Dica: você pode alterar o texto da tarefa adicionando um 'ok' no início.
    Exemplo: 'Estudar Git' → 'Estudar Git - ok'
    """
    if 0 <= indice < len(tarefas):
        tarefas[indice] = tarefas[indice] + " - ok"
        print(f"Tarefa '{tarefas[indice]}' concluída!")
    else:
        print("Índice inválido. Tarefa não encontrada.")

# Desafio 04: Remover uma tarefa
def remover_tarefa(indice):
    """
    Remove uma tarefa pelo índice.
    Dica: use pop() para remover da lista.
    """
    if 0 <= indice < len(tarefas):
        tarefa_removida = tarefas.pop(indice)
        print(f"Tarefa '{tarefa_removida}' removida com sucesso!")
    else:
        print("Índice inválido. Tarefa não encontrada.")

# Desafio 05: Buscar tarefa pelo nome
def buscar_tarefa(nome):
    """
    Busca uma tarefa pelo nome e retorna se ela existe ou não.
    Dica: use um loop para percorrer a lista e comparar strings.
    """
    for i, tarefa in enumerate(tarefas):
        if nome.lower() in tarefa.lower():  # Comparação sem considerar maiúsculas/minúsculas
            print(f"Tarefa encontrada: {i + 1}. {tarefa}")
            return
    print(f"Tarefa '{nome}' não encontrada.")

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
            try:
                indice = int(input("Número da tarefa: ")) - 1  # Ajustando para índice 0 baseado
                concluir_tarefa(indice)
            except ValueError:
                print("Por favor, insira um número válido.")
        elif opcao == "4":
            try:
                indice = int(input("Número da tarefa: ")) - 1  # Ajustando para índice 0 baseado
                remover_tarefa(indice)
            except ValueError:
                print("Por favor, insira um número válido.")
        elif opcao == "5":
            nome = input("Nome da tarefa: ")
            buscar_tarefa(nome)
        elif opcao == "0":
            print("Encerrando o programa...")
            break
        else:
            print("Opção inválida! Tente novamente.")

menu()  
