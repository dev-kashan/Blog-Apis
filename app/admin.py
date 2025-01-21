from django.contrib import admin
from . models import *
admin.site.register(Category)
class BLogAdmin(admin.ModelAdmin):
    class Media:
        js = ("tiny.js",)
admin.site.register(Blog , BLogAdmin)
