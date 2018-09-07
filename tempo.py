import datetime

# TEMPO
# Módulo que contém as funções relacionadas ao tempo (duração, datas, horários, etc)

def conversao(timestamps):
	# Conversão
	# Função para facilitar as próximas funções.

	dataEHoraInicial = datetime.datetime.fromtimestamp(int(timestamps[0]))
	dataEHoraFinal = datetime.datetime.fromtimestamp(int(timestamps[1]))

	return dataEHoraInicial, dataEHoraFinal


def duracao(timestamps):
	# Duração
	# parâmetro = lista com 2 timestamps que serão analisados.

	dataEHoraInicial, dataEHoraFinal = conversao(timestamps)
	duracao = dataEHoraFinal - dataEHoraInicial

	return duracao

def data(timestamps):
	# Data
	# Parâmetro = lista com 2 timestamps da primeira linha do arquivo
	# Obs: os 2 timestamps são recebidos apenas para facilitar, mas para a extração da data é utilizado apenas o de início.

	dataEHoraInicial, dataEHoraFinal = conversao(timestamps)
	data = dataEHoraInicial.strftime('%d-%m-%y')

	return data

def horarios(timestamps):
	# Horários
	# Parâmetro = Lista com 2 timestamps da primeira linha do arquivo
	# Para conseguir os horários basta chamar a função com a chave "inicial", para horário inicial, ou 'final', para horário final.

	dataEHoraInicial, dataEHoraFinal = conversao(timestamps)
	horarioInicial = dataEHoraInicial.strftime('%H:%M:%S')
	horarioFinal = dataEHoraFinal.strftime('%H:%M:%S')

	return {'inicial' : horarioInicial, 'final': horarioFinal}

def tempoTotal(lista):
	# Tempo total
	# Parâmetro = Registros do determinado período da corrida.
	# Ex: Período total --> Lista de todas as linhas do arquivo

	tempoTotal = duracao(lista[0].split())

	for i, linha in enumerate(lista):
		if linha[0] == 'p':
			inicioDaPausa = lista[i-1][2:-1]
			lista2 = lista[i:]

			for i2, linha2 in enumerate(lista2):
				if linha2[0] == 'e':
					fimDaPausa = lista2[i2][2:-1]
					tempoTotal -= duracao([inicioDaPausa, fimDaPausa])
					break

	return tempoTotal