# Generated by Django 4.0.4 on 2024-03-08 16:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('victor', '0002_home_resume'),
    ]

    operations = [
        migrations.AlterField(
            model_name='home',
            name='resume',
            field=models.FileField(default='pdf/resume.pdf', upload_to='pdf/'),
        ),
    ]