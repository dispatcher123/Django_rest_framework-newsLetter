# Generated by Django 3.2.5 on 2021-07-29 07:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0005_alter_articles_author'),
    ]

    operations = [
        migrations.RenameField(
            model_name='journalists',
            old_name='suername',
            new_name='surname',
        ),
    ]
