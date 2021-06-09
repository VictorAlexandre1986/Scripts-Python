from datetime import datetime,timedelta
from locale import setlocale,LC_ALL
from calendar import mdays, isleap,weekday,weekheader

data = datetime(2021,6,9,19,58,30)

print(data.strftime('%d/%m/%Y %H:%M:%S'))

data = datetime.strptime('20/04/2021', '%d/%m/%Y')
print(data)

data1 = datetime.strptime('23/04/2021', '%d/%m/%Y')
print(f'Pegando o timestamp :  ${data1.timestamp()} segundos')

data2 = datetime.fromtimestamp(1618887600.0)
print(data2)

#timedelta intervalo de tempo
print(f'Adicionando 5 dias : {data + timedelta(days=5)}')
print(f'Adicionando duas horas : ${data + timedelta(seconds=2*60*60)}')


#Diferança entre datas
data = datetime(2021,6,15,19,58,30)
data3  = datetime(2021,6,9,19,50,30)

dif = data1 - data3
print(f'Diferença de dias : {dif.days}')
print(f'Diferença de segundos : {dif.seconds}')

#Pegando somente  hora
print(data.time())

#------------------------trabalhando com calendario------------------------
#Formatando data por extenso
setlocale(LC_ALL,'pt_BR.utf-8')
dt = datetime.now()
formatacao = dt.strftime('%A, %d de %B de %Y')
print(f'Pegando a hora do dispositivo : {formatacao}')


print(f'Quantidade de dias dos 12 meses do ano : {mdays}')
mes_atual = int(dt.strftime('%m'))
print(f'Quantidade de dias do mês atual : {mdays[mes_atual]}')


print(f'Retorna se o ano é bissexto : {isleap(2021)}')

print(f'Retornando o dia da semana para a data especificada obs:o numero zero é segunda-feira:{weekday(2021,6,9)}')

print(f'Retorna o nome abreviado do dia da semana, o argumento é o tamanho da abreviação{weekheader(3)}')







    