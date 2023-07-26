idade = int(input("Quantos anos você tem? "))
tem_licenca = input("Você tem uma licença? (sim/não) ")
pais_tem_licenca = input("Seus pais têm uma licença? (sim/não) ")

if idade <= 15 and pais_tem_licenca == "sim":
    print("Você está apto para pescar!")
elif idade >= 16 and tem_licenca == "sim":
    print("Você está apto para pescar!")
else:
    print("Você não está apto para pescar.")
