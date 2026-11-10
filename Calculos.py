from Leitura import *

class VendaProd:
    def __init__(self, dados):
        self.dados = dados
    def apresentar(self):
        print(self.dados)
    def calcular_vendas(self):
        return len(self.dados)
    def qtd_total_produtos(self):
        return sum(venda["quantidade"] for venda in self.dados)
    def qtd_prod_vendidos_nome(self):
        totais = {}
        for venda in self.dados:
            nome_produto = venda["nome_produto"]
            qtd= venda["quantidade"]
            if nome_produto in totais:
                totais[nome_produto]+=qtd
            else:
                totais[nome_produto]=qtd
        return(totais)
    def qtd_prod_vendidos_tipo(self):
            totais2 = {}
            for venda in self.dados:
                tipo = venda["tipo"]
                qtd= venda["quantidade"]
                if tipo in totais2:
                    totais2[tipo]+=qtd
                else:
                    totais2[tipo]=qtd
            return(totais2)
    def total_faturacao(self):
        total_faturacao=0
        for venda in self.dados:
           qtd= venda["quantidade"]
           preco_uni = venda["preco"]
           total_faturacao += qtd * preco_uni
        return(total_faturacao)
    def lucro_obtido(self):
        lucro_obtido=0
        for venda in self.dados:
            qtd= venda["quantidade"]
            margem = venda["margem"]
            lucro_obtido+= margem * qtd
        return(lucro_obtido)
    def produto_mais_vendido_nome(self):
        totais3 = {}
        for venda in self.dados:
            nome_produto = venda["nome_produto"]
            qtd= venda["quantidade"]
            if nome_produto in totais3:
                totais3[nome_produto]+=qtd
            else:
                totais3[nome_produto]=qtd
        maximo_venda_nome= max(totais3, key=totais3.get)
        return(maximo_venda_nome,totais3[maximo_venda_nome])
    def produto_mais_vendido_tipo(self):
        totais4 = {}
        for venda in self.dados:
            tipo = venda["tipo"]
            qtd= venda["quantidade"]
            if tipo in totais4:
                totais4[tipo]+=qtd
            else:
                totais4[tipo]=qtd
        maximo_venda_tipo= max(totais4, key=totais4.get)
        return(maximo_venda_tipo,totais4[maximo_venda_tipo])
    def vendedor_maior_faturacao(self):
        total_faturacao= {}
        for venda in self.dados:
            qtd= venda["quantidade"]
            preco_uni = venda["preco"]
            vendedor= venda["vendedor"]
            if vendedor in total_faturacao:
                total_faturacao[vendedor] += qtd * preco_uni
            else:
                total_faturacao[vendedor] = qtd * preco_uni
        maximo_vendedor= max(total_faturacao, key=total_faturacao.get)
        return(maximo_vendedor,total_faturacao[maximo_vendedor])             
   

