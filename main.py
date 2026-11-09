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
#analise.apresentar()
analise.calcular_vendas()
analise.qtd_prod_vendidos_nome()
analise.qtd_prod_vendidos_tipo()
analise.total_faturacao()
analise.lucro_obtido()
analise.produto_mais_vendido_nome()
analise.produto_mais_vendido_tipo()
analise.vendedor_maior_faturacao()

criar_ficheiro_relatorio()
escrever_ficheiro_relatorio(dados,analise)
