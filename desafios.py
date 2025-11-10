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


# Desafio 02: Listar todas as tarefas
def listar_tarefas():
    """
    Exibe todas as tarefas da lista numeradas.
    Dica: use um for com enumerate() para mostrar o índice e o nome.
    """
    if not tarefas:
        print("Nenhuma tarefa cadastrada.")
        return

    # Exibe cada tarefa numerada a partir de 1 usando enumerate
    for i, tarefa in enumerate(tarefas, 1):
        print(f"{i} - {tarefa}")


# Desafio 03: Marcar uma tarefa como concluída
def concluir_tarefa(indice):
    """
    Marca uma tarefa como concluída.
    Dica: você pode alterar o texto da tarefa adicionando um 'ok' no início.
    Exemplo: 'Estudar Git' → 'Estudar Git - ok'
    """
    # converte número (1-based) para índice da lista (0-based)
    idx = indice - 1

    # valida índice
    if idx < 0 or idx >= len(tarefas):
        print("Índice inválido!")
        return

    # se já estiver marcada, avisa e retorna
    if isinstance(tarefas[idx], str) and tarefas[idx].endswith(" - ok"):
        print("Tarefa já concluída.")
        return

    # marca como concluída adicionando ' - ok' ao final
    tarefas[idx] = f"{tarefas[idx]} - ok"
    print(f"Tarefa {indice} marcada como concluída.")


# Desafio 04: Remover uma tarefa
def remover_tarefa(indice):
    """
    Remove uma tarefa pelo índice.
    Dica: use pop() para remover da lista.
    """
    # converte número (1-based) para índice da lista (0-based)
    idx = indice - 1
    
    # valida índice
    if idx < 0 or idx >= len(tarefas):
        print("Índice inválido!")
        return
    
    # remove e retorna a tarefa removida
    tarefa_removida = tarefas.pop(idx)
    print(f"Tarefa removida: {tarefa_removida}")


# Desafio 05: Buscar tarefa pelo nome
def buscar_tarefa(nome):
    """
    Busca uma tarefa pelo nome e retorna se ela existe ou não.
    Dica: use um loop para percorrer a lista e comparar strings.
    """
    # se a lista estiver vazia, já retorna que não encontrou
    if not tarefas:
        print("Nenhuma tarefa cadastrada.")
        return False
    
    # percorre a lista procurando pelo nome (case insensitive)
    for tarefa in tarefas:
        # remove o " - ok" se existir, para comparar só o nome
        nome_tarefa = tarefa.replace(" - ok", "")
        if nome.lower() in nome_tarefa.lower():
            print(f"Tarefa encontrada: {tarefa}")
            return True
    
    print("Tarefa não encontrada.")
    return False


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

if __name__ == "__main__":
    menu()