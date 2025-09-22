from dados import pedidos, fornecedores, produtos

def realizar_pedido():
    print("\n--- Realizar Pedido de Compra ---")
    
    if not fornecedores:
        print("Nenhum fornecedor cadastrado!")
        return
    if not produtos:
        print("Nenhum produto cadastrado!")
        return
    
    from fornecedores import listar_fornecedores
    listar_fornecedores()
    idx_fornecedor = int(input("Escolha o fornecedor (número): ")) - 1
    fornecedor = fornecedores[idx_fornecedor]
    
    pedido_produtos = []
    total = 0
    while True:
        from produtos import listar_produtos
        listar_produtos()
        codigo_prod = input("Código do produto a adicionar (ou 'fim' para encerrar): ")
        if codigo_prod.lower() == "fim":
            break
        qtde = int(input("Quantidade: "))
        produto = next((p for p in produtos if p["codigo"] == codigo_prod), None)
        if produto:
            pedido_produtos.append({"produto": produto, "quantidade": qtde})
            total += produto["preco"] * qtde
            print(f"Adicionado {qtde}x {produto['nome']} ao pedido.")
        else:
            print("Produto não encontrado.")
    
    pedido = {
        "fornecedor": fornecedor["nome"],
        "itens": pedido_produtos,
        "valor_total": total
    }
    pedidos.append(pedido)
    print(f"Pedido finalizado! Valor total: R$ {total:.2f}")
