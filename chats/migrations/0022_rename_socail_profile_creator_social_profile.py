# Generated by Django 4.2.1 on 2023-08-18 14:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chats', '0021_rename_insta_creator_socail_profile_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='creator',
            old_name='Socail_Profile',
            new_name='Social_Profile',
        ),
    ]
