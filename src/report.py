import pandas as pd
import matplotlib.pyplot as plt


def gerar_tabela(resultados):
    df = pd.DataFrame(resultados)
    df.to_csv("output/resultados.csv", index=False)
    print(df.sort_values("acuracia").head(100))

def grafico_acuracia(resultados, subpasta=""):

    df = pd.DataFrame(resultados)
    df = df.replace("zero_shot", "zero")
    df = df.replace("few_shot", "few")
    df = df.replace("chain_of_thought", "chain")
    df = df.replace("role_prompting", "role")
    df.groupby("tecnica")["acuracia"].mean().plot(kind="bar")
    plt.ylim(0, 1)
    plt.ylabel("acuracia")
    plt.xlabel("tecnicas")
    
    plt.savefig(f"output/graficos/{subpasta}acuracia.png", pad_inches=1, orientation="portrait")
    plt.close()

def grafico_custo(resultados, subpasta=""):
    df = pd.DataFrame(resultados)
    df = pd.DataFrame(resultados)
    df = df.replace("zero_shot", "zero")
    df = df.replace("few_shot", "few")
    df = df.replace("chain_of_thought", "chain")
    df = df.replace("role_prompting", "role")
    df.groupby("tecnica")["tokens"].mean().plot(kind="bar")
    plt.xlabel("tecnicas")
    plt.ylabel("tokens")
    plt.savefig(f"output/graficos/{subpasta}custo.png", pad_inches=1)
    plt.close()

def grafico_temperatura(resultados):
    df = pd.DataFrame(resultados)
    df.groupby("temperatura")["acuracia"].mean().plot(kind="bar")
    
    plt.ylim(0, 1)
    plt.ylabel("acuracia")
    plt.savefig("output/graficos/temperatura.png", pad_inches=1)
    plt.close()


def recomendar(resultados):
    df = pd.DataFrame(resultados)
    melhor = df.groupby("tecnica")["acuracia"].mean().idxmax()
    print(f"Melhor técnica: {melhor}(maior acuracia apresentada)")

    return melhor