def calculararroba(peso):
    arroba = (peso * 0.5) / 15
    print(arroba)
    return arroba

def main():
    quilo = float(input('Digite o peso do boi em KG: '))
    chamar = calculararroba(quilo)

main()