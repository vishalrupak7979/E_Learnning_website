# Generated by Django 4.0.4 on 2022-05-23 05:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Reg',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('schoolmark', models.CharField(max_length=200)),
                ('highschoolmark', models.CharField(max_length=200)),
                ('collegename', models.CharField(max_length=200)),
                ('cgpa', models.CharField(max_length=200)),
                ('aadharno', models.CharField(max_length=200)),
                ('phoneno', models.CharField(max_length=200)),
                ('address', models.CharField(max_length=200)),
            ],
        ),
    ]
