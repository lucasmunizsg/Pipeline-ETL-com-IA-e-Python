# Utilize sua própria URL se quiser ;)
# Repositório da API: https://github.com/digitalinnovationone/santander-dev-week-2023-api
# Documentação Oficial da API OpenAI: https://platform.openai.com/docs/api-reference/introduction
# Informações sobre o Período Gratuito: https://help.openai.com/en/articles/4936830

# Para gerar uma API Key:
# 1. Crie uma conta na OpenAI
# 2. Acesse a seção "API Keys"
# 3. Clique em "Create API Key"
# Link direto: https://platform.openai.com/account/api-keys
sdw2023_api_url = 'https://sdw-2023-prd.up.railway.app'

import pandas as pd
import requests
import json
# import openai


df = pd.read_csv('SDW2023.csv')
user_ids = df['UserID'].tolist()
print(user_ids)


def get_user(id):
  response = requests.get(f'{sdw2023_api_url}/users/{id}')
  return response.json() if response.status_code == 200 else None

users = [user for id in user_ids if (user := get_user(id)) is not None]
print(json.dumps(users, indent=2))

def update_user(user):
    response = requests.put(f"{sdw2023_api_url}/users/{user['id']}", json=user)
    return True if response.status_code == 200 else False

for user in users:
  success = update_user(user)
  print(f"User {user['name']} updated? {success}!")

# OPÇÃO COM API DA DEEP IA
import requests
r = requests.post(
    "https://api.deepai.org/api/text-generator",
    data={
        'text': "Crie uma mensagem para {user['name']} sobre a importância dos investimentos (máximo de 100 caracteres)",
    },
    headers={'api-key': 'quickstart-QUdJIGlzIGNvbWluZy4uLi4K'}
)
print(r.json())
# =====================================================================




# OPÇÃO COM A API DA OPENAI
# openai_api_key = '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'

# openai.api_key = openai_api_key

# def generate_ai_news(user):
#   completion = openai.ChatCompletion.create(
#     model="gpt-4",
#     messages=[
#       {
#           "role": "system",
#           "content": "Você é um especialista em markting bancário."
#       },
#       {
#           "role": "user",
#           "content": f"Crie uma mensagem para {user['name']} sobre a importância dos investimentos (máximo de 100 caracteres)"
#       }
#     ]
#   )
#   return completion.choices[0].message.content.strip('\"')

# for user in users:
#   news = generate_ai_news(user)
#   print(news)
#   user['news'].append({
#       "icon": "https://digitalinnovationone.github.io/santander-dev-week-2023-api/icons/credit.svg",
#       "description": news
#   })