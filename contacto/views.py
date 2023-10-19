from django.shortcuts import render, redirect
from .forms import FormularioContacto
from django.core.mail import EmailMessage

# Create your views here.

def contacto(request):

    formulario_contacto = FormularioContacto()

    if request.method == 'POST':
        formulario_contacto = FormularioContacto(data = request.POST)
        if formulario_contacto.is_valid():
            nombre = request.POST.get("nombre")
            email = request.POST.get("email")
            contenido = request.POST.get("contenido")

            email = EmailMessage("Mensaje desde la APP de Django",
                                 "El usuario con el nombre {} de email {} envia el siguiente mensaje:\n\n {}".format(nombre, email, contenido),
                                 "",["alfyo89@gmail.com"], reply_to=[email])
            
            try:
                email.send()

                return redirect("/contacto/?correctopolis")
            
            except:
                
                return redirect("/contacto/?posNoFunco")

    return render(request, "contacto/contacto.html", {'miFormulario': formulario_contacto})