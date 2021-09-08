from django.urls import path, include
from django.contrib.auth.views import LogoutView
from . import views

urlpatterns = [
  path("", views.home, name="home"),
  path("login/", views.Login.as_view(), name="login"),
  path("logout/", LogoutView.as_view(), name="logout"),
  path("job/outstanding_jobs/", views.JobsList.as_view(), name="jobs_list"),
  path("job/completed_jobs/", views.CompletedJobsList.as_view(), name="completed_jobs_list"),
  path("customer/list", views.CustomerList.as_view(), name="customer_list"),
  path("customer/create", views.CustomerCreate.as_view(), name="customer_create"),
  path("job/create", views.JobCreate.as_view(), name="job_create"),
  path("customer/update/<pk>", views.CustomerUpdate.as_view(), name="customer_update"),
  path("job/update/<pk>", views.JobUpdate.as_view(), name="job_update"),
  path("customer/delete/<pk>", views.CustomerDelete.as_view(), name="customer_delete"),
  path("job/delete/<pk>", views.JobDelete.as_view(), name="job_delete"),
  path("customer/details/<pk>", views.CustomerDetails.as_view(), name="customer_details")
]
