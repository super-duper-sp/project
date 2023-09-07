from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin


from .models import ProjectModel,ExtraModel,AchievementModel

# Register your models here.
class ProjectAdmin(SummernoteModelAdmin):
    summernote_fields = ('description',)


admin.site.register(ProjectModel)
admin.site.register(ExtraModel)
admin.site.register(AchievementModel)


