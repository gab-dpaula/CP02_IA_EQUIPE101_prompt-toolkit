import requests, os

class LLMClient:
    def __init__(self):
        self.host = os.getenv("OLLAMA_HOST", "http://localhost:11434")

    def chat(self, prompt, system=None, temp=0.7, max_tokens=512):
        try:
            response = requests.post(
                f"{self.host}/api/chat",
                json={"prompt": prompt, "system": system, "temperature": temp, "max_tokens": max_tokens},
                timeout=30
            )
            data = response.json()
            return {
                "resposta": data.get("response", ""),
                "tokens_prompt": len(prompt.split()),
                "tokens_resposta": len(data.get("response", "").split()),
                "tempo_ms": data.get("time", 0)
            }
        except Exception as e:
            return {"resposta": f"Erro: {e}", "tokens_prompt": 0, "tokens_resposta": 0, "tempo_ms": 0}

llm_client = LLMClient()