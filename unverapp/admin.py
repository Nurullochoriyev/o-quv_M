from django.contrib import admin
from .models import *

class StudentAdmin(admin.ModelAdmin):
    list_display = ('name','tel_nomer','email','created_ad','updated_ad')
    list_display_links = ['name']
    search_fields = ['name']
    # list_editable = ['updated_ad']


class CursAdmin(admin.ModelAdmin):
    list_display=('title','start_time','end_time','descripions','created_ad','updated_ad')
    list_display_links = ['title']
    search_fields = ['title']
    list_editable = ['descripions']
#



admin.site.register(Student, StudentAdmin)
admin.site.register(Curs, CursAdmin)

