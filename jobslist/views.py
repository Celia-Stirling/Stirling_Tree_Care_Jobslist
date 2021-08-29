from django.shortcuts import render
from .models import Customer, Job
from django.views.generic import ListView

# Create your views here.
def home(request):
    return render(request, "jobslist/home.html")

class JobsList(ListView):
    model = Job
    template_name = "jobslist/outstanding_jobs.html"

class CompletedJobsList(ListView):
    model = Job
    template_name = "jobslist/completed_jobs.html"

class CustomerList(ListView):
    model = Customer
    template_name = "jobslist/customers.html"
