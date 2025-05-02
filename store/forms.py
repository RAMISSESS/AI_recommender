from django import forms
from .models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        exclude = ['tags']  # ✅ Exclude tags because it's AI-generated

