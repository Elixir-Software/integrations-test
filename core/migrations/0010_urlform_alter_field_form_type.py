# Generated by Django 4.1.7 on 2023-11-03 14:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("core", "0009_dateform_alter_field_form_type"),
    ]

    operations = [
        migrations.CreateModel(
            name="URLForm",
            fields=[
                (
                    "form_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="core.form",
                    ),
                ),
                ("type", models.CharField(default="url", editable=False, max_length=4)),
                ("value", models.URLField()),
            ],
            options={
                "abstract": False,
                "base_manager_name": "objects",
            },
            bases=("core.form",),
        ),
        migrations.AlterField(
            model_name="field",
            name="form_type",
            field=models.CharField(
                choices=[
                    ("CHAR", "SHORT TEXT"),
                    ("TEXT", "LARGE TEXT"),
                    ("INTEGER", "INTEGER"),
                    ("FLOAT", "DECIMAL"),
                    ("BOOLEAN", "CHECKBOX"),
                    ("DATE", "DATE"),
                    ("URL", "URL"),
                ],
                max_length=8,
            ),
        ),
    ]