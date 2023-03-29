# Generated by Django 4.1.7 on 2023-03-29 17:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("app", "0002_alter_car_options_alter_category_options_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="schedule",
            name="id_worker",
            field=models.ForeignKey(
                limit_choices_to={"id_post": 2, "is_worker": 1},
                on_delete=django.db.models.deletion.CASCADE,
                related_name="Worker",
                to=settings.AUTH_USER_MODEL,
                verbose_name="Сотрудник",
            ),
        ),
    ]
