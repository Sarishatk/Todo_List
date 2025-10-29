from django.shortcuts import render

# Create your views here.
from django.views.generic import View
from todo_tracker.forms import Todoform



class addTodoList(View):

    def get(self, request):

        form = Todoform()

        return render(request,"add_task.html",{'form':form})
    
    def post(self,request):

        

