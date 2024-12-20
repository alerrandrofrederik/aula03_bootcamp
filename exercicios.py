### Exercício 1: Verificação de Qualidade de Dados
# Você está analisando um conjunto de dados de vendas e precisa garantir 
# que todos os registros tenham valores positivos para `quantidade` e `preço`. 
# Escreva um programa que verifique esses campos e imprima "Dados válidos" se ambos 
# forem positivos ou "Dados inválidos" caso contrário.

# vendas = [
#     {"valor": 2, "quantidade": 5},
#     {"valor": -2, "quantidade": 5},
#     {"valor": 1, "quantidade": 15},
#     {"valor": 2, "quantidade": -5},
# ]

# vendas_validas = []

# for venda in vendas:
#     if venda["valor"] > 0 and venda["quantidade"] > 0:
#         vendas_validas.append(venda)
#         print("Dados válidos")
#     else:
#         print("Dados inválidos")

# print(vendas_validas)



### Exercício 2: Classificação de Dados de Sensor
# Imagine que você está trabalhando com dados de sensores IoT. 
# Os dados incluem medições de temperatura. Você precisa classificar cada leitura 
# como 'Baixa', 'Normal' ou 'Alta'. Considerando que:

# - 0 <= temperatura <= 20: 'Baixa'
# - 21 <= temperatura <= 40: 'Normal'
# - temperatura > 40: 'Alta'

# Escreva um programa que classifique cada leitura e imprima 'Baixa', 'Normal' ou 'Alta'.

# registros_temperatura = [
#     {"temperatura": 0},
#     {"temperatura": 5},
#     {"temperatura": 10},
#     {"temperatura": 15},
#     {"temperatura": 20},
#     {"temperatura": 25},
#     {"temperatura": 30},
#     {"temperatura": 35},
#     {"temperatura": 40},
#     {"temperatura": 45}
# ]

# for registro in registros_temperatura:
#     if registro["temperatura"] <= 20:
#         print("Baixa")
#     elif registro["temperatura"] <= 40:
#         print("Normal")
#     else:
#         print("Alta")

### Exercício 3: Filtragem de Logs por Severidade
# Você está analisando logs de uma aplicação e precisa filtrar mensagens 
# com severidade 'ERROR'. Dado um registro de log em formato de dicionário 
# como `log = {'timestamp': '2021-06-23 10:00:00', 'level': 'ERROR', 'message': 'Falha na conexão'}`, 
# escreva um programa que imprima a mensagem se a severidade for 'ERROR'.

# log = [{'timestamp': '2021-06-23 10:00:00', 'level': 'ERROR', 'message': 'Falha na conexão'},
#     {'timestamp': '2021-06-23 10:00:00', 'level': 'INFO', 'message': 'Conexão estabelecida'},
#     {'timestamp': '2021-06-23 10:00:00', 'level': 'ERROR', 'message': 'Falha na conexão'}]

# for log in log:
#     if log["level"] == "ERROR":
#         print(log["message"])
#     else:
#         print("Nenhuma mensagem de erro encontrada")


### Exercício 4: Validação de Dados de Entrada
# Antes de processar os dados de usuários em um sistema de recomendação, 
# você precisa garantir que cada usuário tenha idade entre 18 e 65 anos e tenha 
# fornecido um email válido. Escreva um programa que valide essas condições 
# e imprima "Dados de usuário válidos" ou o erro específico encontrado.

# usuarios = [
#     {"idade": 15, "email": "a@a.com"},
#     {"idade": 19, "email": "b_b.com"},
#     {"idade": 20, "email": "c@c.com"},
#     {"idade": 67, "email": "d@d_com"}
# ]

# for usuario in usuarios:
#     if usuario["idade"] >= 18 and usuario["idade"] <= 65 and "@" in usuario["email"]:
#         print("Dados de usuário válidos")
#     else:
#         print("Dados de usuário inválidos")


### Exercício 5: Detecção de Anomalias em Dados de Transações
# Você está trabalhando em um sistema de detecção de fraude e precisa identificar 
# transações suspeitas. Uma transação é considerada suspeita se o valor for superior 
# a R$ 10.000 ou se ocorrer fora do horário comercial (antes das 9h ou depois das 18h). 
# Dada uma transação como `transacao = {'valor': 12000, 'horario': 20}`, verifique se ela é suspeita.

transacoes = [
    {'valor': 12000, 'horario': 20},
    {'valor': 10000, 'horario': 10},
    {'valor': 8000, 'horario': 15},
    {'valor': 5000, 'horario': 8}
]

for transacao in transacoes:
    if transacao["valor"] > 10000 or int(transacao['horario']) < 9 or int(transacao['horario'] > 18):
        print("Transação suspeita")
    else:
        print("Transação normal")


### Exercício 6. Contagem de Palavras em Textos
# Objetivo:** Dado um texto, contar quantas vezes cada palavra única aparece nele.

### Exercício 7. Normalização de Dados
# Objetivo:** Normalizar uma lista de números para que fiquem na escala de 0 a 1.

### Exercício 8. Filtragem de Dados Faltantes
# Objetivo:** Dada uma lista de dicionários representando dados de usuários, filtrar aqueles que têm um campo específico faltando

### Exercício 9. Extração de Subconjuntos de Dados
# Objetivo:** Dada uma lista de números, extrair apenas aqueles que são pares.

### Exercício 10. Agregação de Dados por Categoria
# Objetivo:** Dado um conjunto de registros de vendas, calcular o total de vendas por categoria.

### Exercícios com WHILE

### Exercício 11. Leitura de Dados até Flag
# Ler dados de entrada até que uma palavra-chave específica ("sair") seja fornecida.

### Exercício 12. Validação de Entrada
# Solicitar ao usuário um número dentro de um intervalo específico até que a entrada seja válida.

### Exercício 13. Consumo de API Simulado
# Simular o consumo de uma API paginada, onde cada "página" de dados é processada em loop até que não haja mais páginas.

### Exercício 14. Tentativas de Conexão
# Simular tentativas de reconexão a um serviço com um limite máximo de tentativas.

### Exercício 15. Processamento de Dados com Condição de Parada
# Processar itens de uma lista até encontrar um valor específico que indica a parada.