from django.contrib import admin

# Register your models here.
from .models import *


class categoryAdmin(admin.ModelAdmin):
    list_display = ('cname', 'cpic', 'cdate')


admin.site.register(category, categoryAdmin)


class newsAdmin(admin.ModelAdmin):
    list_display = ('id', 'city', 'headlines', 'subject', 'newsdetail', 'newspic', 'ndate', 'ncategory')


admin.site.register(news, newsAdmin)


class notificationAdmin(admin.ModelAdmin):
    list_display = ('id', 'ndes', 'ndate')


admin.site.register(notification, notificationAdmin)


class videoAdmin(admin.ModelAdmin):
    list_display = ('id', 'vtitle', 'vdes', 'thumb', 'vlink', 'vdate')


admin.site.register(video, videoAdmin)


class sliderAdmin(admin.ModelAdmin):
    list_display = ('id', 'stitle', 'sdes', 'spic', 'sdate')


admin.site.register(slider, sliderAdmin)


class SignUpAdmin(admin.ModelAdmin):
    list_display = ('Firstname', 'LastName', 'Email', 'Dob', 'Password', 'ConfirmPassword')


admin.site.register(SignUp, SignUpAdmin)


class LoginAdmin(admin.ModelAdmin):
    list_display = ('Email', 'Password', 'confirmPassword')


admin.site.register(Login, LoginAdmin)
