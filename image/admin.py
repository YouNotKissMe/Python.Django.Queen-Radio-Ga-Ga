from django.contrib import admin
from .models import Picture


# class PictureAdmin(admin.ModelAdmin):
#     list_display = ('lvl_one', 'lvl_two', 'lvl_three')


admin.site.register(Picture)
