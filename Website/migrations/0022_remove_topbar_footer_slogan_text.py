# Generated by Django 3.1.7 on 2021-03-01 11:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Website', '0021_auto_20210301_0546'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='topbar_footer',
            name='slogan_text',
        ),
    ]
