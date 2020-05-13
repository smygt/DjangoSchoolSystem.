# Generated by Django 3.0.1 on 2020-01-15 11:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MainProject', '0041_auto_20200115_1428'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assistant',
            name='given_class',
            field=models.ManyToManyField(blank=True, related_name='given_class', to='MainProject.Lecture'),
        ),
        migrations.AlterField(
            model_name='assistant',
            name='taken_class',
            field=models.ManyToManyField(blank=True, related_name='taken_class', to='MainProject.Lecture'),
        ),
    ]