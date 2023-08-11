from django.urls import path
from enroll.views import student_registration_detail,successpage

urlpatterns = [
    path('registration01/',student_registration_detail),
    path('success/',successpage)
]