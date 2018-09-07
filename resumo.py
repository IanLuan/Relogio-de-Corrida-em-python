from geopy import distance
import datetime

# RESUMO
# Módulo com as funções relacionadas ao resumo da Atividade

def distanciaTotal(latitudes, longitudes): 
    # Calcula a Distância Total

    distanciaTotal = 0
    for i, lat in enumerate(latitudes):
        if i < len(latitudes) - 1:
            distanciaTotal += float(str(distance.distance((lat, longitudes[i]), (latitudes[i+1], longitudes[i+1])))[:-3])
        else:
            break
    return distanciaTotal

def ritmo(tempoTotal, distanciaTotal):
    # Calcula o Ritmo

    tempoTotal = tempoTotal.total_seconds()
    tempoTotal = tempoTotal / 60
    ritmo = tempoTotal / distanciaTotal

    return ritmo

def altitudes(altitudes):
    # Tudo relacionado à altitude
    # Precisa passar uma chave ('max', 'min')

    altitudeMax = float(max(altitudes))
    altitudeMin = float(min(altitudes))

    return {'max': altitudeMax, 'min': altitudeMin}

def bpms(bpms, timestamps, horaInicial):
    # Tudo relacionado aos BPMs
    # Precisa passar uma chave ('max', 'min', 'media)

    bpms = [int(x) for x in bpms]
    pesos = []
    media = 0
    bpmMax = max(bpms)
    bpmMin = min(bpms)

    for i, time in enumerate(timestamps):
        pesos.append(((datetime.datetime.fromtimestamp(int(time)) - horaInicial).total_seconds())/60)
        media += bpms[i] *  ((datetime.datetime.fromtimestamp(int(time)) - horaInicial).total_seconds())/60
    
    media = media / sum(pesos)

    return {'max': bpmMax, 'min': bpmMin, 'media': media}

def passos(passos, tempoTotal):
    # Calcula cadência de Passos
    
    cadencia = int(passos[-1]) / (tempoTotal.total_seconds() / 60)

    return cadencia
