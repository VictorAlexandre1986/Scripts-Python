#Para instalar
#pip install winotify

from winotify import Notification, audio
from datetime import datetime

data = datetime.now().date()

toast = Notification(app_id="Alerta !!!",
                     title="Data",
                     msg=data,
                     duration="long",
                     #icon=r"C:\User|Victor\Documents\logo.jpg"
                     )

#criando um botao que vai redirecionar para a pagina do youtube
toast.add_actions(label="Clique Aqui",launch="https://www.youtube.com")

#Adicionando um audio para alarme
toast.set_audio(sound=audio.LoopingAlarm, loop=True)

toast.show()