from django.contrib import admin
from .models import Dimension, User, Problem,Submission
from django.contrib.auth.admin import UserAdmin
# Register your models here.

admin.site.register(User,UserAdmin)
admin.site.register(Problem)
admin.site.register(Submission)
admin.site.register(Dimension)

UserAdmin.fieldsets += ("Custom fields set",{'fields' : ('age','country','field','profession','university',)}),
