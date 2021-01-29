from django.contrib.auth.forms import UserCreationForm
from django import forms 
from .models import *
from crispy_forms.helper import FormHelper

class UserCreationForm_custom(UserCreationForm):
    email = forms.EmailField()
    first_name = forms.CharField()
    last_name = forms.CharField()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)

    class Meta():
        model = User
        fields = ('first_name','last_name','username', 'email', 'password1' ,'password2' )
    
class StudentForm(forms.ModelForm):
    escuela = forms.CharField()
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)

    class Meta:
        model = Estudiante
        fields = ("escuela", "grado")