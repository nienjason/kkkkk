# Generated by Django 2.2.10 on 2020-02-09 14:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='preface',
            field=models.ImageField(blank=True, null=True, upload_to='', verbose_name='筆電照片'),
        ),
    ]
