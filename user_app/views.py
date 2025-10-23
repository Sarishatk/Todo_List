from django.shortcuts import render
from django.views.generic import View
from user_app.forms import UserRegistrationForm
# Create your views here.


class RegisterView(View):

    def get(self,request):

        form = UserRegistrationForm()

        return render(request,"signup.html",{'form':form})



