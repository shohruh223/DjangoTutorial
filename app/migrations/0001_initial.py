# Generated by Django 4.2.1 on 2023-06-06 19:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='picture/')),
                ('fullname', models.CharField(max_length=55)),
                ('job', models.CharField(max_length=55)),
                ('address', models.CharField(max_length=100)),
            ],
        ),
    ]
