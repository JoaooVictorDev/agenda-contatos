AGENDA = {}
# AGENDA['ligeirinho'] = {
#     'telefone':'32124545',
#     'cidades':'cascavel',
#     'codigo':'1452',
#     'obs':'detalhes da transportadora',
#     }
def visualizar_agenda():
  AGENDA = {}
  with open('AGENDA.txt', 'r') as arquivo:
    linhas = (arquivo.read()).split('none_')
    del linhas[15]
    for linha in linhas:
      contato = linha.split(',')
      nome = (contato[0]).replace('\n', '')
      telefone = contato[1]
      codigo = contato[2]
      cidades = contato[3]
      obs = contato[4]
      AGENDA[nome] = {
          'telefone': telefone,
          'codigo': codigo,
          'cidades': cidades,
          'obs': obs,
      }
  return AGENDA


def mostrar_contatos():
  for contato in AGENDA:
    print('Nome: ', contato)

def buscar_transportadora(contato):
  if contato in AGENDA:
    return 'Contato encontrado'
  else:
    return 'Contato nao encontrado'

def buscar_cidade(cidade):
  AGENDA = visualizar_agenda()  # Pega todos os contatos
  contatos_que_atendem_cidade = []
  
  # Iterar sobre todos os contatos no AGENDA
  for nome, detalhes in AGENDA.items():
    if cidade.lower() in detalhes['cidades'].lower():
          # Copiar detalhes do contato e adicionar o nome para cada contato
      detalhes_com_nome = detalhes.copy()
      detalhes_com_nome['nome'] = nome
      contatos_que_atendem_cidade.append(detalhes_com_nome)  # Adiciona o contato completo
  
  return contatos_que_atendem_cidade  # Retorna uma lista de dicionários


def adicionar_cadastro(trasnsportadora, telefone, cidades, email, codigo, obs):
  AGENDA[trasnsportadora] = {
      'telefone': telefone,
      'cidades': cidades,
      'codigo': codigo,
      'obs': obs,
  }
  print('Transportadora {} cadastrada com sucesso'.format(trasnsportadora))


def excluir_cadastro(transportadora):
  AGENDA.pop(transportadora)
  print('Transportadora {} excluida'.format(transportadora))
  pass
