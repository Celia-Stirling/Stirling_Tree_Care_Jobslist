from django.shortcuts import render
from .models import Customer, Job
from .forms import CustomerCreateForm, JobCreateForm
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

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

class CustomerCreate(CreateView):
    model = Customer
    template_name = "jobslist/customer_create_form.html"
    form_class = CustomerCreateForm

class JobCreate(CreateView):
    model = Job
    template_name = "jobslist/job_create_form.html"
    form_class = JobCreateForm
