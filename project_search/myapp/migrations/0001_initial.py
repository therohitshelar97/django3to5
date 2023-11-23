# Generated by Django 4.2.5 on 2023-11-23 10:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pname', models.CharField(max_length=100, null=True)),
                ('pprice', models.PositiveBigIntegerField(null=True)),
                ('desc', models.CharField(max_length=500, null=True)),
                ('category', models.CharField(max_length=100, null=True)),
            ],
        ),
    ]