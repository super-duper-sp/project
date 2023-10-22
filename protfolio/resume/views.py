from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from blog.models import Post
from .models import MessageModel,EducationModel,ExperienceModel ,AboutModel, BannerModel
from django.apps import apps
BlogModel = apps.get_model('blog','Post')
ProjectModel = apps.get_model('pro','ProjectModel')
SkillsModel = apps.get_model('pro','SkillsModel')
ToolsModel=apps.get_model('pro','ToolsModel')

def resu(request):
    about = AboutModel.objects.all()
    banner = BannerModel.objects.all()
    blog =Post.objects.all()
    experience = ExperienceModel.objects.all()
    education = EducationModel.objects.all()
    project = ProjectModel.objects.all()
    Skills = SkillsModel.objects.all()
    Tools= ToolsModel.objects.all()
    if request.method=="POST":
        post=MessageModel()
        post.name=request.POST['name']
        post.email=request.POST['email']
        post.message=request.POST['message']
        post.save()
        return render(request, 'main/index.html')
    else:
        return render(request, 'main/index.html',{'Skills':Skills,'experiences':experience,'educations':education ,'projects':project ,'Tools':Tools ,'blogs':blog,'about':about , 'banner':banner})





def lunch(request):
    return render(request, 'shubham_loader/shubham.html')


"""
from django.http import HttpResponse
def extra(request):
    return HttpResponse("<h1>i am from resume app and function is extra</h1>")
"""