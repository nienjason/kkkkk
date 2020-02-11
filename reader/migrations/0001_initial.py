# Generated by Django 2.2.10 on 2020-02-11 03:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Reader',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('realname', models.CharField(max_length=32, verbose_name='姓名')),
                ('tel', models.CharField(max_length=255, verbose_name='聯絡電話')),
                ('email', models.EmailField(max_length=254, verbose_name='電子信箱')),
            ],
        ),
    ]