from django.contrib import admin
from django.contrib import admin
from .models import MessageModel,EducationModel,ExperienceModel,AttractModel,SocialModel

admin.site.register(MessageModel)
admin.site.register(EducationModel)
admin.site.register(ExperienceModel)
admin.site.register(AttractModel)
admin.site.register(SocialModel)

admin.site.site_header = 'Portfolio: SHUBHAM PATIDAR'