from django import forms
from . import models
choice_operator=(
    ('+','+'),
    ('-','-'),
    ('*','*'),
    ('/','/'),
)



class userForm(forms.Form):
    Value1 = forms.CharField(max_length=2, label='Value 1')
    Value2 = forms.CharField(widget=forms.TextInput(attrs={'class':'abc'}))

class myform(forms.Form):
    Fname=forms.CharField()
    Lname=forms.CharField()
    Email=forms.EmailField()
    Password=forms.PasswordInput()
    Phonenumber=forms.CharField()

class user1form(forms.Form):
    n1=forms.CharField(max_length=2)
    n2=forms.CharField(max_length=2)
    operator=forms.CharField( widget=forms.RadioSelect(choices=choice_operator))
    operator=forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple,choices=choice_operator)

class StudentForm(forms.ModelForm):
    class Meta:
        model = models.student
        fields = ['name', 'roll_no', 'email_id', 'exam_date']

class carForm(forms.ModelForm):
    class Meta:
        model=models.car
        fields=['name','color','price']