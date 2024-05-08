import os
import pandas as pd

def juntar_csv(diretorio, nome_saida='file.csv'):
    
    if not os.path.exists(diretorio):
        print(f'O diretório {diretorio} não existe.')
        return

    
    arquivos_csv = [arquivo for arquivo in os.listdir(diretorio) if arquivo.endswith('.csv')]

    # Verifica se há pelo menos dois arquivos para juntar
    if len(arquivos_csv) < 2:
        print('Pelo menos dois arquivos CSV são necessários para a junção.')
        return

    
    dados_combinados = pd.DataFrame()

  
    for arquivo in arquivos_csv:
        caminho_arquivo = os.path.join(diretorio, arquivo)
        dados_arquivo = pd.read_csv(caminho_arquivo)
        dados_combinados = pd.concat([dados_combinados, dados_arquivo], ignore_index=True)

    
    caminho_saida = os.path.join(diretorio, nome_saida)
    dados_combinados.to_csv(caminho_saida, index=False)

    print(f'A junção dos arquivos CSV foi concluída. Os dados foram salvos em {caminho_saida}.')


diretorio_dos_csv = r'caminho/dos/varios/csv'
juntar_csv(diretorio_dos_csv)
