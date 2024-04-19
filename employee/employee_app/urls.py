from employee_app.views import *
from django.urls import path
urlpatterns = [
  path("emp/",EmpDetail.as_view()),
  path("emp/<int:pk>",EmpDetail.as_view()),

]