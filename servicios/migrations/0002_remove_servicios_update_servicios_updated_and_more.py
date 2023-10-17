# Generated by Django 4.2.5 on 2023-10-06 09:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('servicios', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='servicios',
            name='update',
        ),
        migrations.AddField(
            model_name='servicios',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='servicios',
            name='imagen',
            field=models.ImageField(upload_to='servicios'),
        ),
    ]