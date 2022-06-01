from distutils.log import info
from django.shortcuts import render, redirect
from .utils import render_to_pdf, sendEmail
from django.http import HttpResponse
from .forms import contactForm, paceinteForm, horaMedicaForm, informeForm
from .models import paciente, horaMedica, doctor, hora, informe
import random

# Create your views here.

def base(request):
    return render(request, 'web/base.html')

def index(request):
    return render(request, 'web/index.html')

def passr(request):
    return render(request, 'web/pass.html')

def tomahora(request):
    return render(request, 'web/tomahora.html')

def login(request):
    return render(request, 'web/login.html')

def contact(request): #CONTACTO

    msnform = contactForm()
    data = {'cform' : msnform}
    
    if request.method == 'POST':
        msnform = contactForm(data = request.POST) 
        if msnform.is_valid():
            msnform.save()
        else:
            data["cform"] = msnform;
        
        print("Mensaje enviado Correctamente")
    else:
        print("No se puedo enviar el mensaje, revisa los datos")
        
    return render(request, 'web/contact.html',  data)


def comisiones(request): #REGISTER USER
    informe = informeForm()
    data = {
        'form' : informeForm
    }
    informe = informeForm(data=request.POST)
    if request.method == 'POST':
        if informe.is_valid():
            informe.save()
            print("te has registrado correctamente")
        else:
            data['form'] = informe
    else:
        print('error en el formulario')
    return render(request, 'web/comisiones.html', data)


def register(request): #REGISTER USER
    paciente = paceinteForm()
    data = {
        'form' : paciente
    }
    paciente = paceinteForm(data=request.POST)
    if request.method == 'POST':
        if paciente.is_valid():
            paciente.save()
            print("te has registrado correctamente")
            return redirect('tomahora')
        else:
            data['form'] = paciente
    else:
        print('error en el formulario')
    return render(request, 'web/register.html', data)

def tomahora(request): #PEDIR HORA
    horaMed = horaMedicaForm()
    data = {
        'formTH' : horaMed
    }
    horaMed = horaMedicaForm(data=request.POST)
    if request.method == 'POST':
        if horaMed.is_valid():
            horaMed.save()
            print("te has registrado correctamente")
            datodoc = request.POST.get('fkMedico')
            doc = doctor.objects.get(id = datodoc)

            datopac = request.POST.get('fkPaciente')
            pac = paciente.objects.get(id= datopac)
            #emailPac = pac.emailPac
            

            datoHora = request.POST.get('fkPaciente')
            hor = hora.objects.get(id= datoHora)
            paciente = str(tHora.__getitem__('fkPaciente'))
            doctor = str(tHora.__getitem__('fkMedico'))
            fecha = request.POST.get('fecha')
            hora = str(tHora.__getitem__('fkHora'))

            msnData = "Hola " + str(pac) + " Has Agendado Correctamente Tu Horma Medica, El/la" + str(doc) + " te espera el " 
            + str(fecha) + " a las " + str(hor) + "hrs. No Faltes! \n Atte. Centro Medico Galenos."
            print(str(msnData))
            #print(str(emailPac))
            sendEmail(emailPac, msnData)
        else:
            data['form'] = horaMed
    else:
        print('error en el formulario')
    return render(request, 'web/tomahora.html', data)


def docs(request): #DOCTORES CRUD

    doc = doctor.objects.all()

    data = {
        'info' : doc
    }
    

    return render(request, 'web/docs.html', data)

def informeHoras(request, idDoc): #INFORME HORA CRUD
    
    horaMed = horaMedica.objects.filter(fkMedico=idDoc)
    
    data = {
        'info' : horaMed,
        'total' : horaMed.count()
    }

    return render(request, 'web/informeHoras.html', data)

def informePagos(request, idDoc): #INFORME HORA CRUD

    horaMed = horaMedica.objects.filter(fkMedico=idDoc)
    pagoTotal = 0;
    for i in horaMed:
        
        print(i.fkPago)
        pagoTotal = pagoTotal + int(str(i.fkPago))
        print(pagoTotal)

    data = {
        'info' : horaMed,
        'total' : pagoTotal
    }
    
    return render(request, 'web/informePagos.html', data)

def geninfoHM(request, idDoc):

    horaMed = horaMedica.objects.filter(fkMedico=idDoc)
    data = {
        'info' : horaMed,
        'total' : horaMed.count()
    }
    pdf = render_to_pdf('web/impresionHoras.html', data)
    return HttpResponse(pdf, content_type='application/pdf')

def geninfoPagosHM(request, idDoc):
    
    horaMed = horaMedica.objects.filter(fkMedico=idDoc)
    pagoTotal = 0;
    for i in horaMed:
        
        print(i.fkPago)
        pagoTotal = pagoTotal + int(str(i.fkPago))
        print(pagoTotal)

    data = {
        'info' : horaMed,
        'total' : pagoTotal
    }
    pdf = render_to_pdf('web/informePagos.html', data)
    return HttpResponse(pdf, content_type='application/pdf')

def gmail(request, idUser):
    horaMed = horaMedica.objects.filter(fkPaciente=idUser)
    msndata = "";

    for i in horaMed:
        print("Has Agendado Correctamente Tu Horma Medica, El/la" + i.fkMedico + " te espera el " \
            + i.fecha + " a las " + i.fkHora + "hrs. No Faltes! \n Atte. Centro Medico Galenos ")

def infoDoc(request, idDoc): #DATOS DE DOCTORES
    
    infodoc = doctor.objects.filter(id=idDoc)

    data = {
        'info' : infodoc,
    }    
    return render(request, 'web/infoDoc.html', data)

def informeComisiones(request): #INF
    
    infocomisiones = informe.objects.all()

    data = {
        'info' : infocomisiones,
        'total1' : infocomisiones.count()
    }    
    return render(request, 'web/informeComisiones.html', data)

def geninfoComision(request):
    
    informes = informe.objects.all()
    data = {
        'info' : informes,
        'total1' : informes.count()
    }
    pdf = render_to_pdf('web/impresionInformes.html', data)
    return HttpResponse(pdf, content_type='application/pdf')


def tomahora(request): #Toma Hora
    tHora = horaMedicaForm()
    data = {
        'formTH' : tHora
    }

    if request.method == 'POST':
        tHora = horaMedicaForm(data = request.POST)
        if tHora.is_valid():
            tHora.save()
            print("hora tomada correctamente")
            
            
        else:
            data["formTH"] = tHora
               
    else:
        print('error en el formulario TOMA DE HORA')

    return render(request, 'web/tomahora.html', data)

def borrarcita(request, idDoc): #ELIMINAR CITA
    horaMed = horaMedica.objects.get(id=idDoc)
    horaMed.delete()
    return redirect(to="informeHoras")

def agenda(request): #INF
    
    citas = horaMedica.objects.all()

    data = {
        'info' : citas,
    }    
    return render(request, 'web/agenda.html', data)
