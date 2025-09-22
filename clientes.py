clientes = []

def cadastrar_cliente():
    nome = input("Nome: ")
    cpf = input("CPF: ")
    idade = input("Idade: ")
    telefone = input("Telefone: ")
    email = input("E-mail: ")
    senha = input("Senha: ")

    cliente = {
        "nome": nome,
        "cpf": cpf,
        "idade": idade,
        "telefone": telefone,
        "email": email,
        "senha": senha
    }

    clientes.append(cliente)
    print("✅ Cliente cadastrado com sucesso!\n")

def listar_clientes():
    if not clientes:
        print("⚠ Nenhum cliente cadastrado.\n")
    else:
        for i, cliente in enumerate(clientes, 1):
            print(f"{i}. {cliente['nome']} - CPF: {cliente['cpf']}")
        print()
        
    "Função nova"
def receber_nfce(cliente_nome, nfce):
    print(f"📄 Cliente {cliente_nome} recebeu a NFCe: {nfce}\n")
