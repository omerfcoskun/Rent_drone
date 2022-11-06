from django.contrib import admin
from .models import Iha
# Register your models here.
@admin.register(Iha)
class IhaAdmin(admin.ModelAdmin):
    #admin paneli özelleştirme
    list_display = ["marka","author","model","weight","category"]
    list_display_links = ["author","marka"]
    search_fields = ["marka"]
    class Meta:
        model = Iha