# Generated by Django 3.1.7 on 2021-02-23 10:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Website', '0013_auto_20210222_1309'),
    ]

    operations = [
        migrations.AlterField(
            model_name='brands',
            name='description',
            field=models.TextField(max_length=200, verbose_name='Description'),
        ),
        migrations.AlterField(
            model_name='career',
            name='Description',
            field=models.TextField(max_length=200, verbose_name='Description'),
        ),
        migrations.AlterField(
            model_name='newsandevent',
            name='description',
            field=models.TextField(max_length=200, verbose_name='Description'),
        ),
        migrations.AlterField(
            model_name='products',
            name='description',
            field=models.TextField(max_length=200, verbose_name='Description'),
        ),
        migrations.AlterField(
            model_name='products',
            name='image',
            field=models.ImageField(default=1, upload_to=None, verbose_name='Product Image'),
            preserve_default=False,
        ),
    ]