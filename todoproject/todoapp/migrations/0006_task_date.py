# Generated by Django 4.1.5 on 2023-02-02 07:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todoapp', '0005_alter_task_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='date',
            field=models.DateField(default='1989-06-15'),
            preserve_default=False,
        ),
    ]
