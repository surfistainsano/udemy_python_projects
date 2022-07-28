from string import Template
from datetime import datetime
from locale import LC_ALL, setlocale

from data_email import meu_email, minha_senha

from email.mime.multipart import MIMEMultipart
# MIMEMultipart estabelece um padrão para o e-mail como o assunto da msg, remetente e destinatário.
from email.mime.text import MIMEText
# MIMEText recebe o corpo do email (text/plantext/html)
from email.mime.image import MIMEImage
# MIMEImage recebe uma img, a fim de anexar ao e-mail
import smtplib  # é o que manda a msg em si. Logo, estabelece a conexão com o servidor smtp

setlocale(LC_ALL, 'pt_BR.utf-8')

data_atual = datetime.now().strftime('%A, %d de %B de %Y %H:%M:%S')

with open('template.html', 'r') as html:
    template = Template(html.read())
    corpo_msg = template.substitute(nome='Marilene', data=data_atual)

msg = MIMEMultipart()
msg['from'] = meu_email  # remetente
msg['to'] = meu_email  # destinatário
msg['subject'] = 'Atenção: este é um e-mail de testes.'

# é preciso compor o corpo da msg
corpo = MIMEText(corpo_msg, 'html')
# como a msg é do tipo html, é preciso informar no segundo parâmetro da classe.
# caso a msg for um texto comum: MIMEText('texto desejado')

# é preciso inserir o conteúdo de ->corpo<- na ->msg<-
# o método .attach() também anexa img sendo do tipo MIMEImage (abaixo)
msg.attach(corpo)

with open('DSC00213.JPG', 'rb') as img:  # open('file_name', 'rb') o modo rb indica que a imagem será lida em bytes
    img = MIMEImage(img.read())
    msg.attach(img)

with smtplib.SMTP(host='smtp.office365.com', port=587) as smtp:
    try:
        smtp.ehlo()  # msg de 'hello' para o servidor do e-mail
        smtp.starttls()  # informa ao servidor do e-mail que o conteúdo presente precisa ser criptografado
        smtp.login(meu_email, minha_senha)
        smtp.send_message(msg)
        print('E-mail enviado com sucesso.')
    except Exception as e:
        print('Erro inesperado', e)
