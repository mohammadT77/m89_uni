# Generated by Django 4.2 on 2023-05-03 16:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_student_alter_user_managers'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='student',
            options={'permissions': [('view_student_exams', 'Can view students exam')]},
        ),
    ]
