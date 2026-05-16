import tiktoken
import json

def contar_tokens(texto):
    encoding = tiktoken.get_encoding("o200k_base")
 
    return len(encoding.encode(texto))
    
def comparar_objetos(obj1, obj2):
    contador = 0
    for propriedade in obj1:
        
        if propriedade in obj2 and obj1[propriedade].upper() == obj2[propriedade].upper():
            contador += 1
    if contador == 0:
        return 0
    return contador / len(obj1)

def medir_acuracia(resposta, esperado):
    if type(esperado) is dict:
        try:
            return comparar_objetos( esperado, json.loads(resposta.strip()))
        except:
            return 0
    if type(esperado) is list:
        contador = 0
        for palavra_chave in esperado:
            if palavra_chave.upper() in resposta.upper():
                contador+= 1
        if contador == 0:
            return 0
        return  contador / len(esperado)
    return 1 if resposta.strip().upper() == esperado.strip().upper() else 0

def medir_consistencia(respostas):
    return len(set(respostas)) / len(respostas)

def testar_temperatura(prompt, temps):
    return {t: f"Rodado com temp={t}" for t in temps}
