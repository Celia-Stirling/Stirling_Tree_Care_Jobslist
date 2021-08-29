from django.shortcuts import render
from .models import Customer, Job
from django.views.generic import ListView

class JobsList(ListView):
  model = Job
  template_name = "jobslist/outstanding_jobs.html"

# Create your views here.
def home(request):
    return render(request, "jobslist/home.html")
