from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import CustomUser, Patient, Doctor
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserCreationForm

class CustomUserAdmin(UserAdmin):
    # add_form = CustomUserCreationForm
    model = CustomUser
    list_display = ['username', 'first_name', 'last_name', 'email', 'user_type']

admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Patient)
admin.site.register(Doctor)
