contatos = []

def add_contato():
    nome = str(input("Digite seu nome:  "))
    telefone = input("Digite o número: ")
    novo_contato ={ "Nome": nome, "Telefone": telefone, }
    contatos.append(novo_contato)
    print("Contato adicionado com sucesso!")

def remove_contato():
    nome = input("Digite o nome do contato que deseja excluir: ").strip()
    for contato in contatos:
        if contato["Nome"] == nome:
            contatos.remove(contato)
            print("Contato removido com sucesso!")
            return
    print("Contato não encontrado!")

def procurar_contato():
    nome = input("Digite o nome do contato: ").strip().lower()
    for contato in contatos:
        if contato['Nome'].lower() == nome.lower():
            print(f"Nome: {contato['Nome']}, Telefone: {contato['Telefone']}")
            return
    print ("Contato não encontrado!")
def lista_contatos():
    print (contatos)

def sair():
        print("Encerrando sistema...")
        exit()
