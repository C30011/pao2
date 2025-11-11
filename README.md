from datetime import datetime
import os    
import sys
import time
disponivel = {"Standard": 10, "Premium": 5, "Luxo": 3}
total_reservas = soma_valores = maior_valor = maior_dias = 0
resp_maior_valor = resp_maior_duracao = ""

def mostrar_menu():
    print("1 - Cadastrar nova reserva")
    print("2 - Carregar reservas já existentes")
    print("3 - Consultar reservas ")
    print("4 - Cancelar reservas")
    print("5 - Listar todas as reservas")
    print("6 - Exibir estatìsticas gerais")

def main():
    while (True):
        mostrar_menu()
        opcao=int(input("Digite a opção desejada:"))
        if opcao== 1:
            Cadastrar_Reserva()
        elif opcao == 2:
            Carregar_reservas()
        elif opcao == 3:
            consultar_reservas()
        elif opcao == 4:
            cancelar_reservas()
        elif opcao == 5:
            listar_reservas()
        elif opcao == 6:
            exibir_estatisticas()
        elif opcao==7:
            print("Saindo..")
            time.sleep(3)
            continue
        time.sleep(3)
        os.system("clear")
main()
           

def Cadastrar_Reserva ():
    print('Ok, Vamos Cadastrar sua Reserva!')
    while True:
        nome = input("\nNome do responsável: ")
        if not nome:
                print("Nome inválido.")
        break
    while True:
        try:
            Checkin = datetime.strptime(input("Check-in (dd/mm/aaaa): "), "%d/%m/%Y")
        except ValueError:
            print('Data de Checkin inválida.')
            continue
        try:
            Checkout = datetime.strptime(input("Check-out (dd/mm/aaaa): "), "%d/%m/%Y")
            if Checkout <= Checkin: 
                print("Check-out inválido."); 
        except ValueError:
            print('Data de Checkout inválida.')
        continue
    While True:
        Tipo_de_Quarto = input('Digite o tipo de Quarto (Standard, Premium, Luxo):')

 
