# ExportaFormularioReferenciaCVM
Projeto de exporta dados dos membros de comitê do formulário de referência da Comissão de Valores Mobiliários (CMV) Brasil

Prerequisitos

Instalação do Python versão 3 e do pip
https://python.org.br/instalacao-windows/

Instalação das bibliotecas

pip install -r requirements.txt


Execução

python etl.py ano_inicial ano_final

python etl.py 2010 2020



Lembrando, que os dados só estão disponíveis a partir do ano de 2010, demais itens do formulário de referência entraram em versões futuras.
