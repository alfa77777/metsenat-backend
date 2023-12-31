# Generated by Django 4.2.3 on 2023-07-24 11:45

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("sponsors", "0003_alter_sponsor_payment_type"),
    ]

    operations = [
        migrations.AlterField(
            model_name="sponsor",
            name="amount",
            field=models.PositiveBigIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name="sponsor",
            name="is_organization",
            field=models.BooleanField(default=False),
        ),
    ]
