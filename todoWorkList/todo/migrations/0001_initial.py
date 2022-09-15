# Generated by Django 4.1.1 on 2022-09-15 08:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Worklist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('discription', models.CharField(max_length=20)),
                ('startdate', models.DateField()),
                ('enddate', models.DateField()),
                ('email', models.EmailField(max_length=254)),
                ('isWorkDone', models.BooleanField(default=False)),
            ],
            options={
                'db_table': 'todo_Worklist',
            },
        ),
    ]