from gtts import gTTS

from playsound import playsound

audio = 'speech.mp3'

language='pt-BR'

sp = gTTS(text="Esse texto vai ser convertido em audio.",lang=language,slow=False)

sp.save(audio)
#playsound(audio)