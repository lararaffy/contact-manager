contatos = []

def add_contato(nome, telefone):
    nome = str(input("Digite seu nome:  "))
    telefone = input("Digite o número: ")
    novo_contato ={ "Nome": nome, "Telefone": telefone, }
    contatos.append(novo_contato)
    print("Contato adicionado com sucesso!")


def remover_contato(contatos, nome):
    if nome in contatos:
        del contatos[nome]
    return contatos

def procurar_contato(contatos, nome):
    return contatos.get(nome, 'Contato não encontrado.')

def listar_contatos(contatos):
    return contatos

