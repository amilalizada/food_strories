# Generated by Django 4.2.3 on 2023-09-15 16:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stories', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='slug',
            field=models.SlugField(default='slug', max_length=100),
            preserve_default=False,
        ),
    ]