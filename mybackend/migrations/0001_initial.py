# Generated by Django 4.2.13 on 2024-05-23 00:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('name', models.TextField()),
                ('student_id', models.IntegerField(primary_key=True, serialize=False)),
                ('email', models.TextField()),
                ('department', models.TextField()),
                ('enter_date', models.DateField()),
            ],
        ),
    ]