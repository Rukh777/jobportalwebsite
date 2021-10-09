from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth import authenticate,login
from .forms import ResumeForm
from .models import Resume
from .forms import CustomerRegistrationForm
from django.contrib import messages
from django.db.models import Q
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth.models import User
from jobportal import settings
from django.core.mail import EmailMessage, send_mail
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.utils.encoding import force_bytes, force_text
from . tokens import generate_token 

@method_decorator(login_required, name='dispatch')
class ProductView(View):
    def get(self, request):
        totalitem = 0
        topwear = Product.objects.filter(category='TW')
        bottomwear = Product.objects.filter(category='BW')
        mobiles = Product.objects.filter(category='M')
        laptops = Product.objects.filter(category='L')
        if request.user.is_authenticated:
            totalitem = len(Cart.objects.filter(user=request.user))
        return render(request, 'app/home.html', {'topwear': topwear, 'bottomwear':bottomwear,
        'mobiles':mobiles,'laptop':laptops,'totalitem':totalitem })

@method_decorator(login_required, name='dispatch')
class ProductDetailView(View):
    def get(self, request, pk):
        totalitem = 0
        product = Product.objects.get(pk=pk)
        item_already_in_cart = False
        if request.user.is_authenticated:
            totalitem = len(Cart.objects.filter(user=request.user))
            item_already_in_cart = Cart.objects.filter(Q(product=product.id) & Q(user=request.user)).exists()
        return render(request,'app/productdetail.html',{'product':product,
        'item_already_in_cart':item_already_in_cart,'totalitem':totalitem })


def index(request):
 return render(request, 'app/index.html')

@login_required
def address(request):
    add = Customer.objects.filter(user=request.user)
    return render(request, 'app/address.html',{'add':add,'active':'btn-primary'})



class CustomerRegistration(View):
    def get(self, request):
        form = CustomerRegistrationForm()
        return render(request, 'app/customerregistration.html',{'form':form})
    def post(self, request):
        form = CustomerRegistrationForm(request.POST)
        if form.is_valid():
            nm = form.cleaned_data['username']
            em = form.cleaned_data['email']
            myuser = User.objects.create(username=nm, email=em)
            myuser.is_active = False
            
            messages.success(request, 'Congartulations!! Registered Successfully , We have sent you confirmation mail,please confirm your account to activate')
            myuser.save()
            
            #welcome email
            subject = "Welcome To Django Login"
            message = "Hello " + myuser.username + "!! \n" + "Welcome To CTC !! \n Thank You For Visiting Our Website"
            from_email =  settings.EMAIL_HOST_USER
            to_list = [myuser.email]
            send_mail(subject, message,from_email,to_list, fail_silently = True)

            #Email Address Confirmation Email
            current_site = get_current_site(request)
            email_subject = "Confirm Your Email @CTC - Django Login !!"
            message2 = render_to_string('app/email_confirmation.html',{
                'name':myuser.username,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(myuser.pk)),
                'token': generate_token.make_token(myuser)

            })
            email = EmailMessage(
                email_subject,
                message2,
                settings.EMAIL_HOST_USER,
                [myuser.email],
            )
            email.fail_silently = True
            email.send()

        return render(request, 'app/customerregistration.html',{'form':form})
        

@method_decorator(login_required, name='dispatch')
class ProfileView(View):
    def get(self, request):
        form  = CustomerProfileForm()
        return render(request, 'app/profile.html', {'form':form,'active':'btn-primary'})
    
    def post(self, request):
        form = CustomerProfileForm(request.POST)
        if form.is_valid():
            usr = request.user
            name = form.cleaned_data['name']
            locality = form.cleaned_data['locality']
            city = form.cleaned_data['city']
            state = form.cleaned_data['state']
            zipcode = form.cleaned_data['zipcode']
            reg = Customer(user=usr, name=name, locality=locality, city=city, state=state, zipcode=zipcode) 
            reg.save()   
            messages.success(request, 'Congartulations!! Profile Successfully ')
        return render(request, 'app/profile.html', {'form':form,'active':'btn-primary'})


def activate(request, uidb64, token,backend='django.contrib.auth.backends.ModelBackend'):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        myuser = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        myuser = None

    if myuser is not None and generate_token.check_token(myuser, token):
        myuser.is_active = True
        myuser.save()
        login(request, myuser, backend='django.contrib.auth.backends.ModelBackend',)
        return redirect('profile')
    else:
        return render(request, 'app/activation_failed.html')

#Resume Uploader

class HomeView(View):
    def get(self, request):
        form = ResumeForm()
        candidates = Resume.objects.all()
        return render(request, 'app/webpage.html',{'candidates':candidates, 'form':form})
    
    def post(self, request):
        form = ResumeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return render(request, 'app/webpage.html', {'form':form})
        else:
            form = ResumeForm()
            return render(request, 'app/webpage.html', {'form':form})

class CandidateView(View):
 def get(self, request, pk):
  candidate = Resume.objects.get(pk=pk)
  return render(request, 'app/candidate.html', {'candidate':candidate})