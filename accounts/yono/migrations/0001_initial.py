# Generated by Django 4.2.2 on 2023-06-23 13:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='bankModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('accountno', models.IntegerField(max_length=50)),
                ('name', models.CharField(max_length=20)),
                ('balance', models.IntegerField(max_length=200)),
            ],
        ),
    ]
