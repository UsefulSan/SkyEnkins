# Generated by Django 4.1.5 on 2023-01-24 09:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_alter_file_changed_alter_file_mark'),
    ]

    operations = [
        migrations.AlterField(
            model_name='file',
            name='created',
            field=models.DateField(auto_now_add=True),
        ),
    ]
