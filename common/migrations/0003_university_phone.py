# Generated by Django 4.2.3 on 2023-09-30 07:21

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("common", "0002_alter_university_options"),
    ]

    operations = [
        migrations.AddField(
            model_name="university",
            name="phone",
            field=models.CharField(blank=True, max_length=13, null=True),
        ),
    ]
