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

#Pegando somente a data
print(f'Retorna o apenas a data {data.date()}')

ano = timedelta(days=365)
outro_ano = timedelta(weeks=40,hours=23,minutes=50,seconds=600)
print(ano)
print(f'Calculando o numero de dias : {outro_ano}')
print(f'Total de segundos durante um ano : {ano.total_seconds()}')
print(f'Multiplicando os dias :{ano * 10}')

#Pegando a data atual
print(datetime.today())


print(data.year)

#Pegando o mes
print(data.month)

print(data.day)

print(f'{data.hour} horas')

print(f'{data.minute} minutos')

print(f'{data.second} segundos ')

print(f'{data.microsecond} microsegundos ')

#Substuindo valores na data, é possível trocar mais de uma coisa ao mesmo tempo
print(f'Trocando somente o dia da data armazenada : {data.replace(day=12)}')
print(f'Trocando somente o ano da data armazenada : {data.replace(year=2025)}')
print(f'Trocando somente o mes da data armazenada : {data.replace(month=12)}')

#Pegando dia da semana
diasSemana=('Segunda','Terça','Quarta','Quinta','Sexta','Sabado')
print(diasSemana[data.weekday()])

#Data por extenso
print(f'Data por extenso : {data.ctime()}')

print(data.strftime("Hoje é %A, dia %d de %B de %Y"))


print(datetime.now())




    