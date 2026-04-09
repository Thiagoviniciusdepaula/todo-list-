def mostrar_menu():
    print("\n=== TO-DO LIST ===")
    print("1 - Adicionar tarefa")
    print("2 - Listar tarefas")
    print("3 - Remover tarefa")
    print("4 - Sair")


def adicionar_tarefa(tarefas):
    tarefa = input("Digite a nova tarefa: ")
    tarefas.append(tarefa)
    print("Tarefa adicionada!")


def listar_tarefas(tarefas):
    if not tarefas:
        print("Nenhuma tarefa cadastrada.")
    else:
        print("\nSuas tarefas:")
        for i, tarefa in enumerate(tarefas, start=1):
            print(f"{i}. {tarefa}")


def remover_tarefa(tarefas):
    listar_tarefas(tarefas)

    if tarefas:
        try:
            numero = int(input("Digite o número da tarefa para remover: "))
            tarefa_removida = tarefas.pop(numero - 1)
            print(f"Tarefa removida: {tarefa_removida}")
        except:
            print("Número inválido!")


def main():
    tarefas = []

    while True:
        mostrar_menu()
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            adicionar_tarefa(tarefas)

        elif opcao == "2":
            listar_tarefas(tarefas)

        elif opcao == "3":
            remover_tarefa(tarefas)

        elif opcao == "4":
            print("Saindo...")
            break

        else:
            print("Opção inválida!")


if __name__ == "__main__":
    main()
