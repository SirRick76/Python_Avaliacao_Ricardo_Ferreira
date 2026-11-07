import csv
from Leitura import *
from Indicadores import *
from Relatorio import *

#ler_ficheiro_produtos()
#ler_ficheiro_vendas()
#ler_produtos()
#ler_vendas()
produtos=ler_produtos()
vendas=ler_vendas()
juntar_dados(produtos,vendas)