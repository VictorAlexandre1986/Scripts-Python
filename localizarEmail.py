from imap_tools import MailBox, AND

usuario = 'teste@gmail.com'
senha = '123'

meu_email = MailBox('imap.gmail.com').login(usuario,senha)

#Pegar email que foram enviados por um remetente especifico

listaEmails = meu_email.fetch(AND(from_='noreply@nvidiadeveloper.com'))

print(f'Existe quantos e-mails com esse remetente ? {len(list(listaEmails))}')

#Pegar e-mail sobre o assunto ...
listaEmails2 = meu_email.fetch(AND(subject='Alerta'))

for email in listaEmails2:
    print(email.subject)
    print(email.text)
    
#Pegando anexo
listaEmails3 = meu_email.fetch(AND(from_='noreply@nvidiadeveloper.com'))
for email in listaEmails3:
    if len(email.attachments) > 0:
        for anexo in email.attachments:
            if 'Relatorio.pdf' in anexo.filename:
                informacoes_anexo = anexo.payload
                with open('CriandoArquivo','wb') as arquivo:
                    arquivo.write(informacoes_anexo)
                    
                    
meu_email.logout()
                