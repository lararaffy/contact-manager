import contatos
def menu():
    while True:
        print("===== BEM VINDO AO GERENCIAMENTO DE CONTATOS =====")
        print("1 - Adicionar contato")
        print("2 - Remover contato")
        print("3 - Buscar contato")
        print("4 - Lista de contato")
        print("5 - SAIR")
        opcao = int(input("Digite a opção desejada: "))

        if opcao == 1:
            contatos.add_contato()
        elif opcao == 2:
            contatos.remove_contato()
        elif opcao == 3:
            contatos.procurar_contato()
        elif opcao == 4:
            contatos.lista_contatos()
        elif opcao == 5:
            contatos.sair()
        else:
         print("Opção inválida. TENTE NOVAMENTE!")


if __name__ == "_main_":
    menu()