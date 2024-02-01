
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication

def enviar_email(nome_usuario, email_usuario):
    corpo_email = (f""" 
    <p style="background-color: #98FB98; border-radius: 10px; padding: 10px; font-size: 18px; text-align: center">
        Olá <b>{nome_usuario}</b>
    </p>
    <p style="font-size: 16px">Agradecemos por usar nossos serviços!<br>Os dados que está recebendo foram retirados do site <b>Amazon.com.br</b></p>
    <p style="font-size: 16px"><br>Segue em anexo uma tabela com informações sobre sua busca<br><br><br>Lembrando que estes são apenas alguns dos resultados<br>Para mais informações recomendamos que acesse o <a href="https://www.amazon.com.br/">site oficial</a></p>
    """)

    msg = MIMEMultipart()
    msg['Subject'] = "Tabela de Preços - Amazon"
    msg['From'] = '#removi'
    msg['To'] = email_usuario
    
    
    corpo = MIMEText(corpo_email, 'html')
    msg.attach(corpo)

  
    with open('Tabela de preços.csv', 'rb') as arquivo:
        anexo = MIMEApplication(arquivo.read(), _subtype="csv")
        anexo.add_header('Content-Disposition', 'attachment', filename='Tabela de preços.csv')
        msg.attach(anexo)


    s = smtplib.SMTP('smtp.gmail.com: 587')
    s.starttls()
    password = '#removi'
    s.login(msg['From'], password)
    s.sendmail(msg['From'], [msg['To']], msg.as_string().encode('utf-8'))
    s.quit()

    print("Email enviado")

