from django.contrib import admin
from django.contrib import admin
from .models import MessageModel,EducationModel,ExperienceModel

admin.site.register(MessageModel)
admin.site.register(EducationModel)
admin.site.register(ExperienceModel)