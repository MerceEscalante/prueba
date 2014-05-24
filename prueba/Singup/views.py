#python first
#django second
#your apps
#local directory

from django.conf import settings
from django.shortcuts import render, render_to_response, RequestContext, HttpResponseRedirect
from django.template.defaultfilters import stringfilter
from django.core.mail import send_mail
from django.contrib import messages

# Create your views here.

from .forms import SingUpForm

def thankyou(request):
    
    form = SingUpForm(request.POST or None)
    
    if form.is_valid():
            save_it = form.save(commit=False)
            save_it.save()
            #send_mail(subject, message, from_email, to_list, fail_silently=True)
            subject = 'Gracias por comprar con nosotros'
            message = 'Se le agradece cordialmente por preferir a C est exquis para realizar sus comprar de reposteria. Estaremos en contacto por el estado de su pedido'
            from_email = settings.EMAIL_HOST_USER
            to_list = [save_it.email]
            
            subject2 = 'Se acaba de realizar un pedido'
            message2 = 'Se acaba de realizar un pedido desde nuestra pagina por el usuario:' + ' ' + save_it.first_name + ' ' + save_it.last_name + ',' + ' ' + save_it.email + ',' + 'en la direccion' + '  ' + save_it.direccion + ',' + 'una cantidad de:' + ' ' + str(save_it.cantidad)
            from_email2 = settings.EMAIL_HOST_USER
            to_list2 = [settings.EMAIL_HOST_USER]
            
            send_mail(subject,message,from_email,to_list,fail_silently=False)
            
            send_mail(subject2,message2,from_email2,to_list2,fail_silently=False)
            
            messages.success(request, 'Gracias por ordenar con nosotros ')
            return HttpResponseRedirect('/thank-you/')
    
    return render_to_response("thankyou.html",locals(),context_instance=RequestContext(request))

def home(request):
    
    return render_to_response("signup.html",locals(),context_instance=RequestContext(request))

def aboutus(request):
    
    return render_to_response("aboutus.html",locals(),context_instance=RequestContext(request))

def productos(request):
    return render_to_response("productos.html",locals(),context_instance=RequestContext(request))
