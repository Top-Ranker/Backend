# Generated by Django 3.2.7 on 2021-09-29 06:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('top', '0002_alter_submission_dimension'),
    ]

    operations = [
        migrations.AddField(
            model_name='submission',
            name='input',
            field=models.TextField(blank=True, null=True),
        ),
    ]