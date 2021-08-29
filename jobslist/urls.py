from django.urls import path

from . import views

urlpatterns = [
  path("", views.home, name="home"),
  path("outstanding_jobs/", views.JobsList.as_view(), name="jobs_list"),
  path("completed_jobs/", views.CompletedJobsList.as_view(), name="completed_jobs_list"),
  path("customers/", views.CustomerList.as_view(), name="customer_list"),
]
