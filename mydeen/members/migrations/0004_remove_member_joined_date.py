# Generated by Django 4.1.7 on 2023-02-21 06:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0003_alter_member_options_member_created_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='member',
            name='joined_date',
        ),
    ]
