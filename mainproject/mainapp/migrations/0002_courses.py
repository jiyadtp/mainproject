# Generated by Django 4.2.7 on 2023-11-25 06:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Courses',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_name', models.CharField(db_index=True, max_length=100, null=True)),
                ('course_type', models.CharField(db_index=True, max_length=10, null=True)),
                ('course_file', models.FileField(db_index=True, null=True, upload_to='course_file')),
                ('course_link', models.CharField(db_index=True, max_length=250, null=True)),
            ],
        ),
    ]
