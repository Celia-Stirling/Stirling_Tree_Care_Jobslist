from django.shortcuts import render
from django.urls import reverse_lazy
from .models import Customer, Job
from .forms import CustomerCreateForm, JobCreateForm, CustomerUpdateForm, JobUpdateForm
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

class CustomerUpdate(UpdateView):
    model = Customer
    template_name = "jobslist/customer_update_form.html"
    form_class = CustomerUpdateForm
    success_url = reverse_lazy('customer_list')

class JobUpdate(UpdateView):
    model = Job
    template_name = "jobslist/job_update_form.html"
    form_class = JobUpdateForm
    success_url = reverse_lazy('jobs_list')
