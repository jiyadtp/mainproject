# Generated by Django 4.2.7 on 2023-11-25 07:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0003_courses_instructor_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='courses',
            name='contact_number',
            field=models.CharField(db_index=True, max_length=50, null=True),
        ),
    ]
