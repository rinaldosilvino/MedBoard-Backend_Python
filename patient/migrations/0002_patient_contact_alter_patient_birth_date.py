# Generated by Django 4.1.5 on 2023-01-11 13:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("contact", "0003_remove_contact_employee_remove_contact_hospital_and_more"),
        ("patient", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="patient",
            name="contact",
            field=models.OneToOneField(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="contact.contact",
            ),
        ),
        migrations.AlterField(
            model_name="patient",
            name="birth_date",
            field=models.DateField(null=True),
        ),
    ]
