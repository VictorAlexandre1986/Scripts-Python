import smtplib
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email import encoders
from email import message


class Gmail():
    
    
    def enviar_email(self,toEmail):
        corpo_email="""
            <p>Parágrafo</p>
            <p>Parágrafo</p>
        """
    
        msg = MIMEMultipart()
        msg["Subject"]="Assunto"
        msg["From"] = "email remetente"
        msg["To"] = toEmail
        password = "senha do app" #Essa senha não é a do email é a senha do app do gmail
        msg.add_header("Content-Type", "text/html")

        corpo = MIMEText(corpo_email)
        
        msg.attach(corpo)
        
        filename='Express.js Guide.pdf'
        with open(filename,'rb') as arquivo:
            att = MIMEBase('application', 'octet-stream')
            att.set_payload(arquivo.read())
        encoders.encode_base64(att)
        
        att.add_header("Content-Disposition",
                       f"attachment; filename= {filename}")
        
        msg.attach(att)
    
    
        s = smtplib.SMTP("smtp.gmail.com: 587")
        s.starttls()
    
        s.login(msg["From"], password)
        s.sendmail(msg["From"], [msg["To"]], msg.as_string().encode("utf-8"))
        print("Email enviado")
        
if __name__ == "__main__":
    email = Gmail()
    email.enviar_email()
    
    
    
    
    '''
O google bloqueia acessos de aplicações que ele julgar como não seguindo os padrões de segurança, 
o problema é que não fica muito claro quais os padrões requisitados além de não ser uma tarefa muito 
trivial para quem está realizando seus primeiros testes de comunicação com um servidor de emails.

Entretanto, para que isso não seja um empecilho em seus primeiros passos no mundo do envio e recebimento 
de emails, você pode liberar o acesso de apps mesmos seguros através das configurações de segurança da sua 
conta em https://myaccount.google.com/u/0/security?hl=pt:'''

""" É também necessário criar uma senha do app, para poder enviar o email"""