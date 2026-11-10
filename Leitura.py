import csv
def ler_ficheiro_produtos():
    '''
    Lê o ficheiro produtos.csv e mostra cada linha no terminal.

    Serve apenas para testar a leitura. Se o ficheiro não existir, mostra uma mensagem de erro em vez de parar o programa. 

    Returns:
        None:apenas imprime as linhas.

    '''
    try:
        with open("dados/produtos.csv", "r", encoding="utf-8-sig",newline='') as ficheiro:
            conteudo = csv.reader(ficheiro,delimiter=";")
            for linha in conteudo:
                print(linha) 
    except FileNotFoundError:
        print("Erro: O ficheiro não foi encontrado.")
    print("a continuar o programa...")

def ler_ficheiro_vendas():
    '''
        Lê o ficheiro vendas.csv e mostra cada linha no terminal.
    
        Serve apenas para testar a leitura. Se o ficheiro não existir, mostra uma mensagem de erro em vez de parar o programa. 
    
        Returns:
            None:apenas imprime as linhas.
    
        '''
    try:
        with open("dados/vendas.csv", "r", encoding="utf-8-sig",newline='') as ficheiro:
            conteudo = csv.reader(ficheiro,delimiter=";")
            for linha in conteudo:
                print(linha) 
    except FileNotFoundError:
        print("Erro: O ficheiro não foi encontrado.")
    print("a continuar o programa...")   

def ler_produtos():
    '''
    Lê o ficheiro produtos.csv e organiza os dados num dicionario.
    
    Converte o preco unitario e a margem para float(trocando a virgula por ponto)
    
    Returns:
        dict:{id_produto:{"nome","tipo","pais_origem","preco","margem"}}
    
    '''
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
    '''
    Lê o ficheiro vendas.csv e guarda cada venda num dicionario.

    Returns:
        list: lista de dicionarios com id_venda,id_produto,vendedor, distrito e quantidade(int).
    
    '''
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
    '''
    Associa cada venda ao produto correspondente através do id_produto
    
    Args:
        produtos(dict):dicionario devolvido por ler_produtos().
        vendas(list):lista devolvida por ler_vendas()
    
    Returns:
        dados(list):vendas completas com nome,tipo,pais de origem,preco e margem do produto.
        Se existir vendas com id_produto nulo são ignoradas
    
    '''
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
    return (dados)


