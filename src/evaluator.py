import tiktoken
import json

def contar_tokens(texto):
    encoding = tiktoken.get_encoding("o200k_base")
 
    return len(encoding.encode(texto))
    
def comparar_objetos(obj1, obj2):
    for propriedade in obj1:
        if propriedade in obj2:
            continue
        return False
    return True

def medir_acuracia(resposta, esperado, tarefa = {}):
    if tarefa["tipo"] == "extracao":
        objeto = json.load(resposta)

        return comparar_objetos(esperado, objeto)
    if tarefa["tipo"] == "sumarizacao":
        contador = 0
        for palavra_chave in esperado:
            if palavra_chave in resposta:
                contador+= 1
        return contador == len(esperado)
    return 1 if resposta.strip().upper() == esperado.strip().upper() else 0

def medir_consistencia(respostas):
    return len(set(respostas)) / len(respostas)

def testar_temperatura(prompt, temps):
    return {t: f"Rodado com temp={t}" for t in temps}
