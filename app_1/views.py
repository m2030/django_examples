from django.shortcuts import render
from app_1.forms import UserProfileInfoForm,UserForm
from django.urls import reverse
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect,HttpResponse
# Create your views here.

def index(request):
    context_dict = {'text':'Hello world', 'number':100}
    return  render(request,'app_1/index.html',context_dict)

def other(request):
    return render(request,'app_1/other.html')

def relative(request):
    return render(request,'app_1/relative_url_templates.html')
   
def register(request):
    registered = False
    if request.method == "POST" :
        user_form = UserForm(data = request.POST)
        profile_form = UserProfileInfoForm(data = request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()


            ##user = user_form.save(commit=False)
            profile=profile_form.save(commit=False)
            profile.user = user

            if 'profile_pic' in request.FILES:
                profile.profile_pic=request.FILES['profile_pic']

            profile.save()

            registered = True
        else:
            print(user_form.errors,profile_form.errors)
            pass
    else:
        user_form = UserForm()
        profile_form = UserProfileInfoForm()

    
    return render(request,'app_1/registrations.html',{'user_form':user_form,'profile_form':profile_form,'registered':registered})

@login_required 
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))
@login_required 
def special(request):
    return HttpResponse("You are logged i ") 
def user_login (request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password') 

        user = authenticate(username=username,password=password)

        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('index'))


            else:
                return HttpResponse("ACCOUNT NOT ACTIVE")
        else:
            print("Some tried to login and faild")
            print("User : {} and password:{}".format(username,password))
            return HttpResponse("in valid login details supplied!")
    else:
        return render(request,'app_1/login.html',{})

