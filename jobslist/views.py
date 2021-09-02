from django.shortcuts import render
from django.urls import reverse_lazy
from .models import Customer, Job
from .forms import CustomerCreateForm, JobCreateForm, CustomerUpdateForm, JobUpdateForm
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.views import LoginView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
def home(request):
    context = {"name": request.user}
    return render(request, "jobslist/home.html", context)

class Login(LoginView):
    template_name = 'jobslist/login.html'

class JobsList(LoginRequiredMixin, ListView):
    model = Job
    template_name = "jobslist/outstanding_jobs.html"

class CompletedJobsList(LoginRequiredMixin, ListView):
    model = Job
    template_name = "jobslist/completed_jobs.html"

class CustomerList(LoginRequiredMixin, ListView):
    model = Customer
    template_name = "jobslist/customers.html"

class CustomerCreate(LoginRequiredMixin, CreateView):
    model = Customer
    template_name = "jobslist/customer_create_form.html"
    form_class = CustomerCreateForm

class JobCreate(LoginRequiredMixin, CreateView):
    model = Job
    template_name = "jobslist/job_create_form.html"
    form_class = JobCreateForm

class CustomerUpdate(LoginRequiredMixin, UpdateView):
    model = Customer
    template_name = "jobslist/customer_update_form.html"
    form_class = CustomerUpdateForm
    success_url = reverse_lazy('customer_list')

class JobUpdate(LoginRequiredMixin, UpdateView):
    model = Job
    template_name = "jobslist/job_update_form.html"
    form_class = JobUpdateForm
    success_url = reverse_lazy('jobs_list')

class CustomerDelete(LoginRequiredMixin, DeleteView):
    model = Customer
    template_name = "jobslist/customer_delete_form.html"
    success_url = reverse_lazy('customer_list')

class JobDelete(LoginRequiredMixin, DeleteView):
    model = Job
    template_name = "jobslist/job_delete_form.html"
    success_url = reverse_lazy('jobs_list')
