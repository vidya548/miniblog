from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm,UsernameField
from .models import Post

class Signform(UserCreationForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class':'form-control'}))
    password2 = forms.CharField(label='confirm Password( again)' ,widget=forms.PasswordInput(attrs={'class':'form-control'}))
    class Meta:
        model=User
        fields=['username','first_name','last_name','email']
        labels={'first_name':'First Name','last_name':'Last Name','email':'Email'}
        widgets={
                 'username':forms.TextInput(attrs={'class':'form-control'}),
                 'first_name': forms.TextInput(attrs={'class': 'form-control'}),
                 'last_name':forms.TextInput(attrs={'class':'form-control'}),
                 'email': forms.EmailInput(attrs={'class': 'form-control'}),

                }

class LoginForm(AuthenticationForm):
    username =UsernameField(widget=forms.TextInput(attrs={'autofocus':True,'class':'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'autofocus':True,'class':'form-control'}))


class PostForm(forms.ModelForm):
    class Meta:
        model=Post
        fields='__all__'
        labels={'title':'Title','decription':'Decription' }
        widgets={'tite':forms.TextInput(attrs={'class':'form-control'}),
                 'decription':forms.Textarea(attrs={'class':'form-control'}),
                 }