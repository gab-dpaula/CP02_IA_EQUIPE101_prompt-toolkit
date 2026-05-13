from src import prompt_builder
import json

def zero_shot(tarefa, input):
    return prompt_builder.montar_prompt(tarefa["instrucao"], "", input, tarefa["formato_output"])

def few_shot(tarefa, input):
    with open("data/examples.json", "r", encoding="utf-8") as f:
        exemplos = json.load(f)[tarefa["nome"]]
    prompt = prompt_builder.montar_prompt(tarefa["instrucao"], "", input, tarefa["formato_output"])
    return prompt_builder.adicionar_exemplos(prompt, exemplos)

def chain_of_thought(tarefa, input):
    prompt = prompt_builder.montar_prompt(tarefa["instrucao"], "", input, tarefa["formato_output"])
    return prompt_builder.adicionar_cot(prompt, tarefa["passos_cot"])

def role_prompting(tarefa, input):
    with open("prompts/system_prompts.json", "r", encoding="utf-8") as f:
        personas = json.load(f)
    persona = personas[tarefa["persona"]]
    return f"SYSTEM: {persona}\nUSER: {input}"