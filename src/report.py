import pandas as pd
import matplotlib.pyplot as plt

def gerar_tabela(resultados):
    df = pd.DataFrame(resultados)
    df.to_csv("output/resultados.csv", index=False)
    print(df.head())

def grafico_acuracia(resultados):
    df = pd.DataFrame(resultados)
    df.groupby("tecnica")["acuracia"].mean().plot(kind="bar")
    plt.savefig("output/graficos/acuracia.png")

def grafico_custo(resultados):
    df = pd.DataFrame(resultados)
    df.groupby("tecnica")["tokens"].mean().plot(kind="bar")
    plt.savefig("output/graficos/custo.png")

def recomendar(resultados):
    df = pd.DataFrame(resultados)
    melhor = df.groupby("tecnica")["acuracia"].mean().idxmax()
    print(f"Melhor técnica: {melhor}")