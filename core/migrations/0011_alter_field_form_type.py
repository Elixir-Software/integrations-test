# Generated by Django 4.1.7 on 2023-11-03 16:17

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("core", "0010_urlform_alter_field_form_type"),
    ]

    operations = [
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
                max_length=16,
            ),
        ),
    ]
