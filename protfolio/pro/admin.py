from django.contrib import admin

from .models import ProjectModel,ExtraModel
admin.site.register(ProjectModel)
admin.site.register(ExtraModel)