# Generated by Django 4.1.3 on 2023-01-17 04:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Students',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('contact', models.IntegerField()),
                ('email', models.EmailField(max_length=254)),
                ('city', models.CharField(choices=[('Purnea', 'Purnea'), ('Patna', 'Patna'), ('Bhagalpur', 'Bhagalpur'), ('Bhopal', 'Bhopal'), ('indore', 'indore'), ('Delhi', 'Delhi'), ('Kolkata', 'Kolkata')], max_length=200)),
            ],
        ),
    ]
