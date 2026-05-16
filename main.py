import json
from src import tasks, techniques, evaluator, report, prompt_builder
from src.llm_client import LLMClient


def main():
    # Criar instância do cliente LLM
    client = LLMClient()

    def executar_tarefa(entrada, tarefa, tecnica, resultados, temperatura=0.5):
        prompt = tecnica(tarefa, entrada["input"])

                
        resposta = client.chat(prompt, temp=temperatura, max_tokens=tarefa["max_tokens"] if "max_tokens" in tarefa else 400 )

        avaliacao = evaluator.medir_acuracia(resposta["resposta"], entrada["esperado"])


        resultado = {
            "tarefa": tarefa["nome"],
            "input": entrada["input"],
            "tecnica": tecnica.__name__,
            "resposta": resposta["resposta"],
            "tokens": resposta["tokens_resposta"],
            "tempo_ms": resposta["tempo_ms"],
            "acuracia": avaliacao,
            "temperatura": temperatura
        }
        resultados.append(resultado)

        return resultado

    # 1. Carregar inputs
    with open("data/inputs.json", "r", encoding="utf-8") as f:
        inputs = json.load(f)

    resultados = []
    tecnicas = [
        techniques.zero_shot,
        techniques.few_shot,
        techniques.chain_of_thought,
        techniques.role_prompting
    ]

    
    # 2. Executar tarefas
    for tarefa_nome, lista_inputs in inputs.items():
        print(f"gerando respotas para a tarefa: {tarefa_nome}")
        tarefa = tasks.TAREFAS[tarefa_nome]
        resultados_tarefa = []
        for entrada in lista_inputs:
            print(f"respondendo o input: \"{entrada["input"]}\"")
            for tecnica in tecnicas:
                
                resultado =executar_tarefa(entrada, tarefa, tecnica, resultados)

                resultados_tarefa.append(resultado)

        
        report.grafico_acuracia(resultados_tarefa, f"{tarefa_nome}/")
        report.grafico_custo(resultados_tarefa, f"{tarefa_nome}/")

    # 3. Gerar relatório geral
    report.grafico_acuracia(resultados)
    report.grafico_custo(resultados)
    report.gerar_tabela(resultados)

    recomendado =  report.recomendar(resultados)
    tecnica = next(tecnica for tecnica in tecnicas if tecnica.__name__ == recomendado)
    temperaturas = [0.1, 0.5, 1]

    resultado_melhor = []
    # teste melhor tecnica
    for temperatura in temperaturas:
        for tarefa_nome, lista_inputs in inputs.items():
            print(f"gerando novas respostas para a tarefa {tarefa_nome} com a tecnica {recomendado} e com a temperatura {temperatura}")
            tarefa = tasks.TAREFAS[tarefa_nome]
            for entrada in lista_inputs:
                executar_tarefa(entrada, tarefa, tecnica, resultado_melhor, temperatura)

    report.grafico_temperatura(resultado_melhor)
if __name__ == "__main__":
    
    main()

# "classificacao_sentimento": [
#     { "input": "Produto excelente, chegou rápido!", "esperado": "POSITIVO" },
#     { "input": "Veio quebrado, péssimo.", "esperado": "NEGATIVO" },
#     { "input": "Bom preço mas qualidade média.", "esperado": "MISTO" },
#     { "input": "Entrega atrasada mas produto ok.", "esperado": "NEUTRO" },
#     { "input": "Gostei do atendimento, mas produto ruim.", "esperado": "MISTO" }
#   ],