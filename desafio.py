

# nome = input("digite seu nome: ")
# salario = float(input("digite seu salario: "))
# bonus_percentual = float(input("digite o percentual de bonus: "))
# kpi = 1000 + salario * bonus_percentual

# print(f"Olá {nome}, seu bônus foi de {kpi}")

#Integre na solução anterior um fluxo de While que repita o fluxo até que o usuário insira as informações corretas

nome_valido = False
salario_valido = False
bonus_valido = False

while not nome_valido:
    try:
        nome = input("digite o seu nome: ")
        nome = nome.strip()
        if len(nome) == 0:
            print("nome invalido, nenhum caracter foi digitado")
        elif any(char.isdigit() for char in nome):
            print("nome invalido, contem um caracter numerico")
        else:
            nome_valido = True
            print("nome valido")
    except:
        print("nome invalido, digite seu nome corretamente")
        nome_valido = False

while not salario_valido:
    try:
        salario = float(input("digite seu salário: "))
        if salario < 0:
            print("salário invalido, digite um salário positivo")
        else:
            salario_valido = True
            print("salário valido")
    except:
        print("Salario invalido digite seu salário corretamente! ")
        salario_valido = False

while not bonus_valido:
    try:
        bonus = float(input("digite seu percentual de bonus: "))
        if salario < 0:
            print("valor invalido, digite um % de bonus positivo")
        else:
            bonus_valido = True
            print("bonus valido")
    except:
        print("bonus invalido digite seu spercentual de bonus corretamente! ")
        bonus_valido = False

kpi = (1000 + salario) * bonus

print(f"Olá {nome}, como seu salário foi de {salario} e o valor do bonus percentual foi a {bonus}, seu bônus foi de {kpi}")


        