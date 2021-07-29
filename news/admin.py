from django.contrib import admin
from .models import Articles,Journalists
# Register your models here.

admin.site.register(Journalists)

@admin.register(Articles)
class ArticlessAdmin(admin.ModelAdmin):
    list_display=('title','author','published_date','city','is_active')