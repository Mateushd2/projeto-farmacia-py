fornecedores = []

def cadastrar_fornecedor():
    nome = input("Nome da empresa: ")
    cnpj = input("CNPJ: ")
    endereco = input("Endereço: ")
    telefone = input("Telefone: ")
    email = input("E-mail: ")

    fornecedor = {
        "nome": nome,
        "cnpj": cnpj,
        "endereco": endereco,
        "telefone": telefone,
        "email": email
    }

    fornecedores.append(fornecedor)
    print("✅ Fornecedor cadastrado com sucesso!\n")

def listar_fornecedores():
    if not fornecedores:
        print("⚠ Nenhum fornecedor cadastrado.\n")
    else:
        for i, fornecedor in enumerate(fornecedores, 1):
            print(f"{i}. {fornecedor['nome']} - CNPJ: {fornecedor['cnpj']}")
        print()

    "Função nova"
def enviar_nfe(fornecedor_nome, nfe):
    """Simula o envio da Nota Fiscal Eletrônica para a farmácia"""
    print(f"📦 Fornecedor {fornecedor_nome} enviou a NFe: {nfe}\n")
