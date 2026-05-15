def montar_prompt(instrucao, input_dados, formato_output):
    if not instrucao or not input_dados or not formato_output:
        raise ValueError("Prompt incompleto")
    return f"{instrucao}\nInput: {input_dados}\nOutput esperado: {formato_output}"

def adicionar_exemplos(prompt, exemplos):
    return prompt + "\nExemplos:\n" + "\n".join([f"Input: {e['input']} -> Output: {e['output']}" for e in exemplos])

def adicionar_cot(prompt, passos):
    return prompt + "\nRaciocínio passo a passo:\n" + "\n".join(passos)