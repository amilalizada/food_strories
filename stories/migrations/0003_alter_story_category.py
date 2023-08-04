# Generated by Django 4.2.3 on 2023-07-19 20:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('stories', '0002_alter_recipe_category_alter_story_category_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='story',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='stories', to='stories.category'),
        ),
    ]