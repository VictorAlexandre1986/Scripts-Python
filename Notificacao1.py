#Para instalar
#pip install win10toast

from datetime import datetime
from win10toast import ToastNotifier

data = datetime.now().date()

data_formatada = data.strftime("%d/%m/%Y")

toaster = ToastNotifier()




toaster.show_toast("Alerta de data", data_formatada , duration=10)