import requests
import sys
import zipfile
import pandas as pd

# Download dos arquivos

ano_inicio = int(sys.argv[1])
ano_fim = int(sys.argv[2])

dffinal = pd.DataFrame()

ano_download = ano_inicio
while ano_download <= ano_fim:
    url = 'https://dados.cvm.gov.br/dados/CIA_ABERTA/DOC/FRE/DADOS/' + 'fre_cia_aberta_' + str(ano_download) + '.zip'
    r = requests.get(url, allow_redirects=True)
    with open('fre_cia_aberta_' + str(ano_download) + '.zip', 'wb') as f:
        f.write(r.content)
        with zipfile.ZipFile('fre_cia_aberta_' + str(ano_download) + '.zip') as z:
            with z.open('fre_cia_aberta_membro_comite_' + str(ano_download) + '.csv') as f:
                df = pd.read_csv(f, sep=';', encoding='latin-1')
                df["ano_public"] = str(ano_download)
                dffinal = pd.concat([dffinal, df], ignore_index=True)

    ano_download += 1
else:
    nome_arquivo = 'membro-comite_' + str(ano_inicio) + '_' + str(ano_fim)
    dffinal.to_excel(nome_arquivo + '.xlsx', engine='xlsxwriter')
    dffinal.to_csv(nome_arquivo + '.csv', mode='a', sep=';', encoding='latin-1', lineterminator='\r\n')
    print(f'Download e extração finalizada, veja os arquivos '
          + nome_arquivo + '.csv e ' + nome_arquivo
          + '.xlsx, no diretório de execução do arquivo etl.py!')
