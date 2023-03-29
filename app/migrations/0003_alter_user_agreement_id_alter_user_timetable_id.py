# Generated by Django 4.1.7 on 2023-03-28 14:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("app", "0002_alter_user_exam"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="agreement_id",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="app.agreement",
                verbose_name="Идентификатор договора",
            ),
        ),
        migrations.AlterField(
            model_name="user",
            name="timetable_id",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="app.timetable",
                verbose_name="Идентификатор расписания практических занятий",
            ),
        ),
    ]
