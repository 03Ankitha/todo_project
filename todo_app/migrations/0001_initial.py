# Generated by Django 5.1.3 on 2024-11-12 07:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('time_required', models.IntegerField(null='False')),
                ('completed', models.BooleanField(default=False)),
            ],
        ),
    ]
