# Generated by Django 2.1.1 on 2018-09-06 10:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand', models.CharField(max_length=128)),
                ('model', models.CharField(max_length=128)),
                ('year', models.DateField(auto_now_add=True)),
                ('carname', models.CharField(max_length=128, unique='true')),
            ],
        ),
    ]