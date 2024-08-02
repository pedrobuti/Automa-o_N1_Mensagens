#Código realizado para automatizar e facilitar a equipe de N1 na resposta de chamados na plataforma JIRA #

# Texto de Bem vindo e apresenta as opções de indisponibilidade
print ("Olá, seja bem-vindo ao programa de automação.")
print ("1- Indisponibilidade de Energia")
print ("2- Indisponibilidade de Link")
print ("3- Indisponibilidade Interna")

# Solicita uma resposta do usuário para as indisponibilidades
resposta1 = print(input("Selecione:"))

# Caso seja problema de energia
if resposta1 == 1 :
    resposta1_energia = print(input("O problema está relacionado com a Copel?",
                                    "1- Sim",
                                    "2- Não"))
    
if resposta1_energia == 1:
    resposta2_a = print(input("Os colaboradores da unidade já entraram em contato com a Copel?",
                                "1- Sim",
                                "2- Não"))
    
# Caso seja problema de Link
    if resposta1 == 2:
        resposta1_link = print(input(""))