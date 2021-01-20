from django.contrib.auth.forms import UserCreationForm
from django import forms 
from .models import *

class UserCreationForm_custom(UserCreationForm):
    email = forms.EmailField()
    first_name = forms.CharField()
    last_name = forms.CharField()

    class Meta():
        model = User
        fields = ('first_name','last_name','username', 'email', 'password1' ,'password2' )
    
class StudentForm(forms.ModelForm):
    
    class Meta:
        model = Student
        fields = ("escuela", "primaria_o_secundaria", "grado")

# class StudentRegistrationForm(forms.Form):
#     escuela = forms.CharField()
#     primaria_o_secundaria = forms.CharField()
#     grado = forms.IntegerField(max_value=6)
#     class Meta():
#         model = Student
#         fields = ('escuela', 'primaria_o_secundaria','grado')