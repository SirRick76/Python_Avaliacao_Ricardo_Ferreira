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
        ficheiro.write("-" * 156 + "\n")
        for venda in dados:
            ficheiro.write(
                f"{venda["id_venda"]:<12}"
                f"{venda["id_produto"]:<13}"
                f"{venda["vendedor"]:<22}"
                f"{venda["distrito"]:<20}"
                f"{venda["nome_produto"]:<20}"
                f"{venda["tipo"]:<15}"
                f"{venda["pais_origem"]:<15}"
                f"{venda["quantidade"]:<13}"
                f"{venda["preco"]:<18}"
                f"{venda["margem"]:<10}\n"
            )
            ficheiro.write("_" * 156 + "\n")
        ficheiro.write("2. ANÁLISE DAS VENDAS \n")
        ficheiro.write("\n")
        ficheiro.write("Número de vendas:")
        ficheiro.write(f"{analise.calcular_vendas():}\n")
        

    