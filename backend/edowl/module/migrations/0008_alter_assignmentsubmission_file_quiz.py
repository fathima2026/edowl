# Generated by Django 4.2.5 on 2023-11-14 07:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('module', '0007_alter_assignmentsubmission_marks_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assignmentsubmission',
            name='file',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
        migrations.CreateModel(
            name='Quiz',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('quiz', models.JSONField()),
                ('total_mark', models.IntegerField(default=50)),
                ('created_time', models.TimeField(auto_now=True)),
                ('created_date', models.DateField(auto_now=True)),
                ('module', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='quiz', to='module.module')),
            ],
            options={
                'verbose_name': '8. quiz',
            },
        ),
    ]
