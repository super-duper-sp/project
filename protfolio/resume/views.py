from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from .models import MessageModel,EducationModel,ExperienceModel
from django.apps import apps
ProjectModel = apps.get_model('pro','ProjectModel')


def resu(request):
    experience = ExperienceModel.objects.all()
    education = EducationModel.objects.all()
    project = ProjectModel.objects.all()

    if request.method=="POST":
        post=MessageModel()
        post.name=request.POST['name']
        post.email=request.POST['email']
        post.message=request.POST['message']
        post.save()
        return render(request, 'example.html')
    else:
        return render(request, 'example.html',{'experiences':experience,'educations':education ,'projects':project})



def lunch(request):
    return render(request, 'shubham.html')


"""
from django.http import HttpResponse
def extra(request):
    return HttpResponse("<h1>i am from resume app and function is extra</h1>")
"""