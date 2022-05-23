# Generated by Django 3.2.12 on 2022-05-23 21:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=255)),
                ('due_date', models.DateField(default='2000-01-01')),
                ('last_modified', models.DateField(auto_now=True)),
            ],
        ),
    ]
