from dados import produtos

def cadastrar_produto():
    print("\n--- Cadastro de Produto ---")
    codigo = input("Código do produto: ")
    nome = input("Nome comercial: ")
    nome_generico = input("Nome genérico: ")
    categoria = input("Categoria: ")
    forma = input("Forma farmacêutica: ")
    dosagem = input("Dosagem/Concentração: ")
    validade = input("Data de validade (MM/AAAA): ")
    preco = float(input("Preço: R$ "))
    
    produto = {
        "codigo": codigo,
        "nome": nome,
        "nome_generico": nome_generico,
        "categoria": categoria,
        "forma": forma,
        "dosagem": dosagem,
        "validade": validade,
        "preco": preco
    }
    produtos.append(produto)
    print("Produto cadastrado com sucesso!")

def listar_produtos():
    print("\n--- Lista de Produtos ---")
    if not produtos:
        print("Nenhum produto cadastrado.")
        return
    for p in produtos:
        print(f"{p['codigo']} - {p['nome']} ({p['categoria']}) - R$ {p['preco']}")