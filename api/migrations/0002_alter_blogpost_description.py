# Generated by Django 3.2.5 on 2023-03-29 07:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='description',
            field=models.TextField(),
        ),
    ]
