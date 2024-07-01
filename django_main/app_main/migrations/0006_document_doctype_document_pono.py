# Generated by Django 5.0.6 on 2024-07-01 09:09

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("app_main", "0005_document"),
    ]

    operations = [
        migrations.AddField(
            model_name="document",
            name="DocType",
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name="document",
            name="PONO",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="app_main.purchaseorder",
            ),
        ),
    ]