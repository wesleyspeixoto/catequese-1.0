# Generated by Django 3.0.3 on 2020-02-14 19:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Turma',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('turma', models.CharField(max_length=50)),
                ('catequista', models.CharField(max_length=50)),
            ],
        ),
    ]
