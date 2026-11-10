import csv
from Leitura import *
from Calculos import *
from Relatorio import *

#ler_ficheiro_produtos()
#ler_ficheiro_vendas()
#ler_produtos()
#ler_vendas()
produtos=ler_produtos()
vendas=ler_vendas()
dados = juntar_dados(produtos,vendas)
analise = VendaProd(dados)
print(
    analise.apresentar(),
    analise.calcular_vendas(),
    analise.qtd_total_produtos(),
    analise.qtd_prod_vendidos_nome(),
    analise.qtd_prod_vendidos_tipo(),
    analise.total_faturacao(),
    analise.lucro_obtido(),
    analise.produto_mais_vendido_nome(),
    analise.produto_mais_vendido_tipo(),
    analise.vendedor_maior_faturacao(),
    sep="\n"
)

criar_ficheiro_relatorio()
escrever_ficheiro_relatorio(dados,analise)
