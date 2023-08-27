def main():
    palavras = [] 
    
    while True:
        palavra = input("Digite uma palavra (ou pressione Enter para sair): ")
        if palavra == "":
            break
        else:
            palavras.append(palavra)
    
    print("\nPalavras com mais de 5 letras:")
    for palavra in palavras:
        if len(palavra) > 5:
            print(palavra)

main()