# Generated by Django 4.2.2 on 2023-09-09 19:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dojo_ninjas_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='dojo',
            name='desc',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
    ]
