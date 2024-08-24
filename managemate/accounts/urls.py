from django.urls import path
from .views import signup_student, signup_mentor, login_view

urlpatterns = [
    path('signup/student/', signup_student, name='signup_student'),
    path('signup/mentor/', signup_mentor, name='signup_mentor'),
    path('login/', login_view, name='login'),
]
