TAREFAS = {
    "classificacao_sentimento": {
        "nome": "classificacao_sentimento",
        "tipo": "classificacao",
        "instrucao": "Classifique como POSITIVO, NEGATIVO, NEUTRO OU MISTO",
        "formato_output": "Responda APENAS com a classificacao",
        "exemplos_fewshot": [
            {"input": "Adorei!", "output": "POSITIVO"},
            {"input": "Péssimo.", "output": "NEGATIVO"}
        ],
        "passos_cot": ["Identifique aspectos positivos", "Identifique aspectos negativos", "Compare e classifique"],
        "persona": "analista_cx"
    }
}