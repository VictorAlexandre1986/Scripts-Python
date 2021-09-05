import pyautogui


#Usando caixas de mensagens estilo javascript

#Função alert() exibe uma caixa de mensagem simples
var = pyautogui.alert(text = 'Sei la' ,title = 'Testando' ,button = 'OK'  )
print('Alert: ',var)

#A função confirm() retorna o texto do botao clicado
var = pyautogui.confirm(text = '', title = '', buttons = ['OK','Cancel'])
print('Confirm: ',var)

#A função prompt exibe uma caixa de mensagem e retorna o conteúdo ou null se estiver vazia
conteudo = pyautogui.prompt(text='Informe seu nome :', title='Informe seu nome',default='')
print('Prompt: ',conteudo)

#A função password usa uma mascara nos caracteres digitados
senha = pyautogui.password(text='Informe sua senha: ', title='Login: ', default='', mask='*')
print('Password',senha)
