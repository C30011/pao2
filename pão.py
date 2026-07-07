 total_reservas += 1
        soma_valores += total
        if total > maior_valor: maior_valor, resp_maior_valor = total, nome
        if dias > maior_dias: maior_dias, resp_maior_duracao = dias, nome
        disponivel[tipo_de_Quarto] -= quantidade_de_Quartos
