
import pyttsx3

#--------------------Sintetizador de voz ---------------------------
engine = pyttsx3.init()

#Obtendo vozes disponiveis
voices = engine.getProperty('voices')

for voice in voices:
    print(voice.id, voice.name, voice.languages)


#O id da voz
engine.setProperty('voice','brazil')
#velocidade da voz
engine.setProperty('rate',120)
engine.setProperty('volume',1.0)         
    
engine.runAndWait()

#Loop principal
while True:
    #Pega a entrada do usuário
    frase = input(">") 
    if frase != "sair!":
        #Coloca frase na fila de processamento da engine
        engine.say(frase)
        #Executa os comandos da fila (no caso, say(frase) )
        engine.runAndWait()
    
    else:
        break

    
