# Generated by Django 4.1.2 on 2022-10-31 20:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("recipes_book", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="recipe",
            name="dish_image",
            field=models.ImageField(upload_to="dish_photos/%Y/%m/%d"),
        ),
    ]
