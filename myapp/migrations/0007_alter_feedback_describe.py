# Generated by Django 4.1.7 on 2023-04-29 16:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0006_remove_feedback_status_feedback_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feedback',
            name='describe',
            field=models.CharField(max_length=500),
        ),
    ]
