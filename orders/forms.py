from django import forms
from .models import *

#дану форму створюємо без привязки до будь чого. Самі створюєм поля і т.д.
class CheckoutContactForm(forms.Form):
	name = forms.CharField(required=True)
	phone = forms.CharField(required=True)
		