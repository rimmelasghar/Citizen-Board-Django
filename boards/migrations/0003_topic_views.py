# Generated by Django 4.1 on 2022-08-29 10:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('boards', '0002_alter_post_updated_by'),
    ]

    operations = [
        migrations.AddField(
            model_name='topic',
            name='views',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
