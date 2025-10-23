from django.shortcuts import render
from django.views.generic import View
from user_app.forms import UserRegistrationForm
from django.contrib.auth.models import User

# Create your views here.


class RegisterView(View):

    def get(self,request):

        form = UserRegistrationForm()

        return render(request,"signup.html",{'form':form})
    
    def post(self,request):

        print(request.POST)

        username = request.POST.get('username')

        first_name =  request.POST.get("first_name")

        last_name =  request.POST.get("last_name")

        password = request.POST.get("password")

        email =  request.POST.get("email")

        form = UserRegistrationForm()

        User.objects.create_user(username =username,first_name = first_name, last_name = last_name,password=password,email=email)

        return render(request,"signup.html",{'form':form})






