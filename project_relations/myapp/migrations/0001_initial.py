# Generated by Django 4.2.5 on 2023-11-08 10:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sname', models.CharField(max_length=100, null=True)),
                ('age', models.IntegerField(null=True)),
                ('email', models.EmailField(max_length=255)),
                ('city', models.CharField(max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Projects',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ptitle', models.CharField(max_length=255, null=True)),
                ('pdescription', models.CharField(max_length=255, null=True)),
                ('student', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='myapp.student')),
            ],
        ),
    ]
