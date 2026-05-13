import json
from src import tasks, techniques, evaluator, report, prompt_builder
from src.llm_client import LLMClient   # importa a classe corretamente

def main():
    # Criar instância do cliente LLM
    client = LLMClient()

    # 1. Carregar inputs
    with open("data/inputs.json", "r", encoding="utf-8") as f:
        inputs = json.load(f)

    resultados = []

    # 2. Executar tarefas
    for tarefa_nome, lista_inputs in inputs.items():
        tarefa = tasks.TAREFAS[tarefa_nome]
        for entrada in lista_inputs:
            for tecnica in [
                techniques.zero_shot,
                techniques.few_shot,
                techniques.chain_of_thought,
                techniques.role_prompting
            ]:
                # Monta prompt com a técnica
                prompt = tecnica(tarefa, entrada["input"])

                # Chama o LLM corretamente
                resposta = client.chat(prompt)

                # Avalia resultado
                avaliacao = evaluator.medir_acuracia(resposta["resposta"], entrada["esperado"])

                resultados.append({
                    "tarefa": tarefa_nome,
                    "input": entrada["input"],
                    "tecnica": tecnica.__name__,
                    "resposta": resposta["resposta"],
                    "tokens": resposta["tokens_resposta"],
                    "tempo_ms": resposta["tempo_ms"],
                    "acuracia": avaliacao
                })

    # 3. Gerar relatório
    report.gerar_tabela(resultados)
    report.grafico_acuracia(resultados)
    report.grafico_custo(resultados)
    report.recomendar(resultados)

if __name__ == "__main__":
    main()