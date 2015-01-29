from django.contrib import admin
from models import MyUser


class UserAdmin(admin.ModelAdmin):
    pass
admin.site.register(MyUser, UserAdmin)
