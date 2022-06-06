from asyncio.windows_events import NULL
from django.db import models

# Create your models here.
class Mlwebapp(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField()
    completed = models.BooleanField(default=False)

    def _str_(self):
        return self.title
class CsvFiles(models.Model):
    date_created = models.DateTimeField(auto_now=True)
    csv_file = models.FileField(upload_to='csv_uploads/')

    # def _str_(self):
    #     return self.name