# Generated by Django 5.0.6 on 2024-07-01 06:57

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("app_main", "0004_remove_purchaseorder_test"),
    ]

    operations = [
        migrations.CreateModel(
            name="document",
            fields=[
                ("Id", models.AutoField(primary_key=True, serialize=False)),
                ("DocName", models.CharField(max_length=255)),
                (
                    "Doc",
                    models.FileField(
                        blank=True, null=True, upload_to="app_main/files/"
                    ),
                ),
            ],
        ),
    ]
