valor = float(input("Digite o valor da compra: R$"))
diapagamento = int(input("Qual o dia que vc fez o pagamento? "))
diavencimento = int(input("Digite o dia do vencimento: "))
if diapagamento < diavencimento:
    desconto = valor - (valor * 0.1)
    print(f"Voce pagou antes do dia do vencimento, com o desconto de 10% eu pagamento ficou R${desconto}")
else:
    atraso = (diapagamento-diavencimento) * -1
    aumento = valor*(atraso * 0.02)
    multa = valor + (aumento*valor)
    print(f"Voce pagou {atraso} dias depois do vencimento, o valor a ser pago com a multa será de R${multa} ")