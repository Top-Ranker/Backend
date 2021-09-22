from django.contrib import admin
from .models import User, problems
from django.contrib.auth.admin import UserAdmin
# Register your models here.

admin.site.register(User,UserAdmin)

UserAdmin.fieldsets += ("Custom fields set",{'fields' : ('age','country','field','profession','university',)}),

class ProblemsAdmin(admin.ModelAdmin):
    pass
admin.site.register(problems, ProblemsAdmin)