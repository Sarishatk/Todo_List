from django.shortcuts import render

# Create your views here.
from django.views.generic import View
from todo_tracker.forms import Todoform
from todo_tracker.models import Todo_track



class addTodoList(View):

    def get(self, request):

        form = Todoform()

        return render(request,"add_task.html",{'form':form})
    
    def post(self,request):

        print(request.POST)

        form = Todoform(request.POST)

        if form.is_valid():

            print(form.cleaned_data)

            todo_list = form.save(commit=False)

            todo_list.user = request.user

            todo_list.save()

            return render(request,"add_task.html",{'form':form})
        

class todolistview(View):

    def get(self, request):

        alllist = Todo_track.objects.filter(user = request.user)

        return render(request,"list.html",{'alllist':alllist})



