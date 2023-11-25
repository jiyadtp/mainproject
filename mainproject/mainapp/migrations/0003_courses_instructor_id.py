# Generated by Django 4.2.7 on 2023-11-25 06:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0002_courses'),
    ]

    operations = [
        migrations.AddField(
            model_name='courses',
            name='instructor_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='course_instructor_id', to='mainapp.instructor'),
        ),
    ]
