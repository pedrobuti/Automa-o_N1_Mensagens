import time

#Código realizado para automatizar e facilitar a equipe de N1 na resposta de chamados na plataforma JIRA #

# Texto de Bem vindo e apresenta as opções de indisponibilidade
print ("Olá, seja bem-vindo ao programa de automação.")
print ("1- Indisponibilidade de Energia")
print ("2- Indisponibilidade de Link")
print ("3- Indisponibilidade Interna")

# ---------------------------------------------------------------------------------------------------- #

# Solicita uma resposta do usuário para as indisponibilidades
resposta1 = print(input("Selecione:"))

# ----------------------------------------------------------------------------------------------------- #

# Caso seja problema de energia
if resposta1 == 1:
    print("Qual unidade está com essa indisponibilidade?")
    unidade_energia = input("Informe:")

if resposta1 == 1 :
    print("O problema está relacionado com a Copel?\n",
                                    "1- Sim\n",
                                    "2- Não\n")
    relacionado_copel = print (input("Selecione:"))


if relacionado_copel == 1:
    relacionado_copel = "está relacionado"
else:
    relacionado_copel = "não está relacionado"


if relacionado_copel == "está relacionado":
    print("A unidade já entrou em contato com a Copel? \n",
                                    "1- Sim\n",
                                    "2- Não\n")
    unidade_entrou_contato = print (input("Selecione:"))


if unidade_entrou_contato == 1:
    unidade_entrou_contato = "entrou em contato"
else:
    unidade_entrou_contato = "não entrou em contato"


if unidade_entrou_contato == "entrou em contato":
    print('Foi informado um prazo de resolução para o problema?\n',
            'Informe o prazo abaixo da seguinte forma: "X"hrs',
            'Exemplo: 8hrs')
    resolucao_problema_energia = print(input("Prazo:"))

    print ("Foi dado um motivo para o problema?\n",
                                    "1- Sim\n",
                                    "2- Não")   
    motivo_problema_energia = print(input("Selecione:"))

if motivo_problema_energia == 1:
    motivo_problema_energia = "foi"
else:
    motivo_problema_energia = "Não foi"

if motivo_problema_energia == "foi":
    print('Qual a justificativa do problema?')
    motivo_escrito_problema_energia = print(input("Nos informe:"))

    print("Aguarde, estamos processando seu chamado!")
    time.sleep(5)
    print("Chamado gerado!")

    print("Após analisarmos a unidade -", unidade_energia , "- , entramos em contato com os colaboradores e foi nos passado as seguintes informações:",
        "A unidade está sem energia, o problema", relacionado_copel , "com a copel, a unidade", unidade_entrou_contato , "com a mesma, e o prazo para resolução é de ", resolucao_problema_energia , " e ", motivo_problema_energia , "informado o motivo para a indisponibilidade")
    if motivo_problema_energia == "foi":
        print (motivo_escrito_problema_energia)