import tempo
import resumo
import time

# MAIN
# Nesse arquivo estão presentes apenas as funções relacionadas à Apresentação dos Valores
# As funções que calculam os valores estão separadas nos módulos de cada Funcionalidade

def dataHoraDuracao():
    timestamps = todas_as_linhas[0].split()   # guardar os timestamps

    # Apresentação dos Valores
    print()
    print(6*'<>', 'Data, Hora e Duração', 6*'<>', '\n')
    print("Data: {} \nHorário: {} \nDuração: {}".format(tempo.data(timestamps), tempo.horarios(timestamps)['inicial'], tempo.duracao(timestamps)))


def resumoCorrida():

    comPausa = 'n' # input('Deseja considerar o tempo de pausa (y/n)? ')

    # Extração de dados considerando e desconsiderando Pausa
    if comPausa == 'n':
        distanciaTotal = resumo.distanciaTotal(latitudes, longitudes)
        tempoTotal = tempo.duracao(todas_as_linhas[0].split())

    horarioInicial, horarioFinal = tempo.conversao(todas_as_linhas[0].split())  # Salvar horario Final e Inicial

    # Apresentação dos Valores
    print()
    print(6*'<>', "Resumo Total da Atividade", 6*'<>', '\n')
    print("Distância Total: {:.4f} Km".format(distanciaTotal))
    print("Tempo Total:", tempoTotal)
    print("Ritmo Médio: {:.2f} mins/km".format(resumo.ritmo(tempoTotal, distanciaTotal)))


    try:   # O Arquvio pode não ter BPMs 
        print("Máximo BPM:", resumo.bpms(bpms, timestamps, horarioInicial)['max'])
        print("Mínimo BPM:", resumo.bpms(bpms, timestamps, horarioInicial)['min'])
        print("Média de BPMs pelo Tempo: {:.2f}".format(resumo.bpms(bpms, timestamps, horarioInicial)['media']))
    except:
       pass

    print("Altitude Máxima: {:.2f}".format(resumo.altitudes(altitudes)['max']))
    print("Altitude Mínima: {:.2f}".format(resumo.altitudes(altitudes)['min']))

    try:   # O Arquivo pode não ter Passos 
        print("Cadência Média de Passos:", resumo.passos(passos, tempoTotal))
    except:
        pass


def menu():
    op = ''

    # Loop do Menu
    while op != 4:
        print()
        print(6 * '<>', "Menu", 6*'<>', '\n')
        print("[1] - Data, Horário e Duração")
        print("[2] - Resumo Total da atividade")
        print("[3] - Resumo por KM da atividade")
        print("[4] - Ler novo Arquivo")
        print("[5] - Sair")
        op = int(input("\nOperação desejada: "))
        if op == 1:
            dataHoraDuracao()
        elif op == 2:
            resumoCorrida()
        elif op == 3:
            print("Em Construção...")
        elif op == 4:
            leitura()
        elif op == 5:
            quit() 


def leitura():
    # Declaração das Listas
    global bpms, latitudes, longitudes, altitudes, timestamps, todas_as_linhas
    
    bpms = []
    latitudes = []
    longitudes = []
    altitudes = []
    timestamps = []
    passos = []

    # Leitura do arquivo

    arq = input("Nome do Arquivo: ")

    try:
        with open(arq, "r") as arquivo:
            todas_as_linhas = arquivo.readlines()

            for linha in todas_as_linhas:
                if linha[0] == 'b':
                    bpms.append(linha[2:-1])
                elif linha[0] == 'l':
                    latitudes.append(linha[2:-1])
                elif linha[0] == 'n':
                    longitudes.append(linha[2:-1])
                elif linha[0] == 'a':
                    altitudes.append(linha[2:-1])
                elif linha[0] == 'r' and len(linha) > 1:
                    timestamps.append(linha[2:-1])
                elif linha[0] == 'p' and len(linha) > 1:
                    passos.append(linha[2:-1])
    except:
        leitura()
    
    menu()


leitura()