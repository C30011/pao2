def mostrar_menu():
    print("1 - Cadastrar nova reserva")
    print("2 - Carregar reservas já existentes")
    print("3 - Consultar reservas ")
    print("4 - Cancelar reservas")
    print("5- Listar todas as reservas")
    print("6 - Exibir estatìsticas gerais")
def main():
    while (True):
        mostrar_menu()
        opcao=int(input("Digite a opção desejada:"))
        if opcao== 1:
            cadastrar_reserva()
        elif opcao == 2:
            carregar_reservas()
        elif opcao == 3:
            consultar_reservas()
        elif opcao == 4:
            cancelar_reservas()
        elif opcao == 5:
            listar_reservas
        elif opcao == 6:
            exibir_estatisticas
        elif opcao==7:
            print("Saindo..")
            time.sleep(3)
            continue
        time.sleep(3)
        os.system("clear")
main()
