import smtplib, ssl
from email.message import EmailMessage
from io import BytesIO # nos ayuda a convertir un html en pdf
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa


def render_to_pdf(template_src, context_dict={}):
    template = get_template(template_src)
    html  = template.render(context_dict)
    result = BytesIO()
    pdf = pisa.pisaDocument(BytesIO(html.encode("ISO-8859-1")), result)
    if not pdf.err:
        return HttpResponse(result.getvalue(), content_type='application/pdf')
    return None

def sendEmail(gmail1, msnData):

    
    try:
        context1 = ssl.create_default_context()
        msj = EmailMessage()
        msj.set_content(msnData)
        msj['to'] = gmail1
        msj['from'] = 'imagineart.contact@gmail.com'
        msj['Subject'] = "Correo de Confirmacion, generado automaticamente."

        print(gmail1)
        #subject = "Correo de Confirmacion, generado automaticamente."
        #msn = 'Subject: {}\n\n{}'.format(subject, msnData)
        print(msnData)
        server = smtplib.SMTP(host='smtp.gmail.com', port= 587)
        server.starttls(context=context1)
        server.ehlo() 
        server.login(user='imagineart.contact@gmail.com', password='iart2020')
        server.send_message(msj)
        print("correo enviado exitosamente")
    except Exception as e:
        print("hubo un error al enviar correo")
        print(e)

    
    
