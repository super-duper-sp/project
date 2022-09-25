from django.contrib import admin

from .models import ProjectModel,ExtraModel,AchievementModel
admin.site.register(ProjectModel)
admin.site.register(ExtraModel)
admin.site.register(AchievementModel)