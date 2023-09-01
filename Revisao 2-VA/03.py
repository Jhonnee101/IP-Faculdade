def relatorio_vendas(vendas):
    total_vendas = sum(sum(meses) for meses in vendas.values())
    media_vendas = total_vendas / len(vendas)
    
    maior_venda = max((vendedor, sum(meses)) for vendedor, meses in vendas.items())
    
    print("Relatório de Vendas:")
    print(f"Total de Vendas da Empresa: R$ {total_vendas:.2f}")
    print(f"Média de Vendas da Empresa: R$ {media_vendas:.2f}")
    print(f"Vendedor com Maior Venda: {maior_venda[0]} - R$ {maior_venda[1]:.2f}")

def main():
    vendas = {
        "Vendedor1": [1500, 2000, 1800, 2200, 2500, 2100, 3000, 1800, 1900, 2200, 2500, 3000],
        "Vendedor2": [1800, 1900, 2000, 2200, 2100, 1900, 2500, 2200, 1800, 2100, 2300, 2400],
        "Vendedor3": [2000, 2200, 2100, 2500, 2300, 2400, 1800, 1900, 2200, 2100, 2000, 2100]}    
    relatorio_vendas(vendas)

main()