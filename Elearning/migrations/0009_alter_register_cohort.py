# Generated by Django 4.2 on 2023-05-06 07:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Elearning', '0008_register_remove_newsletter_instruction'),
    ]

    operations = [
        migrations.AlterField(
            model_name='register',
            name='cohort',
            field=models.CharField(choices=[('BY', 'Beginning of Year'), ('MY', 'Mid of Year'), ('EY', 'End of Year')], max_length=10),
        ),
    ]
