import os
import json
from google import genai

with open('sample_logs.json', 'r') as file:
    logs = json.load(file)

client = genai.Client()

prompt = f"""
Você é um especialista em cibersegurança e análise de logs.
Analise os seguintes logs de acesso em formato JSON e identifique se há alguma atividade suspeita.

Logs:
{json.dumps(logs, indent=2)}

Sua resposta deve conter:
1. Resumo dos eventos analisados.
2. Identificação de ameaças (se houver) com o nível de risco (Baixo, Médio ou Alto).
3. Recomendação de ação de segurança preventiva.
"""

response = client.models.generate_content(
    model='gemini-3.8-flash',
    contents=prompt,
)

print("=== RELATÓRIO DE ANÁLISE DE SEGURANÇA VIA IA ===\n")
print(response.text)