import csv
def ler_ficheiro_produtos():
    try:
        with open("dados/produtos.csv", "r", encoding="utf-8-sig",newline='') as ficheiro:
            conteudo = csv.reader(ficheiro,delimiter=";")
            for linha in conteudo:
                print(linha) 
    except FileNotFoundError:
        print("Erro: O ficheiro não foi encontrado.")
    print("a continuar o programa...")

def ler_ficheiro_vendas():
    try:
        with open("dados/vendas.csv", "r", encoding="utf-8-sig",newline='') as ficheiro:
            conteudo = csv.reader(ficheiro,delimiter=";")
            for linha in conteudo:
                print(linha) 
    except FileNotFoundError:
        print("Erro: O ficheiro não foi encontrado.")
    print("a continuar o programa...")   

def ler_produtos():
    produtos={}
    with open("dados/produtos.csv", "r", encoding="utf-8-sig",newline='') as ficheiro:
        leitor = csv.DictReader(ficheiro,delimiter=";")
        for linha in leitor:
            id_produto = linha["ID_Produto"]
            nome = linha["Nome"]
            tipo = linha["Tipo"]
            pais_origem = linha["Pais_Origem"]
            preco_uni = float(linha["Preco_Unitario"].replace(",", "."))
            margem = float(linha["Margem"].replace(",", "."))

            produtos[id_produto] = {
                "nome": nome,
                "tipo": tipo,
                "pais_origem": pais_origem,
                "preco": preco_uni,
                "margem": margem,
            }
    return(produtos)

#poderia ter mantido o dictreader
def ler_vendas():
    vendas=[]
    with open("dados/vendas.csv", "r", encoding="utf-8-sig",newline='') as ficheiro:
        leitor = csv.reader(ficheiro,delimiter=";")
        next(leitor)
        for linha in leitor:
            id_venda=linha[0]
            id_produto=linha[1]
            vendedor=linha[2]
            distrito=linha[3]
            quantidade=int(linha[4])
            vendas.append({
                "id_venda": id_venda,
                "id_produto":id_produto,
                "vendedor":vendedor,
                "distrito":distrito,
                "quantidade":quantidade})
    return(vendas)

def juntar_dados(produtos,vendas):
    dados = []
    for venda in vendas:
        produto = produtos.get(venda["id_produto"])
        if produto is None:
            print("Produto não encontrado:", venda["id_produto"])
            continue
        registo = dict(venda)               # cópia da venda
        registo["nome_produto"] = produto["nome"]
        registo["tipo"] = produto["tipo"]
        registo["pais_origem"] = produto["pais_origem"]
        registo["preco"] = produto["preco"]
        registo["margem"] = produto["margem"]
        dados.append(registo)
    print (dados)


