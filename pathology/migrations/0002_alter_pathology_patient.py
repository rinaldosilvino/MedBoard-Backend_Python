# Generated by Django 4.1.5 on 2023-01-11 13:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("patient", "0002_patient_contact_alter_patient_birth_date"),
        ("pathology", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="pathology",
            name="patient",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="pathology",
                to="patient.patient",
            ),
        ),
    ]
