from flask import Flask, render_template, request, redirect
app = Flask(__name__)
from agenda import*
AGENDA = {}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/agenda')
def mostrar_agenda():
    # Simulação de dados para agenda de contatos
    contatos = visualizar_agenda()
    return render_template('agenda.html', contatos=contatos)
  
@app.route('/cadastrar-transportadora', methods=['GET', 'POST'])
def cadastrar_transportadora():
    if request.method == 'POST':
        # Capturar os dados do formulário
        nome = request.form['nome']
        cidades = request.form['cidades']
        numero = request.form['numero']
        email = request.form['email']
        observacao = request.form['observacao']

        # Aqui, você pode processar os dados, como salvar em um banco de dados
        # Para este exemplo, vamos apenas exibir os dados recebidos
        transportadora = {
            "nome": nome,
            "cidades": cidades,
            "numero": numero,
            "email": email,
            "observacao": observacao
        }

        return render_template('resultado_cadastro.html', transportadora=transportadora)

    return render_template('cadastrar_transportadora.html')

@app.route('/resultado_cadastro')
def resultado_cadastro():
    return "Página para mostrar resultado do cadastro."


def buscar_no_database(campo, valor):
  resultados = []
  with open('database.txt', 'r') as file:
      for linha in file:
          partes = linha.strip().split(',')
          if valor.lower() in partes[campo].lower():
              resultados.append({
                  'nome': partes[1],
                  'cidades': partes[2],
                  'numero': partes[3],
                  'email': partes[4],
                  'observacao': partes[5] if len(partes) > 5 else ''
              })
  return resultados

@app.route('/buscar-cidade', methods=['GET', 'POST'])
def buscar_cidade_view():
    """Rota para a busca por cidade."""
    contatos = []
    cidade = None

    if request.method == 'POST':
        cidade = request.form['cidade']
        contatos = buscar_cidade(cidade)

    return render_template('buscar_cidade.html', cidade=cidade, contatos=contatos)
  
@app.route('/buscar-transportadora', methods=['GET', 'POST'])
def buscar_transportadora():
  resultados = []
  nome = None
  if request.method == 'POST':
      nome = request.form['nome']
      resultados = buscar_no_database(1, nome)  # Índice 1 é o campo "Nome"

  return render_template('buscar_transportadora.html', nome=nome, resultados=resultados)


@app.route('/atualizar-cadastro')
def atualizar_cadastro():
    return render_template('atualizar_cadastro.html')

@app.route('/excluir-transportadora')
def excluir_transportadora():
    return render_template('excluir_transportadora.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)