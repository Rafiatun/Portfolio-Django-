from unicodedata import category
from django.shortcuts import render

from Main.models import Education, Experience, Project, Skills
from .forms import *

# Create your views here.

def Portfolio(request):
    About="I am Rafiatun Ferdous Khan Lubaba, an undergraduate student at Chittagong University of Engineering and Technology's Department of Mechatronics and Industrial Engineering. I'm a technologist that appreciates learning new things outside of my academic life. In order to develop myself, I've been studying new subjects on a regular basis. For the past two years, I've been studying Python, Machine Learning, Deep Learning, Django, Front End Development, and Uipath."
    About_2="I've been working hard to improve myself on a regular basis. During my early years of university, I worked on some automation and web development projects and competed in a few contests. I'm actively working with organisations to enhance both my technical and soft abilities.As I previously indicated, I am involved in a variety of disciplines, and I also own an e-magazine platform called শোলোক। "
    skills=Skills.objects.all()
    education=Education.objects.all()
    experience= Experience.objects.all()
  
    project=Project.objects.all()
    cat_form=CategoryForm()

    context={
        'about' : About,
        'about_2': About_2,
        'skill': skills,
        'edu': education,
        'exp': experience,
        'project': project,
        'cat_form': cat_form
    }

    if request.method == "POST":
        cat_form=CategoryForm(request.POST)
        project=Project.objects.filter(category__icontains=cat_form['category'].value())

        context={
            'about' : About,
            'about_2': About_2,
            'skill': skills,
            'edu': education,
            'exp': experience,
            'project': project,
            'cat_form': cat_form

        }

    
    return render(request , 'index.html' , context)