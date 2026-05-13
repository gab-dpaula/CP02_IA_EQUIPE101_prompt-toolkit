def contar_tokens(texto):
    return len(texto.split())

def medir_acuracia(resposta, esperado):
    return 1 if resposta.strip().upper() == esperado.strip().upper() else 0

def medir_consistencia(respostas):
    return len(set(respostas)) / len(respostas)

def testar_temperatura(prompt, temps):
    return {t: f"Rodado com temp={t}" for t in temps}