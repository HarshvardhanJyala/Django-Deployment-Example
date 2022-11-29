from django.shortcuts import render
from app_five.forms import UserForm,UserProfileInfoForm

#for login all the imports tat are required:
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
#from django.contrib.urlresolvers import reverse
from django.contrib.auth.decorators import login_required


# Create your views here.

def index(request):
    return render(request, 'app_five/index.html')

@login_required
def special(request):
    return HttpResponse("Nice! You are logged in !")

#this decorators is required here in order to show logout only when there is already login done.
@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))

def register(request):
    registered = False

    if request.method == "POST":
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileInfoForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password) #set method - so that this will encrpt or hide from all users.
            user.save()

            profile = profile_form.save(commit=False) #marked false in order to avoid commit conflict with users data like name and password etc.Remember that this is customed data that we have added.
            profile.user = user

            if 'profile_pic' in request.FILES: #request.FILES for all capturing images in the posted data.
                profile.profile_pic = request.FILES['profile_pic']
            profile.save()
            registered = True
        else:
            print(user_form.errors, profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = UserProfileInfoForm()
    return render(request, 'app_five/registration.html',{'user_form':user_form, 'profile_form':profile_form,'registered':registered})
    #3rd argument is context which is dictionary sending 3 parameters in K,V pair - user_form, profile_form, registered.

def user_login(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse("index"))
            else:
                return HttpResponse("Account Inactive")
        else:
            print("SomeOne tried to login and Failed!!")
            print("Username: {} and Password: {}".format(username,password))
            return HttpResponse("Invalid User detail supplied!")
    else:
        return render(request,'app_five/login.html',{})
