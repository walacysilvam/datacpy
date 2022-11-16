
#   Mineracao de Dados :: Python


from datetime import datetime
import pandas as pd
import pymongo

arquivo = "./dataOut/data_001.csv"

# CONEXCAO COM O DB
client = pymongo.MongoClient("mongodb+srv://walacysilva:ZNpBE7zzF2bHYg7@cluster0.orogg7m.mongodb.net/?retryWrites=true&w=majority")
db = client.dataTest
data_estab = db["estab"]


#LE,
#FORMATA &
#INSERE DADOS NO BANCO DE DADOS.
def manager(arquivo):
    arch = open(arquivo,"r")
    contador = 0
    data_list = []

    for linha in arch:
        value = linha.split(';')
        vz = '""'                     
        contador += 1

        for i in range(len(value)):
            if value[i] == vz:
                value[i] = "VAZIO"                                                                  #retirando espacos em branco e add str.
        try:
            cnpj = str(str(value[0]) + '/'+ str(value[1]) + str(value[2])).replace('"', '')         #formatacao do CNPJ
            data_sitcad = datetime.strptime(str(value[6]).replace('"', ''), '%Y%m%d').date()        #formatacao de DATA
            data_initativ = datetime.strptime(str(value[10]).replace('"', ''), '%Y%m%d').date()     #formatacao de DATA2

            dataBloco = {
                'ID': contador,
                'CNPJ': cnpj,
                'IDENTIFICACAO': str(value[3]).replace('"', ''),
                'NOME_FANTASIA': str(value[4]).replace('"', ''),
                'SITUACAO_CADASTRAL': str(value[5]).replace('"', ''),
                'DATA_SITUACAO_CAD': str(data_sitcad),
                'MOTIVO_SITUACAO_CAD': str(value[7].replace('"', '')),
                'CIDADE_EXT': str(value[8]).replace('"', ''),
                'COD_PAIS': str(value[9]).replace('"', ''),
                'INICIO_ATIV': str(data_initativ),
                'CODIGO_CNAE_P': str(value[11]).replace('"', ''),
                'CODIGO_CNAE_S': str(value[12]).replace('"', ''),
                'TIPO_LOGRADOURO': str(value[13]).replace('"', ''),
                'NOME_LOGRADOURO': str(value[14]).replace('"', ''),
                'NUMERO_ESTABELEC': str(value[15]).replace('"', ''),
                'COMPLEMENTO': str(value[16]).replace('"', ''),
                'BAIRRO': str(value[17]).replace('"', ''),
                'CEP': str(value[18]).replace('"', ''),
                'UF': str(value[19]).replace('"', ''),
                'MUNICIPIO': str(value[20]).replace('"', ''),
                'TELEFONE_01': str("("+value[21]+")" + value[22]).replace('"', ''),
                'TELEFONE_02': str("("+value[23]+")" + value[24]).replace('"', ''),
                'FAX': str("("+value[25]+")" + value[26]).replace('"', ''),
                'E-MAIL': str(value[27]).replace('"', ''),
                'ESPECIAL': str(value[28]).replace('"', ''),
                'ESPECIAL_DATA': str(value[29]).replace('"', ''),
            }

            data_estab.insert_one(dataBloco)
            print("[!] Dados inseridos com sucesso!")

        except Exception:
            pass


        # necessario fazer o controle, 
        # caso contrario o PYTHON trava!

        # O CONTADOR > 1000 ESTÁ RETORNANDO 
        # ERRO, PROVAVEL ESTOURO DE MEMORIA, OU FALTA DELA...

        # OBS ::
        #       NEM SEMPRE OCORRE O ESTOURO/ERROR, 
        #       MAS PARA SEGURANÇA DO SCRIPT, 
        #       APENAS OS PRIMEIROS 2000 RESULTADOS SERAO COMPUTADOS.

        if contador > 2000:
            break

    arch.close()

    #return data_list

# BUSCANDO EMPRESAS COM SITUACAO 02(ATIVAS)
# E CALCULANDO A  % DO TOTAL NO ATLAS.
def busca_ativos():

    q = {"SITUACAO_CADASTRAL" : "02"}
    mysearch = data_estab.find(q)
    cont = 0
    cont_total = 0

    for doc in data_estab.find({}):
        cont_total += 1

    for x in mysearch:
        cont += 1
        #print(x)
    porc = int(cont / cont_total * 100)
    print("[!] Foram encontrados: "+ str(cont)+" resultados.")
    print("[!] De um total: "+ str(cont_total)+" resultados.")
    print("[!] O numero de empresas ativas é: ", str(round(porc)) +"%")

# FAZ UMA PESQUISA PELO CODIGO CNAE E ANO
def busca_res_ano():
    s = {"CODIGO_CNAE_P" : {"$regex" : "56.1"}}
    #d = {"INICIO_ATIV" : {"$regex" : "^2016"}}
    consult1 = data_estab.find(s)
    consult2 = data_estab.find(d)
    cont = 0
    cont_ano = 0
    data = []

    for r in consult1:
        cont += 1
        data += r
        print("[!] Encontrado um total: ", cont)
    
    #for z in consult2:
    #    cont_ano += 1
    #    print("[!] Abertos em 2016: ", cont_ano)

#!! ESSA FUNÇÃO RETORNA ERROR !!
# A FUNCAO EXPORT NÃO EXPORTA!
# NECESSARIO MELHOR REFORMULACAO E CORRECAO DE ERROS.
def export():
    data = []
    for doc in data_estab.find({}):
        data += doc
    
    sv = pd.DataFrame.to_dict(data)
    
    file_name = "data_001"

    #salvando em excel
    sv.to_excel(file_name)

def main(arq):

    ctr = True
    while ctr:
        print("""
        [@] MENU :: ESCOLHA UMA DAS OPCOES ABAIXO.\n
        ------------------------------------------------
        [!] 1. Subir dados processados.
        [!] 2  Numero de empresas ativas.
        [!] 3. Numero de empresas < restaurantes >.
        [!] 4. Exportar dados < CSV/Excel >.
        [!] 5. Encerrar script.
        """)
        opc = input("[!] Qual das opcoes gostaria de chamar? : ")
        if opc == "1":
            manager(arq)
        elif opc == "2":
            busca_ativos()
            break
        elif opc == "3":
            #busca_res_ano()
            print("[!] Necessaria correcao na funcao... opc bloqueada.")
        elif opc == "4":
            #export()
            print("[!] Necessaria correcao na funcao... opc bloqueada.")
            break
        elif opc == "5":
            print("[!] Encerrando script...")
            break
    

if __name__ == '__main__':
    main(arquivo)