from django import forms
from todo_tracker.models import Todo_track

class Todoform(forms.ModelForm):

    class Meta:

        model = Todo_track

        fields = ['category','title','date','price','note']
        



    

      