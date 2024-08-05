import time

# Código realizado para automatizar e facilitar a equipe de N1 na resposta de chamados na plataforma JIRA #

# Texto de Bem-vindo e apresentação das opções de indisponibilidade
print("Olá, seja bem-vindo ao programa de automação.")
print("1- Indisponibilidade de Energia")
print("2- Indisponibilidade de Link")
print("3- Indisponibilidade Interna")

# Solicita uma resposta do usuário para as indisponibilidades
while True:
    try:
        resposta = int(input("Selecione: "))
        if resposta in [1, 2, 3]:
            break
        else:
            print("Seleção inválida. Por favor, escolha 1, 2 ou 3.")
    except ValueError:
        print("Entrada inválida. Por favor, insira um número.")

# Caso seja problema de energia
if resposta == 1:
    unidade_energia = input("Qual unidade está com essa indisponibilidade? Informe: ")

    while True:
        try:
            relacionado_copel = int(input("O problema está relacionado com a Copel?\n1- Sim\n2- Não\nSelecione: "))
            if relacionado_copel in [1, 2]:
                break
            else:
                print("Seleção inválida. Por favor, escolha 1 ou 2.")
        except ValueError:
            print("Entrada inválida. Por favor, insira um número.")

    if relacionado_copel == 1:
        relacionado_copel = "está relacionado"
    else:
        relacionado_copel = "não está relacionado"

    if relacionado_copel == "está relacionado":
        while True:
            try:
                unidade_entrou_contato = int(input("A unidade já entrou em contato com a Copel?\n1- Sim\n2- Não\nSelecione: "))
                if unidade_entrou_contato in [1, 2]:
                    break
                else:
                    print("Seleção inválida. Por favor, escolha 1 ou 2.")
            except ValueError:
                print("Entrada inválida. Por favor, insira um número.")

        if unidade_entrou_contato == 1:
            unidade_entrou_contato = "entrou em contato"
            colaborador_contato = input("Qual colaborador você entrou em contato?")
            resolucao_problema_energia = True
        else:
            unidade_entrou_contato = "não entrou em contato"
            resolucao_problema_energia = False

        if resolucao_problema_energia:
            resposta_problema_energia = input('Informe o prazo abaixo da seguinte forma: "X"hrs\nExemplo: 8hrs\nPrazo: ')

        while True:
            try:
                motivo_problema_energia = int(input("Foi dado um motivo para o problema?\n1- Sim\n2- Não\nSelecione: "))
                if motivo_problema_energia in [1, 2]:
                    break
                else:
                    print("Seleção inválida. Por favor, escolha 1 ou 2.")
            except ValueError:
                print("Entrada inválida. Por favor, insira um número.")

        if motivo_problema_energia == 1:
            resposta_motivo_problema_energia = input("Qual a justificativa do problema? Nos informe: ")
        else:
            resposta_motivo_problema_energia = "Não informado"

        print("Aguarde, estamos processando seu chamado!")
        time.sleep(5)
        print("Chamado gerado!")

        print(
            f"Após analisarmos a unidade de {unidade_energia}, entramos em contato com o(a) {colaborador_contato} e"
            f" foi nos passado as seguintes informações: A unidade está sem energia e o problema {relacionado_copel} à Copel.\n"
            f"A unidade de {unidade_energia} já {unidade_entrou_contato} com a Copel."
        )

        if resolucao_problema_energia:
            print(f"O prazo para resolução é de {resposta_problema_energia}")
        else:
            print("Não foi definido um prazo para resolução")

        if motivo_problema_energia == 1:
            print(f"*{resposta_motivo_problema_energia}* foi informado como motivo para a indisponibilidade")
    else:
        print("Como o problema não está relacionado à Copel, favor verificar outras causas.")
else:
    print("Funcionalidade para as opções escolhidas ainda não implementada.")
