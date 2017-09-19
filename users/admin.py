from django.contrib import admin
from .models import UserProfile
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.admin import User


class UserProfileInLine(admin.StackedInline):
	model = UserProfile

class MyUserAdmin(UserAdmin):
	inlines = [
		UserProfileInLine,
	]

admin.site.unregister(User)
admin.site.register(User, MyUserAdmin)


# Register your models here.
