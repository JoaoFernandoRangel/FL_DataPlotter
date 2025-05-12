import matplotlib
matplotlib.use('TkAgg')  # Esta linha deve vir ANTES do plt import
import pandas as pd
import matplotlib.pyplot as plt

# [Restante do seu código permanece igual...]
# Configuração para exibir gráficos no Jupyter Notebook (se necessário)
# %matplotlib inline

# Caminhos dos arquivos
SDCARD_FILTERED = "./dados-para-analise/sdcard-toplot-filtered.csv"
SMARTHUB = "./dados-para-analise/smarthub-toplot.csv"

# Carregar os dados com tratamento de erros
try:
    df_sdcard = pd.read_csv(SDCARD_FILTERED, sep=";", decimal=",", encoding="latin1")
    df_smarthub = pd.read_csv(SMARTHUB, sep=";", decimal=",", encoding="latin1")
    
    # # Verificar os dados carregados
    # print("Dados SDCard (primeiras linhas):")
    # print(df_sdcard.head())
    # print("\nDados SmartHub (primeiras linhas):")
    # print(df_smarthub.head())
    
except Exception as e: 
    print(f"Erro ao carregar os arquivos: {e}")
    exit()

def plot_value(df, nome_do_eixo_x, nome_do_eixo_y):
    plt.figure(figsize=(12, 6))
    plt.plot(df[nome_do_eixo_x], df[nome_do_eixo_y], marker='o', linestyle='-', color='b')
    plt.xlabel(nome_do_eixo_x, fontsize=12)
    plt.ylabel(nome_do_eixo_y, fontsize=12)
    plt.title(f'{nome_do_eixo_y} vs {nome_do_eixo_x}', fontsize=14)
    plt.grid(True, linestyle='--', alpha=0.7)
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    
    # Adicionando uma mensagem caso não apareça o gráfico
    print("Exibindo gráfico... Se não aparecer, verifique seu ambiente de execução.")
    try:
        plt.show()
    except Exception as e:
        print(f"Erro ao mostrar gráfico: {e}")
    # Verificar se as colunas existem antes de plotar

# Imprimir os 50 primeiros valores da coluna "timestamp"
print(df_sdcard["timestamp"].size)
print(df_smarthub["timestamp"].size)
