# Generated by Django 4.2.6 on 2023-10-16 12:40

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("user", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="userprofile",
            name="deleted_at",
            field=models.DateTimeField(blank=True, editable=False, null=True),
        ),
    ]