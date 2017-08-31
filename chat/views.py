from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.forms import ModelForm
from django.utils.encoding import force_bytes
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode
from django.shortcuts import render, redirect
from django.utils.encoding import force_text
from django.utils.http import urlsafe_base64_decode
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import send_mail, BadHeaderError, EmailMultiAlternatives
from chat.form import ContactForm
from .models import Chat
from django import forms
from django.template import Context
from django.template.loader import get_template
from django.conf import settings
from django.template import loader, Context
from chat.models import Createclass
from django.contrib.auth.models import User
from chat.form import SignUpForm, UserChangeForm, EditProfileform
from datetime import date
import ntpath
from django.template import loader
from django.template.loader import render_to_string
from datetime import datetime
import random
import string
from chat.tokens import account_activation_token


data={}
data1={}
abc= {}
abc1= {}
unique_id= {}
today = date.today()




def SubscriptionView(request):
    users = User.objects.all()
    chat = Createclass.objects.order_by('-id') 
    
	
    
	
    form = ContactForm(request.POST or None)
    if form.is_valid():
	
	form_Class = request.POST.getlist('class')
	text_Class = request.POST.getlist('class1')
	
	
	html_message = loader.render_to_string(
            'htm_file.html',
            {
                'form_class': form_Class,
                'text_class':  text_Class                  
            }
        ) 
	
	emailto = request.POST.getlist('email_to')
	#desc = request.POST.getlist('discription')
	
	asd=emailto
	
	print(asd)
	form_full_name = form.cleaned_data.get('full_name')
	sub = form.cleaned_data.get('subject')
	subject = sub
	from_email = settings.EMAIL_HOST_USER
	
	contact_message = " %s "%(
            
            form_Class
			
			)			
	send_mail(subject,
	        contact_message, 
			from_email,			
			asd, 
			fail_silently=False
			,html_message=html_message)
	return redirect('Function')		
    else:
        form = ContactForm()
        print(users)
    return render(request, 'forn.html', {'form': form, 'users': users, 'chat': chat})
	
class ServerForm(forms.ModelForm):
    class Meta:

        model = Createclass
        
        widgets = {
		
		
            'Title': forms.TextInput(attrs={'class': 'form-control','placeholder':'Enter Title'})
			,'Subject': forms.TextInput(attrs={'class': 'form-control','placeholder':'Enter Subject'})
			,'date': forms.DateTimeInput(attrs={'class': 'datetime-input'})
			,'From': forms.TextInput(attrs={'class':'form-control'})
			,'to': forms.TextInput(attrs={'class':'form-control'})
			,'instructor': forms.TextInput(attrs={'class': 'form-control','placeholder':'Enter instructor'})
			,'description': forms.TextInput(attrs={'class': 'form-control','placeholder':'Enter description'})
        }
	fields = ['Title','Subject','date','From','to','instructor','description','Image']
		

	
def server_create(request, template_name='server_form.html'):
    form = ServerForm(request.POST or None)
    if form.is_valid():
		Createclass =form.save(commit=False)
		Createclass.Image=request.FILES['Image']
		Createclass.user=request.user
		Createclass.save()
		return redirect('Function')
    return render(request, template_name, {'form':form})
	
def class1(request,template_name='class1.html'):
    chat = Createclass.objects.all()
    users = User.objects.all()
    print(users)
	    
	    
	
	
    return render(request, template_name,{'chat': chat,'users': users})
	
	
	
	
	
	
	
	
	
def signup(request):
    allowed_chars = ''.join((string.lowercase, string.uppercase, string.digits))
    unique_id = ''.join(random.choice(allowed_chars) for _ in range(32))
  #  print("--------------------")
  #  print(unique_id)
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
			#user.profile.utype = form.cleaned_data.get('utype')
			
            user.save()
            current_site = get_current_site(request)
            from_email = settings.EMAIL_HOST_USER
            email = form.cleaned_data.get('email')
           # render_to_string(
            
            html_message = loader.render_to_string('account_activation_email.html', {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': account_activation_token.make_token(user),
            })
            subject = 'Activate Your MySite Account'
            contact_message= 'hello'
            asd='jatinderharjinder95@gmail.com'
            send_mail(subject,
			contact_message,
			from_email,
			[email],
			fail_silently=False
			,html_message=html_message)
            return redirect('account_activation_sent')
    else:
        form = SignUpForm()
    return render(request, 'register.html', {'form': form})
	
def account_activation_sent(request):
    return render(request, 'account_activation_sent.html')

def activate(request, uidb64, token,
    backend='django.contrib.auth.backends.ModelBackend'):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.profile.email_confirmed = True
        user.save()
        login(request, user,
        backend='django.contrib.auth.backends.ModelBackend')
        return redirect('server_list')
    else:
        return render(request, 'account_activation_invalid.html')
	
		
def server_list(request, template_name='server_list.html'):
	users = User.objects.all()
	data['object_list'] = users
		
	return render(request, template_name)
	
def pay(request, template_name='pay.html'):
	
		
	return render(request, template_name)
	

def Function(request, template_name='rest.html'):
    
    chat = Createclass.objects.order_by('-id')
    users = User.objects.all()
    data['object_list'] = chat
   
    form_Class12 = request.POST.getlist('class12')

    
	
    
    print(form_Class12)
    id_tupple=(form_Class12)
    chat1 = Createclass.objects.filter(id__in=id_tupple)
    return render(request, template_name,{'chat': chat,'chat1': chat1,'users': users})
	#users = User.objects.all()
	
		
	
def Ateacher1(request, template_name='update.html'):

    users = User.objects.all()
	#data = {}
    data['object_list'] = users
    return render(request, template_name, data)
	
def Ateacher12(request, template_name='server_create12.html'):

    users = User.objects.all()
	#data = {}
    data['object_list'] = users
    return render(request, template_name, data)	

			
def server_update(request, pk, template_name='Addrest.html'):
    users = get_object_or_404(User, pk=pk) 
   
	
    form = EditProfileform(request.POST or None, instance=users)
    if form.is_valid():
        user=form.save()
		#user.refresh_from_db()  # load the profile instance created by the signal
        user.profile.utype = form.cleaned_data.get('utype')
        user.save()
        return redirect('Function')
    return render(request, template_name, {'form':form,'user':users})	
		   
def Home(request,pk,template_name='home.html'):
    createclass = get_object_or_404(Createclass, pk=pk)
    abc[''] = pk
	
	
    users = User.objects.all()
    time=datetime.now()
  
	
    c = Chat.objects.all()
    return render(request, template_name, {'time':time,'home': 'active', 'chat': c, 'object':createclass,'users': users})

	
def Post(request):
		
		
		if request.method == "POST":
			msg = request.POST.get('msgbox', None)
			img = request.POST.get('imagebox', None)
			print('-------------------')
			#img=ntpath.basename(img)
			print(img)
			#numone = (request.GET.get('object.Title', None))
			c = Chat(user=request.user, message=msg, name=abc,Image=img)
			if msg != '':
				c.save()
			return JsonResponse({ 'msg': msg,'img':img, 'user': c.user.username })
		else:
			return HttpResponse('Request must be POST.')
	
def Messages1(request):
    c = Chat.objects.all() 
    return render(request, 'messages.html', {'chat': c})
	
def Messages(request):
    
    c = Chat.objects.filter(name=abc)
	#filter(created__date=date.today())
    return render(request, 'messages.html', {'chat': c})
  
def server_delete(request, pk, template_name='server_confirm_delete.html'):
    createclass = get_object_or_404(Createclass, pk=pk)    
    if request.method=='POST':
        createclass.delete()
        return redirect('Function')
    return render(request, template_name, {'object':createclass})
	
def server_class(request, pk, template_name='server_class.html'):
    createclass = get_object_or_404(Createclass, pk=pk)    
    if request.method=='POST':
        
        return redirect('')
    return render(request, template_name, {'object':createclass})	
		