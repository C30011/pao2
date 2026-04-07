import sys
valor_reserva = 0

nome = input("\nNome do responsável: ")

checkout_dia = int(input("Digite o dia de Checkout:"))

if checkout_dia > 30:
    print('Data invalida!')
    sys.exit()

checkout_mes = int(input("Digite o mes de Checkout:"))

if checkout_mes > 12:
    print('Data invalida!')
    sys.exit()

checkout_ano = int(input("Digite o ano de Checkout:"))

checkin_dia = int(input("Digite o dia de Checkin:"))

if checkin_dia > 30:
    print('Data invalida!')
    sys.exit()

checkin_mes = int(input("Digite o mes de Checkin:"))

if checkin_mes > 12:
    print('Data invalida!')
    sys.exit()
checkin_ano = int(input("Digite o ano de Checkin:"))

if checkin_dia > checkout_dia and checkin_mes == checkout_mes and checkin_ano == checkout_ano:
    print('Data invalida!')
    sys.exit()
elif checkin_dia == checkout_dia and checkin_mes > checkout_mes and checkin_ano == checkout_ano:
    print('Data invalida!')
    sys.exit()
elif checkin_dia == checkout_dia and checkin_mes == checkout_mes and checkin_ano == checkout_ano:
    print('Data invalida!')
    sys.exit()
Dias = checkin_dia + checkout_dia
meses = checkin_mes checkout_mes

Quantidade_Quartos = int(input('Digite a quantidade de Quartos:'))
tipo_Quarto = input('Digite o tipo de quarto (Pataxó,Ancestra,Descobrimento):')

if tipo_Quarto == 'Pataxó':
    valor_reserva = 100 * Total_Dias * Quantidade_Quartos
elif tipo_Quarto == 'Ascestra':
    valor_reserva = 180 * Total_Dias * Quantidade_Quartos
elif tipo_Quarto == 'Descobrimento':
    valor_reserva = 250 * Total_Dias * Quantidade_Quartos
else:
    print("Tipo de Quarto invalido.")
    sys.exit()


print(f'O Tipo de quarto é {tipo_Quarto}')
print(f'')
    

