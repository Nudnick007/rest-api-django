# Generated by Django 5.0.6 on 2024-07-12 07:17

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("app_main", "0026_alter_document_date"),
    ]

    operations = [
        migrations.AddField(
            model_name="purchaseorder",
            name="vendoralerts",
            field=models.CharField(max_length=500, null=True),
        ),
    ]
