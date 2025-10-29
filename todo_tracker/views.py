from django.shortcuts import render

# Create your views here.
from django.views.generic import View
from todo_tracker.models import Todo_track


class addTodoList(View):

    def get(self, request):

        form = Todo_track()

        return render(request,"add_task.html",{'form':form})

