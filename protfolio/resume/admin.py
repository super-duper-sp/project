from django.contrib import admin
from django.contrib import admin
from .models import MessageModel,EducationModel,ExperienceModel,AboutModel,SocialModel,BannerModel

admin.site.register(MessageModel)
admin.site.register(EducationModel)
admin.site.register(ExperienceModel)
admin.site.register(AboutModel)
admin.site.register(SocialModel)
admin.site.register(BannerModel)
admin.site.site_header = 'Portfolio: SHUBHAM PATIDAR'