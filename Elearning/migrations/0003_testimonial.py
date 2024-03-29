# Generated by Django 4.2 on 2023-05-04 01:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Elearning', '0002_expert'),
    ]

    operations = [
        migrations.CreateModel(
            name='Testimonial',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='testimonial_image')),
                ('name', models.CharField(max_length=50)),
                ('profession', models.CharField(max_length=50)),
                ('testimony', models.TextField()),
            ],
        ),
    ]
