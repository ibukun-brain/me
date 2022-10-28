from django.contrib import admin
from app.models import HNGProfile
# Register your models here.

@admin.register(HNGProfile)
class HNGProfileAdmin(admin.ModelAdmin):
    list_display = [
        "username",
        "backend",
        "age",
        "bio"
    ]