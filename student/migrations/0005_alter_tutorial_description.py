# Generated by Django 5.1 on 2024-08-29 12:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0004_rename_tutorial_attachments_tutorial_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tutorial',
            name='description',
            field=models.TextField(max_length=100, null=True),
        ),
    ]
