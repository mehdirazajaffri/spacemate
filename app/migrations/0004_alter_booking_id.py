# Generated by Django 4.2.6 on 2023-10-16 13:03

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):
    dependencies = [
        ("app", "0003_alter_room_amenities_delete_roomamenity"),
    ]

    operations = [
        migrations.AlterField(
            model_name="booking",
            name="id",
            field=models.UUIDField(
                default=uuid.uuid4, editable=False, primary_key=True, serialize=False
            ),
        ),
    ]