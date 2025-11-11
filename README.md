from datetime import datetime
import os    
import sys
import time

def Menu_Principal():
    print('Digite o Numero da Respectivo que Deseja do Menu Principal')
    print('1 - Cadastrar Reserva')
    print('2 - Listar Reservas Disponiveis')
    print('3 - Cancelar Reserva')
    print('4 - Caucular Estatistica ')
    print('5 - Sair')
    
def Cadastrar_Reserva ():
    print('Vamos Cadastrar sua Reserva!')

    Nome_Responsavel = input('Digite o seu Nome:')

    while True:
        try:
            Checkin = datetime.strptime(input("Check-in (dd/mm/aaaa): "), "%d/%m/%Y")
        except ValueError:
            print('Data de Checkin inválida.')
            continue
        try:
            Checkout = datetime.strptime(input("Check-out (dd/mm/aaaa): "), "%d/%m/%Y")
        except ValueError:
            print('Data de Checkout inválida.')
            continue
        if Checkout <= Checkin: 
            print("Check-out inválido."); 
            continue

        Tipo_De_Quarto = input('Digite o tipo de quarto (Standard,Premium,Luxo):')


def Listar_Reservas ():
    print(' Ok, Vamos Listar Sua Reserva ')

def Cancelar_Reserva ():
    print('Ok, A Reserva será Cancelada')

def Cancelar_Reserva():
    print('Ok, Cancelaremos sua Reserva')

def Caucular_Estatistica():
    print('Ok, Caucularemos as Estatisticas')

def Sair():
    print('Ok, Iremos Retirar o programa')
def main():
    Menu_Principal()
Menu_Principal()

