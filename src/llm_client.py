from src.evaluator import contar_tokens
import requests, os

class LLMClient:
    def __init__(self):
        self.host = os.getenv("OLLAMA_HOST", "http://localhost:11434")

    def chat(self, prompt, system=None, temp=0.7, max_tokens=512):
        try:
            response = requests.post(
                f"{self.host}/api/generate",
                
                json={ "model": os.getenv("MODEL", "gpt-oss:120b"), "prompt": prompt, "think": False, "stream": False, "options": { "temperature": temp, "num_predict": max_tokens }},
                timeout=30
            )
            data = response.json()
            tempo = data.get("total_duration", 0)
            return {
                "resposta": data.get("response", ""),
                "tokens_prompt": contar_tokens(prompt),
                "tokens_resposta": contar_tokens(data.get("response", "")),
                "tempo_ms": tempo  / (10 ** 6) if tempo >0 else 0
            }
        except Exception as e:
            return {"resposta": f"Erro: {e}", "tokens_prompt": 0, "tokens_resposta": 0, "tempo_ms": 0}

llm_client = LLMClient()