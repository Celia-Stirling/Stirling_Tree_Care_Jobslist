from django.urls import path

from . import views

urlpatterns = [
  path("", views.home, name="home"),
  path("outstanding_jobs/", views.JobsList.as_view(), name="jobs_list")
]
