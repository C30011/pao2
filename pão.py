
print("--- Sistema de Reservas: Hotel Porto Seguro ---")

nome = input("Nome do responsável: ")
if nome == "":
     print("O Nome é Inválido!:")
     exit()

dia_in = int(input("Dia do check-in: "))
mes_in = int(input("Mês do check-in: "))
ano_in = int(input("Ano do check-in: "))

dia_out = int(input("\nDia do check-out: "))
mes_out = int(input("Mês do check-out: "))
ano_out = int(input("Ano do check-out: "))

if (ano_out < ano_in) or \
(ano_out == ano_in and mes_out < mes_in) or \
(ano_out == ano_in and mes_out == mes_in and dia_out <= dia_in):
     print("A data de check-out deve ser posterior ao check-in.")
     exit()

quarto = input("Tipo de quarto (Pataxó, Ancestral, Descobrimento): ")
Quantidade_de_quartos = int(input("Digite a quantidade de Quartos: "))
if Quantidade_de_quartos == "":
     print("O Nome é Inválido!:")
     exit()

diaria = 0
if quarto == "Pataxó":
     diaria = 100 * Quantidade_de_quartos
elif quarto == "Ancestral":
     diaria = 180 * Quantidade_de_quartos
elif quarto == "Descobrimento":
     diaria = 250 * Quantidade_de_quartos
else:
     print("Quarto inválido")
     exit()

total_dias = (dia_out - dia_in) + (mes_out - mes_in) * 30 + (ano_out - ano_in) * 365
custo_total = total_dias * diaria

print("\n" + "="*30)
print(f"Nome do Responsável: {nome}")
print(f"Data de Checkin e de Checkout: {dia_in}/{mes_in}/{ano_in} a {dia_out}/{mes_out}/{ano_out}")
print(f"A Quantidade de quartos é: {Quantidade_de_quartos}")
print(f"Tipo de Quarto: {quarto}")
print(f"Custo da Reserva: R$ {custo_total}")
print("="*30)
