# Generated by Django 5.0.6 on 2024-06-28 11:11

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("app_main", "0004_remove_purchaseorder_test"),
    ]

    operations = [
        migrations.CreateModel(
            name="Details",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("doc", models.FileField(null=True, upload_to="")),
            ],
        ),
    ]
