import json

exemplos = {}

personas = {}

with open("data/examples.json", "r", encoding="utf-8") as f:
    print("exemplos")
    exemplos = json.load(f)
    print(exemplos)

with open("prompts/system_prompts.json", "r", encoding="utf-8") as f:
    personas = json.load(f)

TAREFAS = {
    "classificacao_sentimento": {
        "nome": "classificacao_sentimento",
        "tipo": "classificacao",
        "instrucao": "Classifique o texto seguinte como POSITIVO, NEGATIVO, NEUTRO OU MISTO",
        "formato_output": "Responda APENAS com a classificacao",
        "exemplos_fewshot": exemplos["classificacao_sentimento"],
        "passos_cot": ["Identifique aspectos positivos", "Identifique aspectos negativos", "Compare e classifique"],
        "persona": personas["analista_cx"]
    },
    "extracao": {
        "nome": "extracao",
        "tipo": "extracao",
        "instrucao": "",
        "exemplos_fewshot": exemplos["extracao"],
        "passos_cot": [],
        "persona": personas["extracao"]
    },
    "sumarizacao": {
        "nome": "sumarizacao",
        "tipo": "sumarizacao",
        "instrucao": "",
        "exemplos_fewshot": exemplos["sumarizacao"],
        "passos_cot": [],
        "persona": personas["sumarizacao"]
    }
}


# classifacação de exercicios em materias escolas
# extração de conhecimentos (pega um curriculo e extrai os conhecimentos)
# 