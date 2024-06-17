import requests
import sys
import zipfile
import pandas as pd

# Download dos arquivos

ano_inicio = int(sys.argv[1])
ano_fim = int(sys.argv[2])

dffinal = pd.DataFrame()
dffinal1 = pd.DataFrame()

ano_download = ano_inicio
while ano_download <= ano_fim:
    url = 'https://dados.cvm.gov.br/dados/CIA_ABERTA/DOC/FRE/DADOS/' + 'fre_cia_aberta_' + str(ano_download) + '.zip'
    r = requests.get(url, allow_redirects=True)
    with open('fre_cia_aberta_' + str(ano_download) + '.zip', 'wb') as f:
        f.write(r.content)
        with zipfile.ZipFile('fre_cia_aberta_' + str(ano_download) + '.zip') as z:
            with z.open('fre_cia_aberta_membro_comite_' + str(ano_download) + '.csv') as file:
                df = pd.read_csv(file, sep=';', encoding='ANSI')
                
                df["ano_public"] = str(ano_download)
                dffinal = pd.concat([dffinal, df], ignore_index=True)
                
        
            with z.open('fre_cia_aberta_administrador_membro_conselho_fiscal_' + str(ano_download) + '.csv') as file1:
                df1 = pd.read_csv(file1, sep=';', encoding='ANSI')
                
                df1["ano_public"] = str(ano_download)
                dffinal1 = pd.concat([dffinal1, df1], ignore_index=True)
                
    ano_download += 1
else:
    nome_arquivo = 'membro-comite_' + str(ano_inicio) + '_' + str(ano_fim)
    dffinal.to_excel(nome_arquivo + '.xlsx', engine='xlsxwriter')
    dffinal.to_csv(nome_arquivo + '.csv', mode='a', sep=';', encoding='ANSI', lineterminator='\r\n')
    nome_arquivo1 = 'administrador_membro_conselho_fiscal_' + str(ano_inicio) + '_' + str(ano_fim)
    dffinal1.to_excel(nome_arquivo1 + '.xlsx', engine='xlsxwriter')
    dffinal1.to_csv(nome_arquivo1 + '.csv', mode='a', sep=';', encoding='ANSI', lineterminator='\r\n')
    print('Download e extração finalizada, veja os arquivos '
          + nome_arquivo + '.csv, ' + nome_arquivo
          + '.xlsx, ' + nome_arquivo1 + '.csv, e ' + nome_arquivo1 + 
          '.xlsx, no diretório de execução do arquivo etl.py!') 
    