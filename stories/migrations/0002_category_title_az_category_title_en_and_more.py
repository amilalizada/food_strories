# Generated by Django 4.2.3 on 2023-10-16 13:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('stories', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='title_az',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='category',
            name='title_en',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='recipe',
            name='long_description_az',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='recipe',
            name='long_description_en',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='recipe',
            name='short_description_az',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='recipe',
            name='short_description_en',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='recipe',
            name='slug',
            field=models.SlugField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='recipe',
            name='title_az',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='recipe',
            name='title_en',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='tag',
            name='title_az',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='tag',
            name='title_en',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='recipes', to='stories.category'),
        ),
    ]
