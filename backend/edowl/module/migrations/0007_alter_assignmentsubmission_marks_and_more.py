# Generated by Django 4.2.5 on 2023-11-09 13:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('module', '0006_assignment_created_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assignmentsubmission',
            name='marks',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True),
        ),
        migrations.AlterField(
            model_name='assignmentsubmission',
            name='remarks',
            field=models.CharField(blank=True, null=True),
        ),
    ]