from django.contrib import admin


# Register your models here.
from .models import Mlwebapp, CsvFiles

class MlwebAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'completed')

class CsvAdmin(admin.ModelAdmin):
    list_display = ('date_created', 'csv_file')
# Register your models here.

admin.site.register(Mlwebapp, MlwebAdmin)
admin.site.register(CsvFiles, CsvAdmin)