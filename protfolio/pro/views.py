from django.shortcuts import render
from .models import ProjectModel
# Create your views here.


# Create your views here.
def projects(request):
     projects = ProjectModel.objects.all()
     return render(request, 'projects.html', {'projects':projects ,})


