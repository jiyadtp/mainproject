# Generated by Django 4.2.7 on 2023-11-25 10:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0005_studentcourses'),
    ]

    operations = [
        migrations.AddField(
            model_name='courses',
            name='amount',
            field=models.CharField(db_index=True, max_length=10, null=True),
        ),
    ]