def taximetro(distancia):
    def calculaMult():
        if distancia < 5:
            return 1.2
        else:
            return 1
    multiplicador = calculaMult()
    largada = 3
    km_rodado = 2
    valor = (largada + distancia + km_rodado) * multiplicador
    return valor

dist = eval(input("Entre com a distancia a ser percorrida em Km: "))

pagamento = taximetro(dist)

print(f"O valor da corrida é R$: {pagamento}")

input("Obrigado pela preferencia!")



