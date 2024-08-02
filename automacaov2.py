import time

# Código realizado para automatizar e facilitar a equipe de N1 na resposta de chamados na plataforma JIRA #

# Texto de Bem-vindo e apresentação das opções de indisponibilidade
print("Olá, seja bem-vindo ao programa de automação.")
print("1- Indisponibilidade de Energia")
print("2- Indisponibilidade de Link")
print("3- Indisponibilidade Interna")

# Solicita uma resposta do usuário para as indisponibilidades
resposta1 = int(input("Selecione: "))

# Caso seja problema de energia
if resposta1 == 1:
    unidade_energia = input("Qual unidade está com essa indisponibilidade? Informe: ")

    print("O problema está relacionado com a Copel?\n1- Sim\n2- Não")
    relacionado_copel = int(input("Selecione: "))

    if relacionado_copel == 1:
        relacionado_copel = "está relacionado"
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
            resolucao_problema_energia = input(
                'Foi informado um prazo de resolução para o problema?\nInforme o prazo abaixo da seguinte forma: "X"hrs\nExemplo: 8hrs\nPrazo: '
            )

            print("Foi dado um motivo para o problema?\n1- Sim\n2- Não")
            motivo_problema_energia = int(input("Selecione: "))

            if motivo_problema_energia == 1:
                motivo_problema_energia = "foi"
                motivo_escrito_problema_energia = input("Qual a justificativa do problema? Nos informe: ")
            else:
                motivo_problema_energia = "não foi"

            print("Aguarde, estamos processando seu chamado!")
            time.sleep(5)
            print("Chamado gerado!")

            print(
                f"Após analisarmos a unidade {unidade_energia}, entramos em contato com os colaboradores e "
                f"foi nos passado as seguintes informações: A unidade está sem energia, o problema {relacionado_copel} com a Copel, "
                f"a unidade {unidade_entrou_contato} com a mesma, e o prazo para resolução é de {resolucao_problema_energia} "
                f"e {motivo_problema_energia} informado o motivo para a indisponibilidade."
            )
            if motivo_problema_energia == "foi":
                print(motivo_escrito_problema_energia)
