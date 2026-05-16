import json

exemplos = {}

personas = {}

with open("data/examples.json", "r", encoding="utf-8") as f:
    exemplos = json.load(f)

with open("prompts/system_prompts.json", "r", encoding="utf-8") as f:
    personas = json.load(f)

TAREFAS = {
    "classificacao_sentimento": {
        "nome": "classificacao_sentimento",
        "tipo": "classificacao",
        "instrucao": "Classifique o texto seguinte como POSITIVO, NEGATIVO ou NEUTRO",
        "formato_output": "Responda APENAS com a classificacao",
        "exemplos_fewshot": exemplos["classificacao_sentimento"],
        "passos_cot": ["Identifique aspectos positivos", "Identifique aspectos negativos", "Compare e classifique"],
        "persona": personas["classificacao_sentimento"]
    },
    "extracao_problema": {
        "nome": "extracao",
        "tipo": "extracao",
        "formato_output": "siga o seguinte formato: { 'produto': string, 'periodo': 'INICIAL'|'POSTERIOR', 'problema': string }, apenas mande um json sem nenhum tipo de formatação",
        "instrucao": "você receberá um texto relatando um problema referente a um produto, extraia o nome do produto, o problema principal e a periodo que a falha veio a ocorrer, INICIAL, logo na chegada, ou POSTERIOR, a partir de alguns dias de uso",
        "exemplos_fewshot": exemplos["extracao_problema"],
        "passos_cot": ["identifique o produto", "extraia o problema central", "descubra se o produto já veio com defeito ou foi após um periodo de uso"],
        "persona": personas["extracao_problema"]
    },
    "sumarizacao_descricao": {
        "nome": "sumarizacao_descricao",
        "tipo": "sumarizacao",
        "max_tokens": 150,
        "formato_output": """responda apenas em texto simples em uma única linha, o resumo deve ser menor que a descrição original""",
        "instrucao": "faça um resumo da descrição desse produto, mantenha todos os dados importantes, tenha foco em apresentar o nome do produto e seus dados",
        "exemplos_fewshot": exemplos["sumarizacao_descricao"],
        "passos_cot": ["identifique os dados de maior interesse", "mostre o nome do produto primeiro", "comece a abordar seus dados"],
        "persona": personas["sumarizacao_descricao"]
    },
    
}


# classifacação de exercicios em materias escolas
# extração de conhecimentos (pega um curriculo e extrai os conhecimentos)
# 