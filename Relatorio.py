import datetime as dt
from Leitura import *
from Calculos import *


def criar_ficheiro_relatorio():
    try:
        with open("relatorio_vendas.txt", "x", encoding="utf-8") as ficheiro:
            pass
    except FileExistsError:
        print("O ficheiro já existe!")
def escrever_ficheiro_relatorio(dados,analise):
    data_atual = dt.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open("relatorio_vendas.txt", "w", encoding="utf-8") as ficheiro:
        ficheiro.write(f"Última atualização: {data_atual}\n")
        ficheiro.write("ANÁLISE DE VENDAS \n")
        ficheiro.write("1. DADOS DAS VENDAS \n")
        ficheiro.write(f"{"|Id_Venda ":<12}{"|Id_Produto":<13}{"|Vendedor ":<22}{"|Distrito ":<20}{"|Nome Produto ":<20}{"|Tipo ":<15}{"|Pais Origem ":<15}{"|Quantidade ":<13}{"|Preco Unitario ":<18}{"|Margem |":<10}\n")
        ficheiro.write("-" * 157 + "\n")
        for venda in dados:
            ficheiro.write(
                f"|{venda["id_venda"]:<11}"
                f"|{venda["id_produto"]:<12}"
                f"|{venda["vendedor"]:<21}"
                f"|{venda["distrito"]:<19}"
                f"|{venda["nome_produto"]:<19}"
                f"|{venda["tipo"]:<14}"
                f"|{venda["pais_origem"]:<14}"
                f"|{venda["quantidade"]:<12}"
                f"|{venda["preco"]:<17}"
                f"|{venda["margem"]:<7}|\n"
            )
            ficheiro.write("-" * 157 + "\n")
        ficheiro.write("2. ANÁLISE DAS VENDAS \n")
        ficheiro.write("\n")
        ficheiro.write("Número de vendas:")
        ficheiro.write(f"{analise.calcular_vendas():}\n")
        ficheiro.write("\n")
        ficheiro.write("Quantidade total de produtos vendidos por nome:\n")
        for nomes,qtd in analise.qtd_prod_vendidos_nome().items():
            ficheiro.write(f"{nomes:<20}{qtd:>6} unidades\n")
        ficheiro.write("\n")
        ficheiro.write("Quantidade total de produtos vendidos por nome:\n")
        for tipos,qtd in analise.qtd_prod_vendidos_tipo().items():
            ficheiro.write(f"{tipos:<20}{qtd:>6} unidades\n")
        ficheiro.write("\n")
        ficheiro.write("Total faturado:")
        ficheiro.write(f"{analise.total_faturacao():}€\n")
        ficheiro.write("\n")
        ficheiro.write("Lucro obtido:")
        ficheiro.write(f"{analise.lucro_obtido():}€\n")
        ficheiro.write("\n")
        ficheiro.write("Produto mais vendido por nome:\n")
        nome,qtd = analise.produto_mais_vendido_nome()
        ficheiro.write(f"Nome Produto: {nome} - {qtd} unidades\n")
        ficheiro.write("\n")
        ficheiro.write("Produto mais vendido por tipo:\n")
        tipo,qtd = analise.produto_mais_vendido_tipo()
        ficheiro.write(f"Tipo Produto: {tipo} - {qtd} unidades\n")
        ficheiro.write("\n")
        ficheiro.write("Vendedor com maior faturação:\n")
        vendedor, maior_faturacao = analise.vendedor_maior_faturacao()
        ficheiro.write(f"Nome Vendedor: {vendedor} - {maior_faturacao} €\n")


        

    