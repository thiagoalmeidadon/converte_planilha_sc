import pandas as pd
import sys
from pandas import ExcelWriter

nome_arquivo = sys.argv[1]
arquivo_final = f'{sys.argv[2]}_ranking.xlsx'

def importar_dados_planilha(nome_arquivo, arquivo_final):
    player = []
    score = []
    ranking = pd.read_excel(nome_arquivo, sheet_name="Final Scores",
                            skiprows=range(0,2))
    for i in range(0, len(ranking)):
        player.append(ranking["Player"][i])
        score.append(ranking["Total Score (points)"][i])
    
    df = pd.DataFrame({'Player' : player, 'Total Score' : score })
    with ExcelWriter(arquivo_final, engine="openpyxl", mode="w") as w:
        df.to_excel(w, 'Ranking', index=False)

if __name__=='__main__':
    argc = len(sys.argv)
    if argc < 3:
        print(f'Modo de uso:\n\t python3 {sys.argv[0]}.py nome_planilha nome_arquivo_final')
        sys.exit()

    importar_dados_planilha(nome_arquivo, arquivo_final)