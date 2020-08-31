from django.shortcuts import render
from .models import Experience
from .models import Education
from .models import Skills

def CV_list(request):
    exp = Experience.objects.all()
    education = Education.objects.all()
    skills = Skills.objects.all()
    return render(request, 'cv/CV_list.html', {'exp' : exp, 'education' : education, 'skills' : skills})
