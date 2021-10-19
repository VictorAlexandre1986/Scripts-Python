#pip install pipwin
#pipwin install pyaudio
#pip install SpeechRecognizer

import speech_recognition as sr

rec = sr.Recognizer()

print(sr.Microphone().list_microphone_names())

def CapturarVoz():
    with sr.Microphone() as mic:
        rec.adjust_for_ambient_noise(mic)
        print('Pode falar que eu vou gravar')
        audio = rec.listen(mic)
        texto = rec.recognize_google(audio,language="pt-BR") 
        print(texto)
        
def ArquivoAudio():
    arquivo = r"C:\audios\audio.wav"
    with rec.AudioFile(arquivo) as source:
        audio = rec.record(source)  
        
        print(rec.recognize_google(audio,language="pt-BR")) 