from django import forms
from .models import Customer, Job

class CustomerCreateForm(forms.ModelForm):
  class Meta:
    model = Customer
    fields = ("first_name", "last_name", "phone", "email")

class JobCreateForm(forms.ModelForm):
  class Meta:
    model = Job
    fields = ("customer", "street", "town", "postcode", "type", "description", "price", "deadline")

class CustomerUpdateForm(forms.ModelForm):
  class Meta:
    model = Customer
    fields = ("first_name", "last_name", "phone", "email")

class JobUpdateForm(forms.ModelForm):
  class Meta:
    model = Job
    fields = ("customer", "street", "town", "postcode", "type", "description", "price", "deadline", "date_completed", "paid")
