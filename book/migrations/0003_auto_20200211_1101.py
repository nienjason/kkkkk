# Generated by Django 2.2.10 on 2020-02-11 03:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0002_book_preface'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='preface',
            field=models.ImageField(upload_to='', verbose_name='筆電照片'),
        ),
    ]
