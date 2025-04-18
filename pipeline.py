import pandas as pd
import json

arquivo_csv = input("Digite o nome do arquivo CSV: ")
    
# Lê o arquivo CSV e converte pra dicionário
def ler_csv(csv) -> dict:
    with open(csv, "r", encoding = 'utf-8'):
        df = pd.read_csv(csv)

    return df.to_dict(orient='records')

df_lido_conv = ler_csv(arquivo_csv)
print('Csv convertido pra dicionario: ', (json.dumps(df_lido_conv, indent=3, ensure_ascii=False)))
print('\n')

# Retornar um dicionário filtrando valores > 1000

def processar_dados(df_lido_conv) -> dict:
    dados_processados = []
    for d in df_lido_conv:
        if d['vendas'] > 1000: 
            dados_processados.append(d)
        else:
            pass
        
    return dados_processados

dados_processados = (processar_dados(df_lido_conv))
print('Dados processados com valores > 1000: ', dados_processados)
print('\n')

# Função pra calcular as vendas por categoria

def calcular_vendas_categoria(processar_dados) -> dict:
    venda_por_categoria = []
    for d in processar_dados:
        calculo = d['quantidade'] * d['vendas']
        produto = d['produto']
        dicionario = {}
        dicionario[produto] = round(calculo,2)
        venda_por_categoria.append(dicionario)

    return venda_por_categoria

venda_total = calcular_vendas_categoria(dados_processados)
print('O total de vendas de produtos com valores > 1000 foi: ', venda_total)
print('\n')



