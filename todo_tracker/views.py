from django.shortcuts import render,redirect

# Create your views here.
from django.views.generic import View,UpdateView
from todo_tracker.forms import Todoform
from todo_tracker.models import Todo_track
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy




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

            return redirect('home')
        

class todolistview(View):

    def get(self, request):

        alllist = Todo_track.objects.filter(user = request.user)

        return render(request,"list.html",{'alllist':alllist})



class DeleteList(View):

    def get(self, request,**kwargs):

        id = kwargs.get('pk')

        todo_list = get_object_or_404(Todo_track,id = id,user = request.user)

        todo_list.delete()

        return redirect("home")
    

class todoUpdate(UpdateView):

    model = Todo_track

    form_class = Todoform

    template_name = "update.html"

    success_url = reverse_lazy("home")