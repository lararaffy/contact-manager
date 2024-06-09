def add_contato(contatos, nome, telefone):
    contatos[nome] = {'telefone': telefone}
    return contatos

def remover_contato(contatos, nome):
    if nome in contatos:
        del contatos[nome]
    return contatos

def procurar_contato(contatos, nome):
    return contatos.get(nome, 'Contato não encontrado.')

def listar_contatos(contatos):
    return contatos

