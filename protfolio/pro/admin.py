from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin


from .models import ProjectModel,SkillsModel,ToolsModel

# Register your models here.
class ProjectAdmin(SummernoteModelAdmin):
    summernote_fields = ('description',)


admin.site.register(ProjectModel)
admin.site.register(ToolsModel)
admin.site.register(SkillsModel)


