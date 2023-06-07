# Generated by Django 4.1.6 on 2023-02-19 12:43

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("ads", "0002_selection"),
    ]

    operations = [
        migrations.AddField(
            model_name="category",
            name="slug",
            field=models.SlugField(
                default=1,
                max_length=10,
                validators=[django.core.validators.MinLengthValidator(5)],
            ),
            preserve_default=False,
        ),
    ]
