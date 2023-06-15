# Generated by Django 4.2 on 2023-06-15 18:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Aio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('marca', models.CharField(max_length=20)),
                ('modelo', models.CharField(max_length=20)),
                ('serie', models.CharField(max_length=50)),
                ('nombre', models.CharField(max_length=30)),
                ('apellido', models.CharField(max_length=30)),
                ('dni', models.CharField(max_length=8)),
            ],
        ),
        migrations.CreateModel(
            name='Celulares',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('marca', models.CharField(max_length=20)),
                ('modelo', models.CharField(max_length=20)),
                ('serie', models.CharField(max_length=50)),
                ('nombre', models.CharField(max_length=30)),
                ('apellido', models.CharField(max_length=30)),
                ('imei', models.DecimalField(decimal_places=0, max_digits=20)),
                ('dni', models.CharField(max_length=8)),
            ],
        ),
        migrations.CreateModel(
            name='Desktop',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('marca', models.CharField(max_length=20)),
                ('modelo', models.CharField(max_length=20)),
                ('serie', models.CharField(max_length=50)),
                ('nombre', models.CharField(max_length=30)),
                ('apellido', models.CharField(max_length=30)),
                ('dni', models.CharField(max_length=8)),
            ],
        ),
        migrations.CreateModel(
            name='Notebook',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('marca', models.CharField(max_length=20)),
                ('modelo', models.CharField(max_length=20)),
                ('serie', models.CharField(max_length=50)),
                ('nombre', models.CharField(max_length=30)),
                ('apellido', models.CharField(max_length=30)),
                ('dni', models.CharField(max_length=8)),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=40)),
                ('apellido', models.CharField(max_length=40)),
                ('dni', models.CharField(max_length=8)),
                ('email', models.CharField(max_length=40)),
            ],
        ),
    ]