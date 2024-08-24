from django.contrib import admin
from django.urls import path, include
from django.shortcuts import render

def student_dashboard(request):
    return render(request, 'student_dashboard.html')

def mentor_dashboard(request):
    return render(request, 'mentor_dashboard.html')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('dashboard/student/', student_dashboard, name='student_dashboard'),
    path('dashboard/mentor/', mentor_dashboard, name='mentor_dashboard'),
]
