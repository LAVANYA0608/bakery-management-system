from django import forms
from .models import Product

# Admin Registration Form
class AdminRegisterForm(forms.Form):
    email = forms.EmailField(label="Email", max_length=50, widget=forms.EmailInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label="Password", max_length=20, widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    
# Customer Registration Form
class CustomerRegisterForm(forms.Form):
    name = forms.CharField(label="Name", max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(label="Email", max_length=50, widget=forms.EmailInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label="Password", max_length=20, widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    address = forms.CharField(label="Address", max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    mobile_no = forms.CharField(label="Mobile No", max_length=10, widget=forms.TextInput(attrs={'class': 'form-control'}))

class LoginForm(forms.Form):
    email = forms.EmailField(max_length=50, required=True, label="Email")
    password = forms.CharField(widget=forms.PasswordInput(), required=True, label="Password")


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'image', 'price']