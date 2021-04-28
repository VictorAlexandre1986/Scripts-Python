import pyttsx3

texto="Ola mundo"

speaker = pyttsx3.init()

voices = speaker.getProperty('voices')

for voice in voices:
    #Identificando os sintetizadores de voz instalado no S.O
    print(voice, voice.id)

#Definindo o sintetizador
speaker.setProperty('voice', voices[0].id)

rate = speaker.getProperty('rate')
#Velocidade da fala
speaker.setProperty('rate',125)


volume = speaker.getProperty('volume')

#Definindo o volume, o valor entre 0 e 1
speaker.setProperty('volume', 1.0)


#Reproduzindo o audio
speaker.say(texto)

speaker.runAndWait()
speaker.stop()
