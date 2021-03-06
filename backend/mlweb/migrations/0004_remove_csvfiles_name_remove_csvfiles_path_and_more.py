# Generated by Django 4.0.4 on 2022-06-05 09:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mlweb', '0003_csvfiles'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='csvfiles',
            name='name',
        ),
        migrations.RemoveField(
            model_name='csvfiles',
            name='path',
        ),
        migrations.AddField(
            model_name='csvfiles',
            name='csv_file',
            field=models.FileField(default=None, upload_to='csv_uploads/'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='csvfiles',
            name='date_created',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
