from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from blog.models import Post
from .models import MessageModel,EducationModel,ExperienceModel ,AttractModel
from django.apps import apps
BlogModel = apps.get_model('blog','Post')
ProjectModel = apps.get_model('pro','ProjectModel')
ExtraModel = apps.get_model('pro','ExtraModel')
AchievementModel=apps.get_model('pro','AchievementModel')
def resu(request):
    extra = ExtraModel.objects.all()
    blog =Post.objects.all()
    experience = ExperienceModel.objects.all()
    education = EducationModel.objects.all()
    project = ProjectModel.objects.all()
    attract = AttractModel.objects.all()
    achieve=AchievementModel.objects.all()
    if request.method=="POST":
        post=MessageModel()
        post.name=request.POST['name']
        post.email=request.POST['email']
        post.message=request.POST['message']
        post.save()
        return render(request, 'example.html')
    else:
        return render(request, 'example.html',{'achieves':achieve,'experiences':experience,'educations':education ,'projects':project ,'attracts':attract ,'extras':extra,'blogs':blog })



def lunch(request):
    return render(request, 'shubham.html')


"""
from django.http import HttpResponse
def extra(request):
    return HttpResponse("<h1>i am from resume app and function is extra</h1>")
"""