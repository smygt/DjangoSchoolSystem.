# Generated by Django 2.2.7 on 2019-11-30 21:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('MainProject', '0012_instructor'),
    ]

    operations = [
        migrations.CreateModel(
            name='Assistant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('assistant_name', models.CharField(max_length=25, null=True)),
                ('assistant_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('given_class', models.ManyToManyField(related_name='given_class', to='MainProject.Lecture')),
                ('taken_class', models.ManyToManyField(related_name='taken_class', to='MainProject.Lecture')),
            ],
        ),
    ]