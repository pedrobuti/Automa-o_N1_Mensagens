import time

# Código realizado para automatizar e facilitar a equipe de N1 na resposta de chamados na plataforma JIRA #

# Texto de Bem-vindo e apresentação das opções de indisponibilidade
print("Olá, seja bem-vindo ao programa de automação.")
print("1- Indisponibilidade de Energia")
print("2- Indisponibilidade de Link")
print("3- Indisponibilidade Interna")

# Solicita uma resposta do usuário para as indisponibilidades
resposta = int(input("Selecione: "))

# Caso seja problema de energia
if resposta == 1:
    unidade_energia = input("Qual unidade está com essa indisponibilidade? Informe: ")

    print("O problema está relacionado com a Copel?\n1- Sim\n2- Não")
    relacionado_copel = int(input("Selecione: "))

    if resposta == 1:
        relacionado_copel = True, "está relacionado" 
    else:
        relacionado_copel = "não está relacionado"

    if relacionado_copel == "está relacionado":
        print("A unidade já entrou em contato com a Copel?\n1- Sim\n2- Não")
        unidade_entrou_contato = int(input("Selecione: "))

        if unidade_entrou_contato == 1:
            unidade_entrou_contato = "entrou em contato"
        else:
            unidade_entrou_contato = "não entrou em contato"

        if unidade_entrou_contato == "entrou em contato":
            resolucao_problema_energia = True
        else:
            resolucao_problema_energia = False

        if resolucao_problema_energia == True:
            resposta_problema_energia = input('Informe o prazo abaixo da seguinte forma: "X"hrs\nExemplo: 8hrs\nPrazo: ')

        if unidade_entrou_contato == "entrou em contato":
            print("Foi dado um motivo para o problema? \n 1- Sim \n 2- Não")
            motivo_problema_energia = int(input("Selecione: "))

            if motivo_problema_energia == 1:
                motivo_problema_energia = True
            else:
                motivo_problema_energia = False
            
            if motivo_problema_energia == True:
                resposta_motivo_problema_energia = input("Qual a justificativa do problema? Nos informe: ")
            else:
                pass

            print("Aguarde, estamos processando seu chamado!")
            time.sleep(5)
            print("Chamado gerado!")

            print(
                f"Após analisarmos a unidade de {unidade_energia}, entramos em contato com os colaboradores e "
                f"foi nos passado as seguintes informações: A unidade está sem energia e o problema {relacionado_copel} a Copel.\n"
                f"A unidade de {unidade_energia} já entrou em contato com a copel.")
            
            if resolucao_problema_energia == True:
                print (f"O prazo para resolução é de {resposta_problema_energia}")
            else:
                print (f"Não foi definido um prazo para resolução")
            if motivo_problema_energia == True:
                print (f"{resposta_motivo_problema_energia} informado o motivo para a indisponibilidade")
