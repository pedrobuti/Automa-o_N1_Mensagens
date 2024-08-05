from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    data = request.json
    unidade_energia = data.get('unidade_energia')
    relacionado_copel = data.get('relacionado_copel')
    entrou_contato = data.get('entrou_contato')
    colaborador_contato = data.get('colaborador_contato', 'Não informado')
    prazo_resolucao = data.get('prazo_resolucao', 'Não definido')
    motivo_problema = data.get('motivo_problema')
    justificativa_problema = data.get('justificativa_problema', 'Não informado')

    mensagem_destacada = (
        f"Após analisarmos a unidade de {unidade_energia}, entramos em contato com o(a) {colaborador_contato} e "
        f"foi nos passado as seguintes informações: A unidade está sem energia e o problema {relacionado_copel} à Copel.\n"
        f"A unidade de {unidade_energia} já {entrou_contato} com a Copel.\n"
        f"O prazo para resolução é de {prazo_resolucao}\n"
        f"*{justificativa_problema}* foi informado como motivo para a indisponibilidade."
    )

    return jsonify({"message": mensagem_destacada})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
