# Generated by Django 3.2.7 on 2022-10-27 21:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='HNGProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=200)),
                ('backend', models.BooleanField(default=True)),
                ('age', models.PositiveSmallIntegerField(default=0)),
                ('bio', models.TextField(blank=True)),
            ],
        ),
    ]
