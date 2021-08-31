from django.urls import path

from . import views

urlpatterns = [
  path("", views.home, name="home"),
  path("job/outstanding_jobs/", views.JobsList.as_view(), name="jobs_list"),
  path("job/completed_jobs/", views.CompletedJobsList.as_view(), name="completed_jobs_list"),
  path("customer/list", views.CustomerList.as_view(), name="customer_list"),
  path("customer/create", views.CustomerCreate.as_view(), name="customer_create"),
  path("job/create", views.JobCreate.as_view(), name="job_create"),
  path("customer/update/<pk>", views.CustomerUpdate.as_view(), name="customer_update"),
  path("job/update/<pk>", views.JobUpdate.as_view(), name="job_update"),
]
