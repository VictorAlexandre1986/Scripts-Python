import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.base import MIMEBase
from email import encoders


meu_email='email do remetente'
senha='senha do email'

msg = MIMEMultipart()
msg['from'] = 'Nome do remetente'
msg['to'] = 'E-mail do destinatario'
msg['subject']='Assunto'

texto='''
Ola mundo!!! 
Envinado uma imagem e um arquivo
'''
corpo = MIMEText(texto)

msg.attach(corpo)
with open('geckodriver.log','rb') as arquivo:
    att = MIMEBase('application', 'octet-stream')
    att.set_payload(arquivo.read())
    encoders.encode_base64(att)
    msg.attach(att)


with open ('CodigoBarras.png','rb') as imagem:
    img = MIMEImage(imagem.read())
    msg.attach(img)

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    try:
        smtp.ehlo()
        smtp.starttls()
        smtp.login(meu_email, senha)
        smtp.send_message(msg)
        print('E-mail enviado com sucesso')
    except Exception as e:
        print('Email não enviado!!!')

'''
O google bloqueia acessos de aplicações que ele julgar como não seguindo os padrões de segurança, 
o problema é que não fica muito claro quais os padrões requisitados além de não ser uma tarefa muito 
trivial para quem está realizando seus primeiros testes de comunicação com um servidor de emails.

Entretanto, para que isso não seja um empecilho em seus primeiros passos no mundo do envio e recebimento 
de emails, você pode liberar o acesso de apps mesmos seguros através das configurações de segurança da sua 
conta em https://myaccount.google.com/u/0/security?hl=pt:'''

