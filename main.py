from fornecedores import cadastrar_fornecedor, listar_fornecedores, enviar_nfe
from produtos import cadastrar_produto, listar_produtos
from clientes import cadastrar_cliente, listar_clientes, receber_nfce
from pedidos import realizar_pedido
from sefaz import validar_nfe, validar_nfce

def menu():
    while True:
        print("=== Sistema de Farmácia ===")
        print("1. Cadastrar Fornecedor")
        print("2. Cadastrar Produto")
        print("3. Cadastrar Cliente")
        print("4. Realizar Pedido de Compra")
        print("5. Listar Fornecedores")
        print("6. Listar Produtos")
        print("7. Listar Clientes")
        print("8. Enviar NFe (Fornecedor)")
        print("9. Receber NFCe (Cliente)")
        print("10. Validar NFe na SEFAZ")
        print("11. Validar NFCe na SEFAZ")
        print("12. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            cadastrar_fornecedor()
        elif opcao == "2":
            cadastrar_produto()
        elif opcao == "3":
            cadastrar_cliente()
        elif opcao == "4":
            realizar_pedido()
        elif opcao == "5":
            listar_fornecedores()
        elif opcao == "6":
            listar_produtos()
        elif opcao == "7":
            listar_clientes()
        elif opcao == "8":
            fornecedor = input("Nome do fornecedor: ")
            nfe = input("Número da NFe: ")
            enviar_nfe(fornecedor, nfe)
        elif opcao == "9":
            cliente = input("Nome do cliente: ")
            nfce = input("Número da NFCe: ")
            receber_nfce(cliente, nfce)
        elif opcao == "10":
            nfe = input("Número da NFe: ")
            validar_nfe(nfe)
        elif opcao == "11":
            nfce = input("Número da NFCe: ")
            validar_nfce(nfce)
        elif opcao == "12":
            print("👋 Saindo...")
            break
        else:
            print("⚠ Opção inválida.\n")

menu()
